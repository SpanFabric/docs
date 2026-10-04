"""Fail-closed semantic checks for active SpanGPU governance routes.

The repository-vendored ``markdown-it-py`` CommonMark parser is the single
authority for what Markdown renders as a link.  This module owns only the
subsequent SpanGPU-specific path canonicalization, classification, and
authorization decision.  It deliberately has no fallback parser: a missing,
shadowed, malformed, or altered vendored dependency rejects validation.

Backtick-delimited repository-root paths remain a SpanGPU direct-governance
form, but are read only from CommonMark ``code_inline`` tokens.  Raw HTML
navigation is deliberately unsupported and rejected from CommonMark HTML
tokens.  A historical target is never executable from active governance.
Structured provenance is independently recorded metadata; it does not
participate in navigation authorization.
"""
from __future__ import annotations

import base64
import csv
from dataclasses import dataclass
import hashlib
from html.parser import HTMLParser
import importlib
from pathlib import Path, PurePosixPath
import argparse
import re
import sys
from typing import Iterable


REGISTRY = PurePosixPath("governance/12-machine-readable/governance-entrypoints.yaml")
PROJECT_STATE = PurePosixPath("governance/PROJECT_STATE.yaml")
PROJECT_PROJECTION = PurePosixPath("governance/12-machine-readable/project.yaml")
PHASES = PurePosixPath("governance/12-machine-readable/phases.yaml")
PHASE_STATUS_SCHEMA = PurePosixPath("governance/12-machine-readable/phase-status-schema.yaml")
PHASE_DOCUMENT = PurePosixPath("governance/08-phases/PHASE-000-builderkit-organization-and-evidence-bootstrap.md")
PHASE_INDEX_YAML = PurePosixPath("governance/08-phases/INDEX.yaml")
PHASE_INDEX_MD = PurePosixPath("governance/08-phases/INDEX.md")
ROUTER = PurePosixPath("governance/09-codex/FIRST_CODEX_PROMPT.md")

LEGACY_TOKENS = (
    "stage a",
    "stage b",
    "pre-apply",
    "materialize-repositories.py --apply",
    "gh repo create",
    "bootstrap-repos",
    "bootstrap-workspace",
    "ready_for_phase_00",
    "github mutation is forbidden",
)
DIRECTIVE = re.compile(r"\b(?:run|execute|start|resume|use|follow|create)\b", re.IGNORECASE)
NEUTRALIZERS = re.compile(
    r"\b(?:not|never|forbidden|quarantined|superseded|historical|provenance|cannot)\b",
    re.IGNORECASE,
)

# Direct governance paths are a SpanGPU-specific instruction form.  The
# expression is applied exclusively to CommonMark ``code_inline`` tokens, not
# to raw Markdown source.
DIRECT_GOVERNANCE_PATH = re.compile(
    r"`(?P<destination>AGENTS\.md|governance/[^`\s]+)`"
)
HTTP_URL = re.compile(r"https?://[^\s]+\Z", re.IGNORECASE)
URI_SCHEME = re.compile(r"[A-Za-z][A-Za-z0-9+.-]*:")
LOCAL_PATH_SUFFIXES = (".md", ".yaml", ".yml", ".json")
VENDOR_ROOT = Path(__file__).resolve().parent / "_vendor"
VENDORED_DISTRIBUTIONS = {
    "markdown_it": ("markdown-it-py", "4.2.0", "markdown_it_py-4.2.0.dist-info"),
    "mdurl": ("mdurl", "0.1.2", "mdurl-0.1.2.dist-info"),
}
_COMMONMARK_PARSER = None


@dataclass(frozen=True)
class RawReference:
    source: str
    line: int
    form: str
    destination: str


@dataclass(frozen=True)
class ResolvedReference:
    source: str
    line: int
    form: str
    raw_destination: str
    canonical_target: str | None
    classification: str
    allowed: bool
    reason: str


