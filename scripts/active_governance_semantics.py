"""Fail-closed semantic checks for active SpanGPU governance routes.

This module intentionally uses only the Python standard library.  It is the
single canonical resolver used by the governance regression tests and its
``--audit`` command; tests must not recreate path-resolution behaviour.

Supported executable reference forms are deliberately narrow and explicit:

* inline Markdown links: ``[label](destination)`` (including ``<destination>``
  and a single-quoted, double-quoted, or parenthesized title),
* explicit, collapsed, or shortcut Markdown reference links with a local definition, and
* backtick-delimited, repository-root-anchored direct governance paths.

All other plausible local link encodings are rejected rather than
reinterpreted.  A historical target is never executable from active
governance.  Structured provenance is independently recorded metadata; it
does not participate in navigation authorization.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path, PurePosixPath
import argparse
import re
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

# The Markdown-governance grammar is parsed below by one deterministic
# cursor-based extractor.  A local destination cannot contain whitespace.
# Titles are parsed explicitly and never become a destination.
DIRECT_GOVERNANCE_PATH = re.compile(
    r"`(?P<destination>AGENTS\.md|governance/[^`\s]+)`"
)
HTTP_URL = re.compile(r"https?://[^\s]+\Z", re.IGNORECASE)
URI_SCHEME = re.compile(r"[A-Za-z][A-Za-z0-9+.-]*:")
LOCAL_PATH_SUFFIXES = (".md", ".yaml", ".yml", ".json")


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


def normalize_reference_label(label: str) -> str:
    return " ".join(label.split()).casefold()


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


class MarkdownSyntaxError(ValueError):
    """The declared Markdown-governance grammar could not consume a construct."""


def skip_horizontal_space(text: str, offset: int) -> int:
    while offset < len(text) and text[offset] in " \t":
        offset += 1
    return offset


def consume_destination(text: str, offset: int, *, inline: bool) -> tuple[str, int]:
    """Consume one declared destination without treating a title as a target."""
    if offset >= len(text) or text[offset] in " \t\n)":
        raise MarkdownSyntaxError("missing destination")
    if text[offset] == "<":
        end = text.find(">", offset + 1)
        if end < 0 or "\n" in text[offset:end] or "<" in text[offset + 1:end]:
            raise MarkdownSyntaxError("unterminated or nested angle destination")
        return text[offset : end + 1], end + 1

    start = offset
    while offset < len(text) and text[offset] not in " \t\n":
        if inline and text[offset] == ")":
            break
        offset += 1
    if start == offset:
        raise MarkdownSyntaxError("missing destination")
    return text[start:offset], offset


def consume_title(text: str, offset: int) -> int:
    """Consume exactly one single-, double-, or parenthesized Markdown title."""
    if offset >= len(text):
        raise MarkdownSyntaxError("missing title")
    opener = text[offset]
    if opener in {"'", '"'}:
        cursor = offset + 1
        escaped = False
        while cursor < len(text):
            character = text[cursor]
            if character == "\n":
                break
            if not escaped and character == opener:
                return cursor + 1
            escaped = character == "\\" and not escaped
            if character != "\\":
                escaped = False
            cursor += 1
        raise MarkdownSyntaxError("unterminated quoted title")
    if opener == "(":
        cursor = offset + 1
        depth = 1
        escaped = False
        while cursor < len(text):
            character = text[cursor]
            if character == "\n":
                break
            if not escaped and character == "(":
                depth += 1
            elif not escaped and character == ")":
                depth -= 1
                if depth == 0:
                    return cursor + 1
            escaped = character == "\\" and not escaped
            if character != "\\":
                escaped = False
            cursor += 1
        raise MarkdownSyntaxError("unterminated parenthesized title")
    raise MarkdownSyntaxError("unsupported title syntax")


def parse_inline_destination(text: str, offset: int) -> tuple[str, int]:
    """Parse ``(destination [title])`` and consume its closing parenthesis."""
    offset = skip_horizontal_space(text, offset)
    destination, offset = consume_destination(text, offset, inline=True)
    after_destination = skip_horizontal_space(text, offset)
    if after_destination < len(text) and text[after_destination] == ")":
        return destination, after_destination + 1
    if after_destination == offset:
        raise MarkdownSyntaxError("destination and title must be separated by horizontal whitespace")
    after_title = skip_horizontal_space(text, consume_title(text, after_destination))
    if after_title >= len(text) or text[after_title] != ")":
        raise MarkdownSyntaxError("unparsed trailing inline-link syntax")
    return destination, after_title + 1


def parse_reference_definition_destination(text: str) -> str:
    """Parse ``destination [title]`` and reject every trailing token."""
    offset = skip_horizontal_space(text, 0)
    destination, offset = consume_destination(text, offset, inline=False)
    after_destination = skip_horizontal_space(text, offset)
    if after_destination == len(text):
        return destination
    if after_destination == offset:
        raise MarkdownSyntaxError("destination and title must be separated by horizontal whitespace")
    after_title = skip_horizontal_space(text, consume_title(text, after_destination))
    if after_title != len(text):
        raise MarkdownSyntaxError("unparsed trailing reference-definition syntax")
    return destination


def looks_like_local_governance_destination(fragment: str) -> bool:
    """Detect only path-shaped local text before choosing the fail-closed branch."""
    for candidate in re.findall(r"<[^>\n]*>|[^\s<>]+", fragment):
        candidate = candidate.strip("<>()[]{}'\".,;:")
        if not candidate or HTTP_URL.fullmatch(candidate) or URI_SCHEME.match(candidate):
            continue
        path_part = split_suffix(candidate)
        if (
            path_part in {"AGENTS.md", "governance"}
            or path_part.startswith(("./", "../", "/", "//", "governance/"))
            or "/" in path_part
            or "\\" in path_part
            or "%" in path_part
            or path_part.endswith(LOCAL_PATH_SUFFIXES)
        ):
            return True
    return False


def fail_closed_if_local_markdown(source: str, text: str, offset: int, detail: str) -> None:
    line_end = text.find("\n", offset)
    fragment = text[offset:] if line_end < 0 else text[offset:line_end]
    if looks_like_local_governance_destination(fragment):
        raise GovernanceRouteError(
            f"{source}:{line_number(text, offset)}: malformed or unsupported local Markdown reference: {detail}"
        )


def reference_definitions(source: str, text: str) -> tuple[dict[str, str], list[tuple[int, int]]]:
    """Parse every declared reference definition before resolving reference uses."""
    definitions: dict[str, str] = {}
    spans: list[tuple[int, int]] = []
    offset = 0
    for line in text.splitlines(keepends=True):
        body = line.rstrip("\r\n")
        indent = len(body) - len(body.lstrip(" \t"))
        if indent <= 3 and body[indent:].startswith("["):
            close = body.find("]", indent + 1)
            if close >= 0 and close + 1 < len(body) and body[close + 1] == ":":
                label_text = body[indent + 1:close]
                value = body[close + 2:]
                try:
                    if not label_text:
                        raise MarkdownSyntaxError("empty reference definition label")
                    destination = parse_reference_definition_destination(value)
                except MarkdownSyntaxError as error:
                    fail_closed_if_local_markdown(source, text, offset + close + 2, str(error))
                else:
                    label = normalize_reference_label(label_text)
                    if label in definitions:
                        raise GovernanceRouteError(
                            f"{source}:{line_number(text, offset)}: duplicate reference definition {label!r}"
                        )
                    definitions[label] = destination
                    spans.append((offset, offset + len(line)))
        offset += len(line)
    return definitions, spans


def inline_or_reference_at(
    source: str,
    text: str,
    offset: int,
    definitions: dict[str, str],
) -> tuple[RawReference, int] | None:
    """Parse one inline, explicit, collapsed, or shortcut reference at ``offset``."""
    if offset and text[offset - 1] == "!":
        return None
    label_end = text.find("]", offset + 1)
    if label_end < 0 or "\n" in text[offset:label_end]:
        return None
    label_text = text[offset + 1:label_end]
    next_offset = label_end + 1
    if next_offset < len(text) and text[next_offset] == "(":
        try:
            destination, end = parse_inline_destination(text, next_offset + 1)
        except MarkdownSyntaxError as error:
            fail_closed_if_local_markdown(source, text, next_offset + 1, str(error))
            return None
        return RawReference(source, line_number(text, offset), "inline", destination), end
    if next_offset < len(text) and text[next_offset] == "[":
        reference_end = text.find("]", next_offset + 1)
        if reference_end < 0 or "\n" in text[next_offset:reference_end]:
            return None
        reference_label = text[next_offset + 1:reference_end] or label_text
        label = normalize_reference_label(reference_label)
        if label not in definitions:
            raise GovernanceRouteError(
                f"{source}:{line_number(text, offset)}: undefined reference label {label!r}"
            )
        return RawReference(source, line_number(text, offset), "reference", definitions[label]), reference_end + 1
    if next_offset < len(text) and text[next_offset] in "[:":
        return None
    label = normalize_reference_label(label_text)
    if label in definitions:
        return RawReference(source, line_number(text, offset), "reference", definitions[label]), next_offset
    return None


def markdown_references(source: str, text: str) -> list[RawReference]:
    """Extract every declared executable Markdown/direct-governance form once."""
    references: list[RawReference] = []
    definitions, definition_spans = reference_definitions(source, text)
    protected_spans = list(definition_spans)

    offset = 0
    while offset < len(text):
        definition = next((span for span in definition_spans if span[0] <= offset < span[1]), None)
        if definition:
            offset = definition[1]
            continue
        if text[offset] != "[":
            offset += 1
            continue
        parsed = inline_or_reference_at(source, text, offset, definitions)
        if parsed is None:
            offset += 1
            continue
        reference, end = parsed
        references.append(reference)
        protected_spans.append((offset, end))
        offset = end

    def inside_protected_span(candidate: int) -> bool:
        return any(start <= candidate < end for start, end in protected_spans)

    for match in DIRECT_GOVERNANCE_PATH.finditer(text):
        if inside_protected_span(match.start()):
            continue
        references.append(
            RawReference(source, line_number(text, match.start()), "direct-governance", match.group("destination"))
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
        for reference in structured_provenance_references(args.repo_root.resolve()):
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
        active_routes = sum(item.classification == "ACTIVE" and item.allowed for item in audit)
        external_routes = sum(item.classification == "EXTERNAL_HTTP" for item in audit)
        allowed_historical = sum(
            item.classification.startswith("HISTORICAL") and item.allowed for item in audit
        )
        unclassified = sum(item.classification == "UNCLASSIFIED" for item in audit)
        # ``markdown_references`` is the only declared Markdown-governance
        # extractor. Every RawReference it emits is appended above or rejected
        # during extraction, so there is no unaudited recognized-route state.
        print(
            "AUDIT_SUMMARY\t"
            f"legitimate_active_routes={active_routes}\t"
            f"external_references={external_routes}\t"
            f"structured_provenance_metadata={len(structured_provenance_references(args.repo_root.resolve()))}\t"
            f"allowed_historical_navigable_routes={allowed_historical}\t"
            f"unclassified_navigable_local_routes={unclassified}\t"
            "ignored_recognized_local_markdown_references=0"
        )
    else:
        print("ACTIVE_GOVERNANCE_SEMANTICS=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