@dataclass(frozen=True)
class StructuredProvenanceReference:
    source: str
    historical_target: str
    relationship: str
    line: int


class GovernanceRouteError(AssertionError):
    """A route could not be resolved safely or violates classification policy."""


def read(root: Path, relative: PurePosixPath) -> str:
    path = (root / Path(*relative.parts)).resolve()
    root_resolved = root.resolve()
    if root_resolved not in path.parents and path != root_resolved:
        raise GovernanceRouteError(f"path escapes repository root: {relative.as_posix()}")
    return path.read_text(encoding="utf-8")


def list_value(document: str, key: str) -> tuple[str, ...]:
    match = re.search(rf"(?m)^{re.escape(key)}:\n((?:^- [^\n]+\n?)+)", document)
    if not match:
        raise GovernanceRouteError(f"missing flat YAML list: {key}")
    return tuple(line[2:].strip() for line in match.group(1).splitlines() if line.strip())


def scalar(document: str, key: str, indent: int = 0) -> str:
    match = re.search(rf"(?m)^{' ' * indent}{re.escape(key)}: ([^\n]+)$", document)
    if not match:
        raise GovernanceRouteError(f"missing scalar {key}")
    return match.group(1).strip().strip("'")


def root_mapping(document: str, key: str) -> str:
    match = re.search(
        rf"(?ms)^{re.escape(key)}:\n(.*?)(?=^[^\s#][^:]*:|\Z)", document
    )
    if not match:
        raise GovernanceRouteError(f"missing root mapping {key}")
    return match.group(1)


def require_solo_owner_hosting_authority(document: str) -> None:
    """Enforce the active canonical hosting model without parsing permissive YAML."""
    hosting = root_mapping(document, "hosting_authority")
    required_fragments = (
        "  mode: SOLO_OWNER\n",
        "  independent_technical_review:\n    authority: FRESH_BREAKER\n    required: true\n",
        "  owner_acceptance:\n    authority: OWNER\n    required: true\n    may_be_pr_author: true\n",
        "  github_review:\n    human_approval_required: false\n    required_approvals: 0\n",
        "  branch_protection:\n    pull_request_required: true\n",
        "    - verification-gate\n    - bootstrap-integrity\n",
        "    force_push_allowed: false\n",
        "    deletion_allowed: false\n",
        "    admin_bypass_allowed: false\n",
        "    require_up_to_date: false\n",
    )
    for fragment in required_fragments:
        if fragment not in hosting:
            raise GovernanceRouteError(
                "SOLO_OWNER hosting_authority is incomplete or weakened: " + fragment.strip()
            )


def phase_block(document: str, phase_id: str) -> str:
    match = re.search(rf"(?ms)^- id: {re.escape(phase_id)}\n(.*?)(?=^- id:|\Z)", document)
    if not match:
        raise GovernanceRouteError(f"missing phase: {phase_id}")
    return match.group(0)


def phase_status(document: str, phase_id: str) -> str:
    return scalar(phase_block(document, phase_id), "status", indent=2)


def registry(root: Path) -> tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
    document = read(root, REGISTRY)
    return (
        list_value(document, "active_entrypoints"),
        list_value(document, "historical_superseded"),
        list_value(document, "historical_evidence"),
    )


def structured_provenance_references(root: Path) -> tuple[StructuredProvenanceReference, ...]:
    """Read provenance metadata that is intentionally separate from routing.

    The registry permits only an empty list or canonical source/historical-target
    triples.  It is never consulted by the executable-reference resolver.
    """
    document = read(root, REGISTRY)
    empty = re.search(r"(?m)^structured_provenance: \[\]\s*$", document)
    if empty:
        return ()
    block = re.search(
        r"(?ms)^structured_provenance:\n(?P<items>(?:^- source: [^\n]+\n  historical_target: [^\n]+\n  relationship: provenance\n?)+)",
        document,
    )
    if not block:
        raise GovernanceRouteError("structured_provenance must be [] or exact source/historical_target provenance triples")
    references: list[StructuredProvenanceReference] = []
    pairs: set[tuple[str, str]] = set()
    item_pattern = re.compile(
        r"(?m)^- source: (?P<source>[^\n]+)\n  historical_target: (?P<target>[^\n]+)\n  relationship: (?P<relationship>provenance)$"
    )
    for match in item_pattern.finditer(block.group("items")):
        source, target = match.group("source"), match.group("target")
        try:
            canonical_source = canonical_registry_path(source)
            canonical_target = canonical_registry_path(target)
        except GovernanceRouteError as error:
            raise GovernanceRouteError(f"invalid structured provenance reference: {error}") from error
        if (canonical_source, canonical_target) in pairs:
            raise GovernanceRouteError("duplicate structured provenance reference")
        pairs.add((canonical_source, canonical_target))
        references.append(
            StructuredProvenanceReference(
                canonical_source,
                canonical_target,
                match.group("relationship"),
                line_number(document, block.start("items") + match.start()),
            )
        )
    return tuple(references)


def canonical_registry_path(raw: str) -> str:
    """Validate an already repository-relative registry identity."""
    if not raw or raw.startswith("/") or "\\" in raw or "%" in raw:
        raise GovernanceRouteError(f"non-canonical registry path: {raw!r}")
    parts = raw.split("/")
    if any(part in {"", ".", ".."} for part in parts):
        raise GovernanceRouteError(f"non-canonical registry path: {raw!r}")
    return "/".join(parts)


def _is_within(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return True


def _metadata_field(metadata: str, field: str) -> str | None:
    prefix = f"{field}: "
    for line in metadata.splitlines():
        if line.startswith(prefix):
            return line[len(prefix) :]
    return None


def line_number(text: str, offset: int) -> int:
    """Return a source line for metadata diagnostics, not Markdown parsing."""
    return text.count("\n", 0, offset) + 1


def _validate_vendored_distribution(module_name: str) -> tuple[Path, str]:
    """Verify a vendored runtime package before it can acquire parser authority.

    The original wheel archives are intentionally not required at runtime. The
    retained wheel payload is checked against its wheel ``RECORD`` hashes. A
    RECORD path must identify a file within the vendored import root; there is
    no exception for installer-generated files outside that root.
    """
    try:
        distribution_name, expected_version, info_name = VENDORED_DISTRIBUTIONS[module_name]
    except KeyError as error:
        raise GovernanceRouteError(f"unknown required vendored module: {module_name}") from error
    script_root = Path(__file__).resolve().parent
    vendor_root = VENDOR_ROOT.resolve()
    if not _is_within(vendor_root, script_root) or vendor_root == script_root:
        raise GovernanceRouteError("vendored CommonMark root escapes the repository scripts directory")
    package_root = vendor_root / module_name
    info_root = vendor_root / info_name
    metadata_path = info_root / "METADATA"
    record_path = info_root / "RECORD"
    if not vendor_root.is_dir() or not package_root.is_dir() or not (package_root / "__init__.py").is_file():
        raise GovernanceRouteError(f"vendored CommonMark dependency is missing: {module_name}")
    if not metadata_path.is_file() or not record_path.is_file():
        raise GovernanceRouteError(f"vendored CommonMark metadata is missing: {distribution_name}")
    try:
        metadata = metadata_path.read_text(encoding="utf-8")
    except OSError as error:
        raise GovernanceRouteError(f"cannot read vendored CommonMark metadata: {distribution_name}") from error
    if _metadata_field(metadata, "Name") != distribution_name or _metadata_field(metadata, "Version") != expected_version:
        raise GovernanceRouteError(f"vendored CommonMark version mismatch: {distribution_name}")
    try:
        with record_path.open("r", encoding="utf-8", newline="") as handle:
            rows = tuple(csv.reader(handle))
    except (OSError, csv.Error) as error:
        raise GovernanceRouteError(f"cannot parse vendored CommonMark RECORD: {distribution_name}") from error
    if not rows:
        raise GovernanceRouteError(f"empty vendored CommonMark RECORD: {distribution_name}")
    for row in rows:
        if len(row) != 3 or not row[0]:
            raise GovernanceRouteError(f"malformed vendored CommonMark RECORD: {distribution_name}")
        record_relative = PurePosixPath(row[0])
        if record_relative.is_absolute():
            raise GovernanceRouteError(f"absolute vendored CommonMark RECORD path: {distribution_name}")
        if any(part in {"", ".", ".."} for part in record_relative.parts):
            raise GovernanceRouteError(f"non-canonical vendored CommonMark RECORD path: {distribution_name}")
        target = vendor_root.joinpath(*record_relative.parts)
        if not _is_within(target, vendor_root) or not target.is_file():
            raise GovernanceRouteError(f"missing vendored CommonMark RECORD payload: {row[0]}")
        if not row[1] and record_relative.as_posix() == f"{info_name}/RECORD":
            continue
        match = re.fullmatch(r"sha256=([A-Za-z0-9_-]+)", row[1])
        if not match or not row[2].isdigit():
            raise GovernanceRouteError(f"invalid vendored CommonMark RECORD hash: {row[0]}")
        payload = target.read_bytes()
        digest = base64.urlsafe_b64encode(hashlib.sha256(payload).digest()).decode("ascii").rstrip("=")
        if digest != match.group(1) or len(payload) != int(row[2]):
            raise GovernanceRouteError(f"vendored CommonMark payload integrity mismatch: {row[0]}")
    return vendor_root, expected_version


def _load_vendored_commonmark_parser():
    """Load only the pinned repo-local parser and fail closed on any shadowing."""
    global _COMMONMARK_PARSER
    if _COMMONMARK_PARSER is not None:
        return _COMMONMARK_PARSER
    vendor_root, markdown_version = _validate_vendored_distribution("markdown_it")
    _, mdurl_version = _validate_vendored_distribution("mdurl")
    for module_name in VENDORED_DISTRIBUTIONS:
        for loaded_name, module in tuple(sys.modules.items()):
            if loaded_name != module_name and not loaded_name.startswith(f"{module_name}."):
                continue
            module_file = getattr(module, "__file__", None)
            if not module_file or not _is_within(Path(module_file), vendor_root):
                raise GovernanceRouteError(f"non-vendored CommonMark module already loaded: {loaded_name}")
    vendor_text = str(vendor_root)
    if vendor_text in sys.path:
        sys.path.remove(vendor_text)
    sys.path.insert(0, vendor_text)
    try:
        markdown_it = importlib.import_module("markdown_it")
        mdurl = importlib.import_module("mdurl")
        from markdown_it import MarkdownIt
    except Exception as error:
        raise GovernanceRouteError("vendored CommonMark parser import failed") from error
    for module_name, module, expected_version in (
        ("markdown_it", markdown_it, markdown_version),
        ("mdurl", mdurl, mdurl_version),
    ):
        module_file = getattr(module, "__file__", None)
        if not module_file or not _is_within(Path(module_file), vendor_root):
            raise GovernanceRouteError(f"CommonMark import escaped vendor root: {module_name}")
        if getattr(module, "__version__", None) != expected_version:
            raise GovernanceRouteError(f"vendored CommonMark runtime version mismatch: {module_name}")
    if _COMMONMARK_PARSER is None:
        try:
            _COMMONMARK_PARSER = MarkdownIt("commonmark", {"html": True})
        except Exception as error:
            raise GovernanceRouteError("vendored CommonMark parser initialization failed") from error
    return _COMMONMARK_PARSER


class _RawHtmlNavigationDetector(HTMLParser):
    """Identify browser navigation primitives contained in parser-emitted HTML."""

    _NAVIGATION_ATTRIBUTES = {
        "a": {"href"},
        "area": {"href"},
        "base": {"href"},
        "form": {"action"},
        "button": {"formaction"},
        "input": {"formaction"},
        "iframe": {"src"},
        "frame": {"src"},
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.destinations: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        names = self._NAVIGATION_ATTRIBUTES.get(tag.lower(), set())
        for name, value in attrs:
            if name.lower() in names:
                self.destinations.append("" if value is None else value)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)


def _raw_html_navigation_references(source: str, line: int, markup: str) -> list[RawReference]:
    detector = _RawHtmlNavigationDetector()
    try:
        detector.feed(markup)
        detector.close()
    except Exception as error:
        raise GovernanceRouteError(f"{source}:{line}: raw HTML token could not be inspected safely") from error
    return [RawReference(source, line, "raw-html-navigation", destination) for destination in detector.destinations]


def _token_line(token) -> int:
    mapping = getattr(token, "map", None)
    return mapping[0] + 1 if mapping and mapping[0] >= 0 else 1


def markdown_references(source: str, text: str) -> list[RawReference]:
    """Extract actual navigable references from vendored CommonMark tokens only."""
    parser = _load_vendored_commonmark_parser()
    try:
        tokens = parser.parse(text)
    except Exception as error:
        raise GovernanceRouteError(f"{source}: vendored CommonMark parser failed") from error
    references: list[RawReference] = []
    for token in tokens:
        line = _token_line(token)
        if token.type == "html_block":
            references.extend(_raw_html_navigation_references(source, line, token.content))
            continue
        if token.type != "inline":
            continue
        for child in token.children or ():
            if child.type == "link_open":
                destination = child.attrGet("href")
                if destination is None:
                    raise GovernanceRouteError(f"{source}:{line}: CommonMark link token lacks href")
                references.append(RawReference(source, line, "markdown-link", destination))
            elif child.type == "html_inline":
                references.extend(_raw_html_navigation_references(source, line, child.content))
            elif child.type == "code_inline":
                for match in DIRECT_GOVERNANCE_PATH.finditer(f"`{child.content}`"):
                    references.append(
                        RawReference(source, line, "direct-governance", match.group("destination"))
                    )
    return references


def split_suffix(destination: str) -> str:
    positions = [position for marker in ("#", "?") if (position := destination.find(marker)) >= 0]
    return destination[: min(positions)] if positions else destination


def source_directory(source: str) -> list[str]:
    return source.split("/")[:-1]


def is_repository_root_target(destination: str) -> bool:
    return destination == "AGENTS.md" or destination.startswith("governance/")


def canonical_repository_destination(source: str, raw_destination: str) -> str | None:
    """Resolve a local governance destination using Git/POSIX path semantics.

    ``None`` denotes a permitted external HTTP(S) URL.  All local aliases are
    either reduced to a single slash-separated repository identity or rejected.
    """
    destination = raw_destination.strip()
    if destination.startswith("<") and destination.endswith(">"):
        destination = destination[1:-1]
    if not destination:
        raise GovernanceRouteError("empty local destination")
    if HTTP_URL.fullmatch(destination):
        return None
    if destination.startswith("/") or destination.startswith("//"):
        raise GovernanceRouteError("absolute filesystem or network-path destination")
    if URI_SCHEME.match(destination):
        raise GovernanceRouteError("unsupported non-HTTP(S) URI destination")
    if "\\" in destination:
        raise GovernanceRouteError("backslash repository path")
    if "%" in destination:
        raise GovernanceRouteError("percent-encoded or ambiguous local destination")
    if any(ord(character) < 32 for character in destination):
        raise GovernanceRouteError("control character in local destination")

    path_part = split_suffix(destination)
    # A fragment-only reference stays within the active source file.
    if not path_part:
        return canonical_registry_path(source)
    if path_part.startswith("/"):
        raise GovernanceRouteError("absolute filesystem destination")
    raw_parts = path_part.split("/")
    if any(part == "" for part in raw_parts):
        raise GovernanceRouteError("ambiguous empty repository path segment")
    output = [] if is_repository_root_target(path_part) else source_directory(source)
    for part in raw_parts:
        if part == ".":
            continue
        if part == "..":
            if not output:
                raise GovernanceRouteError("repository-root traversal")
            output.pop()
            continue
        output.append(part)
    if not output:
        raise GovernanceRouteError("destination resolves to repository root")
    return "/".join(output)


def classify_target(target: str | None, active: set[str], superseded: set[str], evidence: set[str]) -> str:
    if target is None:
        return "EXTERNAL_HTTP"
    if target in active:
        return "ACTIVE"
    if target in superseded:
        return "HISTORICAL_REFERENCE"
    if target in evidence:
        return "HISTORICAL_EVIDENCE"
    return "UNCLASSIFIED"


def audit_active_governance_references(root: Path) -> tuple[ResolvedReference, ...]:
    active, superseded, evidence = registry(root)
    active_set, superseded_set, evidence_set = set(active), set(superseded), set(evidence)
    report: list[ResolvedReference] = []
    for source in active:
        text = read(root, PurePosixPath(source))
        for raw in markdown_references(source, text):
            if raw.form == "raw-html-navigation":
                report.append(
                    ResolvedReference(
                        raw.source,
                        raw.line,
                        raw.form,
                        raw.destination,
                        None,
                        "REJECTED",
                        False,
                        "raw HTML navigation is forbidden",
                    )
                )
                continue
            try:
                target = canonical_repository_destination(raw.source, raw.destination)
            except GovernanceRouteError as error:
                report.append(
                    ResolvedReference(raw.source, raw.line, raw.form, raw.destination, None, "REJECTED", False, str(error))
                )
                continue
            classification = classify_target(target, active_set, superseded_set, evidence_set)
            if classification == "EXTERNAL_HTTP":
                report.append(ResolvedReference(raw.source, raw.line, raw.form, raw.destination, None, classification, True, "external HTTP(S) documentation"))
            elif classification == "ACTIVE":
                report.append(ResolvedReference(raw.source, raw.line, raw.form, raw.destination, target, classification, True, "active governance target"))
            elif classification.startswith("HISTORICAL"):
                report.append(ResolvedReference(raw.source, raw.line, raw.form, raw.destination, target, classification, False, "active executable route resolves to historical target"))
            else:
                report.append(ResolvedReference(raw.source, raw.line, raw.form, raw.destination, target, classification, False, "unclassified internal executable governance target"))
    return tuple(report)


def audit_summary(audit: Iterable[ResolvedReference], structured_provenance_count: int) -> dict[str, int]:
    """Count parser-derived routes and their independently applied policy decisions."""
    routes = tuple(audit)
    markdown_links = tuple(item for item in routes if item.form == "markdown-link")
    return {
        "parsed_navigable_markdown_links": len(markdown_links),
        "parsed_local_markdown_links": sum(item.canonical_target is not None for item in markdown_links),
        "parsed_external_markdown_links": sum(item.classification == "EXTERNAL_HTTP" for item in markdown_links),
        "direct_governance_code_references": sum(item.form == "direct-governance" for item in routes),
        "allowed_active_routes": sum(item.classification == "ACTIVE" and item.allowed for item in routes),
        "rejected_historical_routes": sum(
            item.classification.startswith("HISTORICAL") and not item.allowed for item in routes
        ),
        "rejected_unclassified_or_unsafe_routes": sum(
            not item.allowed and item.classification in {"UNCLASSIFIED", "REJECTED"} for item in routes
        ),
        "raw_html_navigation_rejections": sum(
            item.form == "raw-html-navigation" and item.classification == "REJECTED" and not item.allowed
            for item in routes
        ),
        "structured_provenance_records": structured_provenance_count,
    }


def legacy_governance_paths(root: Path) -> set[str]:
    paths: set[str] = set()
    for path in (root / "governance").rglob("*"):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if any(token in text.lower() for token in LEGACY_TOKENS):
            paths.add(path.relative_to(root).as_posix())
    return paths


def active_execution_lines(root: Path, active: Iterable[str]) -> list[str]:
    failures: list[str] = []
    for relative in active:
        text = read(root, PurePosixPath(relative))
        for number, line in enumerate(text.splitlines(), start=1):
            normalized = line.lower()
            if not any(token in normalized for token in LEGACY_TOKENS):
                continue
            if DIRECTIVE.search(line) and not NEUTRALIZERS.search(line):
                failures.append(f"{relative}:{number}: {line.strip()}")
    return failures


def assert_governance_semantics(root: Path) -> tuple[ResolvedReference, ...]:
    active, superseded, evidence = registry(root)
    historical = set(superseded) | set(evidence)
    provenance = structured_provenance_references(root)

    if not active:
        raise GovernanceRouteError("registry must declare active entrypoints")
    if not superseded:
        raise GovernanceRouteError("registry must retain superseded operational provenance")
    if set(active) & historical:
        raise GovernanceRouteError("a historical path cannot be active")
    for reference in provenance:
        if reference.source not in active:
            raise GovernanceRouteError(
                f"structured provenance source is not an active registry path: {reference.source}"
            )
        if reference.historical_target not in historical:
            raise GovernanceRouteError(
                f"structured provenance target is not a classified historical path: {reference.historical_target}"
            )
        if reference.relationship != "provenance":
            raise GovernanceRouteError("structured provenance relationship must be provenance")

    expected_active = {
        "AGENTS.md",
        PROJECT_STATE.as_posix(),
        PROJECT_PROJECTION.as_posix(),
        REGISTRY.as_posix(),
        PHASES.as_posix(),
        PHASE_DOCUMENT.as_posix(),
        ROUTER.as_posix(),
    }
    if not expected_active <= set(active):
        raise GovernanceRouteError("current routing model is incomplete")

    for relative in superseded:
        banner = read(root, PurePosixPath(relative)).splitlines()[:4]
        if banner != ["# HISTORICAL / SUPERSEDED", "", "**NOT AN ACTIVE ENTRYPOINT — DO NOT EXECUTE.**", ""]:
            raise GovernanceRouteError(f"superseded operational document lacks a durable banner: {relative}")

    classified = set(active) | historical
    unclassified = legacy_governance_paths(root) - classified
    if unclassified:
        raise GovernanceRouteError(f"every obsolete governance occurrence must be classified: {sorted(unclassified)}")
    execution_lines = active_execution_lines(root, active)
    if execution_lines:
        raise GovernanceRouteError("active governance must not direct a superseded Bootstrap operation: " + "; ".join(execution_lines))

    audit = audit_active_governance_references(root)
    historical_allowed = [
        item for item in audit if item.classification.startswith("HISTORICAL") and item.allowed
    ]
    if historical_allowed:
        first = historical_allowed[0]
        raise GovernanceRouteError(
            f"{first.source}:{first.line}: historical navigation was incorrectly allowed"
        )
    rejected = [item for item in audit if not item.allowed]
    if rejected:
        first = rejected[0]
        raise GovernanceRouteError(
            f"{first.source}:{first.line}: rejected {first.form} destination {first.raw_destination!r}: {first.reason}"
        )

    state = read(root, PROJECT_STATE)
    projection = read(root, PROJECT_PROJECTION)
    for document in (state, projection):
        require_solo_owner_hosting_authority(document)
        if scalar(document, "repositories_bootstrapped") != "true":
            raise GovernanceRouteError("repositories_bootstrapped must remain true")
        for expected in (
            "status: INDEPENDENT_REVIEW_PENDING",
            "PHASE-000: NOT_COMPLETED",
            "GATE-000: NOT_PASSED",
            "phase_001: NOT_AUTHORIZED",
            "finding: F-000-04",
            "status: QUARANTINED",
            "authorization: FORBIDDEN",
            "current_boundary: NORMAL_PR_AND_MANUAL_AUTHORITY_FLOW",
        ):
            if expected not in document:
                raise GovernanceRouteError(f"project state misses {expected}")
        if "github_mutation_allowed: false" in document:
            raise GovernanceRouteError("superseded global GitHub-mutation prohibition reintroduced")
    if state != projection:
        raise GovernanceRouteError("PROJECT_STATE and machine projection diverged")

    allowed_phase_statuses = set(list_value(read(root, PHASE_STATUS_SCHEMA), "allowed_phase_status"))
    machine_phase_status = phase_status(read(root, PHASES), "PHASE-000")
    index_phase_status = phase_status(read(root, PHASE_INDEX_YAML), "PHASE-000")
    phase_document = read(root, PHASE_DOCUMENT)
    if "## STATUS\n`IN_PROGRESS`" not in phase_document:
        raise GovernanceRouteError("PHASE-000 document status is not IN_PROGRESS")
    if machine_phase_status != "IN_PROGRESS" or machine_phase_status != index_phase_status:
        raise GovernanceRouteError(
            "PHASE-000 catalog status diverged or regressed: "
            f"machine={machine_phase_status}, index={index_phase_status}"
        )
    if "`IN_PROGRESS`" not in read(root, PHASE_INDEX_MD).splitlines()[4]:
        raise GovernanceRouteError("PHASE-000 Markdown index diverged")
    if machine_phase_status not in allowed_phase_statuses or machine_phase_status == "NOT_STARTED":
        raise GovernanceRouteError("PHASE-000 status is invalid or regressed to NOT_STARTED")
    for expected in (
        "CONTROLLED_INITIAL_BASELINE_BOOTSTRAP",
        "`SUPERSEDED`",
        "`QUARANTINED`",
        "PHASE-000 is `NOT_COMPLETED`",
        "GATE-000 is `NOT_PASSED`",
        "PHASE-001 is\n`NOT_AUTHORIZED`",
    ):
        if expected not in phase_document:
            raise GovernanceRouteError(f"PHASE-000 document misses {expected}")

    router = read(root, ROUTER)
    for required in (
        "AGENTS.md",
        "PROJECT_STATE.yaml",
        "governance-entrypoints.yaml",
        "next_required_action",
        "historical_superseded",
        "Codex Verification Contract",
        "materialize-repositories.py --apply",
        "quarantined",
        "NOT an active",
    ):
        if required not in router:
            raise GovernanceRouteError(f"router misses {required}")
    return audit


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--audit", action="store_true", help="print the canonical active-reference audit")
    args = parser.parse_args()
    try:
        audit = assert_governance_semantics(args.repo_root.resolve())
    except GovernanceRouteError as error:
        print(f"ACTIVE_GOVERNANCE_REJECTED: {error}")
        return 2
    if args.audit:
        print("reference kind\tsource\tline\tform\traw destination\tcanonical target\tclassification\tdecision")
        for item in audit:
            target = item.canonical_target if item.canonical_target is not None else "-"
            decision = "ALLOWED: " if item.allowed else "REJECTED: "
            kind = "EXTERNAL_REFERENCE" if item.classification == "EXTERNAL_HTTP" else "NAVIGABLE_REFERENCE"
            print("\t".join((kind, item.source, str(item.line), item.form, item.raw_destination, target, item.classification, decision + item.reason)))
        provenance = structured_provenance_references(args.repo_root.resolve())
        for reference in provenance:
            print("\t".join((
                "STRUCTURED_PROVENANCE",
                reference.source,
                str(reference.line),
                "metadata",
                reference.historical_target,
                reference.historical_target,
                "STRUCTURED_PROVENANCE",
                "METADATA_ONLY: no navigation authorization",
            )))
        summary = audit_summary(audit, len(provenance))
        print(
            "AUDIT_SUMMARY\t"
            + "\t".join(f"{name}={value}" for name, value in summary.items())
        )
    else:
        print("ACTIVE_GOVERNANCE_SEMANTICS=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
