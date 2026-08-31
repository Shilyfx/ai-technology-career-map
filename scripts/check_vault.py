#!/usr/bin/env python3
"""Dependency-free structural checks for this Obsidian vault."""

from __future__ import annotations

import datetime as dt
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = {
    "seed_warn_days": 90,
    "required_dates": ("created", "updated"),
}
STATUS = {"seed", "developing", "validated", "reference", "deprecated"}
STABILITY = {"stable", "current", "emerging"}
DEPTH = {"recognize", "explain", "use", "implement", "optimize", "research"}
SOURCE_KINDS = {
    "official-job-posting",
    "official-career-page",
    "official-role-description",
    "secondary-source",
}
TYPES = {
    "home",
    "moc",
    "path",
    "concept",
    "assessment",
    "radar",
    "role",
    "matrix",
    "source-index",
    "source",
    "snapshot",
    "inbox",
    "job-sample",
    "skill",
    "evidence",
    "lab",
    "project",
    "review",
    "system",
    "term",
}
DATE_KEYS = {"created", "updated", "review_after", "snapshot_date", "retrieved", "published"}
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SECRET = re.compile(r"(?:sk-[A-Za-z0-9]{20,}|gh[pousr]_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16})")
SECRET_SUFFIXES = {".md", ".canvas", ".json", ".yaml", ".yml"}
FORMAL_EXEMPT = {"README.md", "AGENTS.md"}
APPLIED_BATCH = "enterprise-applied-ai-2026-08"
EVIDENCE_TYPES = {"required", "preferred", "responsibility", "inferred-prerequisite"}
EVIDENCE_STRENGTHS = {"explicit", "inferred"}
CONFIDENCE = {"high", "medium", "low"}
SOURCE_FIDELITY = {"direct", "close-paraphrase", "inferred"}
SOURCE_ACCESS = {"full", "partial", "dynamic-partial", "page-shell-only", "blocked"}
AUDIT_STATUS = {"verified", "partial", "historical"}


def scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_list(value: str) -> list[str]:
    """Parse the small list forms used by this vault without PyYAML."""
    items = [item.strip() for item in value.splitlines() if item.strip()]
    if len(items) == 1 and items[0].startswith("[") and items[0].endswith("]"):
        inner = items[0][1:-1].strip()
        items = [item.strip() for item in inner.split(",") if item.strip()] if inner else []
    return [scalar(item.strip().rstrip(",")) for item in items if scalar(item.strip().rstrip(","))]


def read_note(path: Path) -> tuple[dict[str, str], str, bool]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text, False
    end = text.find("\n---", 4)
    if end < 0:
        return {}, text, False
    raw = text[4:end]
    meta: dict[str, str] = {}
    current_list_key = ""
    for line in raw.splitlines():
        if line.startswith("  - ") and current_list_key:
            # Keep lists searchable without needing a YAML dependency.
            meta[current_list_key] += "\n" + scalar(line[4:])
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", line)
        if not match:
            continue
        key, value = match.group(1), scalar(match.group(2) or "")
        meta[key] = value
        current_list_key = key if not value else ""
    return meta, text[end + 4 :], True


def date_value(value: str) -> dt.date | None:
    try:
        return dt.date.fromisoformat(value)
    except (TypeError, ValueError):
        return None


def note_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)


def scan_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if path.is_dir() or ".git" in path.parts:
            continue
        if path.suffix.lower() in SECRET_SUFFIXES or ".obsidian" in path.parts:
            files.append(path)
    return sorted(files)


def resolve_target(raw_target: str, stem_map: dict[str, list[Path]]) -> list[Path]:
    target = raw_target.strip().replace("\\", "/")
    target_path = Path(target[:-3] if target.endswith(".md") else target)
    direct = ROOT / str(target_path)
    if direct.exists():
        return [direct]
    md_direct = ROOT / (str(target_path) + ".md")
    if md_direct.exists():
        return [md_direct]
    # A path-qualified target must resolve exactly; basename fallback would
    # hide stale paths after a directory migration.
    if "/" in target:
        return []
    candidates = stem_map.get(target_path.name.casefold(), [])
    if candidates:
        return candidates
    normalized = re.sub(r"\s+", "-", target_path.name).casefold()
    return stem_map.get(normalized, [])


def check_wikilinks(
    source: Path,
    text: str,
    stem_map: dict[str, list[Path]],
    incoming: defaultdict[Path, int],
    errors: list[str],
    context: str = "",
) -> None:
    for raw_target in WIKILINK.findall(text):
        candidates = resolve_target(raw_target, stem_map)
        suffix = f" ({context})" if context else ""
        if not candidates:
            errors.append(f"broken wikilink in {source.relative_to(ROOT)}{suffix}: [[{raw_target}]]")
        elif len(candidates) == 1:
            incoming[candidates[0]] += 1


def heading_present(body: str, heading: str) -> bool:
    return bool(re.search(rf"(?mi)^#+\s+{re.escape(heading)}(?:\s|：|:|$)", body))


def section_body(body: str, heading: str) -> str:
    match = re.search(rf"(?ms)^##\s+{re.escape(heading)}\s*$\n(.*?)(?=^##\s+|\Z)", body)
    return match.group(1).strip() if match else ""


def parse_skill_extraction_table(body: str) -> tuple[list[dict[str, str]], str | None]:
    """Parse only the explicit Skill Extraction table, never arbitrary wikilinks."""
    section = section_body(body, "Skill Extraction")
    lines = section.splitlines()
    header_index = next((i for i, line in enumerate(lines) if line.lstrip().startswith("|") and ("Evidence Type" in line and ("Skill" in line or "Normalized Skill" in line))), None)
    if header_index is None:
        return [], "missing Skill Extraction evidence table"
    headers = [cell.strip() for cell in lines[header_index].strip().strip("|").split("|")]
    normalized = {h.casefold(): i for i, h in enumerate(headers)}
    needed = ("evidence type", "requirement strength", "confidence")
    if any(key not in normalized for key in needed):
        return [], "Skill Extraction table missing Evidence Type/Requirement Strength/Confidence"
    skill_key = "skill" if "skill" in normalized else "normalized skill"
    rows: list[dict[str, str]] = []
    for line in lines[header_index + 1:]:
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != len(headers) or all(set(cell) <= {"-", ":", " "} for cell in cells):
            continue
        row = {h.casefold(): cells[i] for h, i in normalized.items()}
        row["skill"] = row.get(skill_key, "")
        row["raw"] = row.get("raw evidence", row.get("raw requirement / responsibility", ""))
        rows.append(row)
    return rows, None


def parse_evidence_traces(body: str) -> dict[int, dict[str, str]]:
    """Parse numbered Evidence Trace blocks for strict Batch B checks."""
    section = section_body(body, "Evidence Trace")
    blocks = re.split(r"(?m)^###\s+Evidence\s+(\d+)\s*$", section)
    traces: dict[int, dict[str, str]] = {}
    for i in range(1, len(blocks), 2):
        try:
            number = int(blocks[i])
        except ValueError:
            continue
        block = blocks[i + 1]
        fields: dict[str, str] = {}
        for line in block.splitlines():
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            fields[key.strip().casefold()] = value.strip().strip("`")
        traces[number] = fields
    return traces


def derive_skill_evidence_counts(applied_rows: dict[Path, list[dict[str, str]]]) -> dict[str, Counter]:
    counts: dict[str, Counter] = defaultdict(Counter)
    for rows in applied_rows.values():
        for row in rows:
            skills = WIKILINK.findall(row.get("skill", ""))
            for skill in skills:
                counts[skill.casefold()][row.get("evidence type", "").strip()] += 1
    return counts


def similarity(a: str, b: str) -> float:
    words_a = set(re.findall(r"[a-z0-9\u4e00-\u9fff]+", a.casefold()))
    words_b = set(re.findall(r"[a-z0-9\u4e00-\u9fff]+", b.casefold()))
    if not words_a or not words_b:
        return 0.0
    return len(words_a & words_b) / max(1, min(len(words_a), len(words_b)))


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    review_due = 0
    notes = note_files()
    records: dict[Path, tuple[dict[str, str], str, bool]] = {}
    stem_map: defaultdict[str, list[Path]] = defaultdict(list)

    for path in notes:
        meta, body, has_frontmatter = read_note(path)
        records[path] = (meta, body, has_frontmatter)
        stem_map[path.stem.casefold()].append(path)

    for paths in stem_map.values():
        if len(paths) > 1:
            errors.append("duplicate note name: " + ", ".join(str(p.relative_to(ROOT)) for p in paths))

    job_sample_skill_evidence: defaultdict[str, set[Path]] = defaultdict(set)
    applied_rows: dict[Path, list[dict[str, str]]] = {}
    for path, (meta, body, _) in records.items():
        if meta.get("type") != "job-sample":
            continue
        if meta.get("sample_batch") == APPLIED_BATCH:
            rows, parse_error = parse_skill_extraction_table(body)
            if parse_error:
                # The detailed error is emitted in the per-sample block below.
                applied_rows[path] = []
            else:
                applied_rows[path] = rows
            for row in rows:
                for raw_skill in WIKILINK.findall(row.get("skill", "")):
                    job_sample_skill_evidence[raw_skill.casefold()].add(path)
        else:
            # Legacy Batch A keeps its historical schema; only the controlled
            # extraction section is used to establish Job Sample evidence.
            section = section_body(body, "Skill Extraction")
            for raw_skill in WIKILINK.findall(section):
                job_sample_skill_evidence[raw_skill.casefold()].add(path)

    source_urls: defaultdict[str, list[Path]] = defaultdict(list)
    for path, (meta, _, _) in records.items():
        if meta.get("type") == "job-sample" and meta.get("source_url"):
            source_urls[meta["source_url"].strip()].append(path)
    for source_url, paths in source_urls.items():
        if len(paths) > 1:
            errors.append(
                "duplicate job-sample source_url " + source_url + ": "
                + ", ".join(str(path.relative_to(ROOT)) for path in paths)
            )

    alias_map: defaultdict[str, set[Path]] = defaultdict(set)
    for path, (meta, _, has_frontmatter) in records.items():
        rel = path.relative_to(ROOT).as_posix()
        if not has_frontmatter or rel in FORMAL_EXEMPT or rel.startswith("99-Templates/"):
            continue
        for alias in parse_list(meta.get("aliases", "")):
            alias_key = alias.casefold()
            alias_map[alias_key].add(path)
            other_stems = [candidate for candidate in stem_map.get(alias_key, []) if candidate != path]
            if other_stems:
                warnings.append(
                    f"alias conflicts with note stem '{alias}': {rel} -> "
                    + ", ".join(str(candidate.relative_to(ROOT)) for candidate in other_stems)
                )
    for alias, paths in alias_map.items():
        if len(paths) > 1:
            warnings.append(
                f"ambiguous alias '{alias}': "
                + ", ".join(str(path.relative_to(ROOT)) for path in sorted(paths))
            )

    for path, (meta, body, has_frontmatter) in records.items():
        rel = path.relative_to(ROOT).as_posix()
        is_template = rel.startswith("99-Templates/")
        if rel in FORMAL_EXEMPT:
            if rel == "README.md" and "[[" in body:
                errors.append("README must use standard Markdown links, not wikilinks")
            continue
        if not has_frontmatter:
            errors.append(f"missing frontmatter: {rel}")
            continue
        kind = meta.get("type", "")
        if kind not in TYPES:
            errors.append(f"invalid or missing type in {rel}: {kind or '<empty>'}")
        status = meta.get("status", "")
        if status not in STATUS:
            errors.append(f"invalid status in {rel}: {status or '<empty>'}")
        stability = meta.get("stability", "")
        if stability and stability not in STABILITY:
            errors.append(f"invalid stability in {rel}: {stability}")
        depth = meta.get("depth", "")
        if depth and depth not in DEPTH:
            errors.append(f"invalid depth in {rel}: {depth}")
        if not is_template:
            for key in CONFIG["required_dates"]:
                if not meta.get(key):
                    errors.append(f"missing {key} in {rel}")
        for key in DATE_KEYS:
            if meta.get(key) and date_value(meta[key]) is None:
                errors.append(f"invalid date {key} in {rel}: {meta[key]}")
        if kind in {"radar", "snapshot"} and not meta.get("snapshot_date"):
            errors.append(f"missing snapshot_date in {rel}")
        if not is_template and (
            kind in {"radar", "snapshot"} or stability in {"current", "emerging"} or kind == "role"
        ):
            if not meta.get("review_after"):
                errors.append(f"missing review_after for time-sensitive page: {rel}")
        if not is_template and meta.get("review_after"):
            review_date = date_value(meta["review_after"])
            if review_date and review_date <= dt.date.today():
                review_due += 1
                warnings.append(f"review due: {rel} (review_after {meta['review_after']})")
        if status == "seed" and not is_template and meta.get("created"):
            created = date_value(meta["created"])
            if created and (dt.date.today() - created).days > CONFIG["seed_warn_days"]:
                warnings.append(f"old seed note: {rel}")
        if kind == "concept" and not is_template:
            text = re.sub(r"```.*?```", "", body, flags=re.S)
            text = re.sub(r"[#|`*_\-]", "", text)
            if len(re.sub(r"\s+", "", text)) < 240:
                warnings.append(f"near-empty concept: {rel}")

        page_kind = meta.get("page_kind", "")
        if page_kind == "current-state":
            if kind != "home":
                errors.append(f"current-state must have type home: {rel}")
            for key in ("current", "next"):
                if not meta.get(key):
                    errors.append(f"current-state missing {key}: {rel}")
            if meta.get("current") and meta.get("current") == meta.get("next"):
                errors.append(f"current-state current equals next: {rel}")
        elif page_kind == "technology-radar":
            if kind != "radar":
                errors.append(f"technology-radar must have type radar: {rel}")
            for key in ("snapshot_date", "review_after"):
                if not meta.get(key):
                    errors.append(f"technology-radar missing {key}: {rel}")
            for band in ("Core", "Build", "Deepen", "Watch", "Avoid"):
                if not heading_present(body, band):
                    errors.append(f"technology-radar missing {band} section: {rel}")
        elif page_kind == "term-radar":
            if kind != "radar":
                errors.append(f"term-radar must have type radar: {rel}")
            for key in ("snapshot_date", "review_after"):
                if not meta.get(key):
                    errors.append(f"term-radar missing {key}: {rel}")
        elif page_kind == "evidence-index":
            if kind != "moc" or meta.get("domain") != "evidence":
                errors.append(f"evidence-index must be type moc with domain evidence: {rel}")
        elif page_kind == "job-sample-index":
            if kind != "moc" or meta.get("domain") != "jobs":
                errors.append(f"job-sample-index must be type moc with domain jobs: {rel}")
        elif page_kind == "job-inbox":
            if kind != "inbox":
                errors.append(f"job-inbox must have type inbox: {rel}")
        elif page_kind == "skill-index":
            if kind != "moc" or meta.get("domain") != "skills":
                errors.append(f"skill-index must be type moc with domain skills: {rel}")
        elif page_kind == "role-skill-assessment":
            if kind != "assessment":
                errors.append(f"role-skill-assessment must have type assessment: {rel}")
        elif page_kind == "imported-source":
            if kind != "source":
                errors.append(f"imported-source must have type source: {rel}")
            for key in ("title", "article_url", "source_url", "source_kind", "retrieved"):
                if not meta.get(key):
                    errors.append(f"imported-source missing {key}: {rel}")

        if kind == "job-sample" and not is_template:
            for key in ("company", "role_title", "role_family", "seniority", "location", "source_url", "source_kind", "source_status", "snapshot_date", "retrieved", "created", "updated", "review_after"):
                if not meta.get(key):
                    errors.append(f"job-sample missing {key}: {rel}")
            if meta.get("source_kind") and meta["source_kind"] not in SOURCE_KINDS:
                errors.append(f"invalid source_kind in {rel}: {meta['source_kind']}")
            for heading in ("Responsibilities", "Explicit Requirements", "Skill Extraction", "Limitations", "Evidence Trace"):
                if not heading_present(body, heading):
                    errors.append(f"job-sample missing {heading}: {rel}")
            for trace_field in ("Source Section:", "Evidence Type:", "Confidence:"):
                if trace_field not in body:
                    errors.append(f"job-sample Evidence Trace missing {trace_field} in {rel}")
            if meta.get("sample_batch") == "enterprise-applied-ai-2026-08":
                for key in ("sample_batch", "company_segment", "role_subtrack", "evidence_audit_status", "source_access"):
                    if not meta.get(key):
                        errors.append(f"applied job-sample missing {key}: {rel}")
                if meta.get("source_access") not in SOURCE_ACCESS:
                    errors.append(f"invalid source_access in {rel}: {meta.get('source_access','')}")
                if meta.get("evidence_audit_status") not in AUDIT_STATUS:
                    errors.append(f"invalid evidence_audit_status in {rel}: {meta.get('evidence_audit_status','')}")
                if meta.get("evidence_audit_status") == "historical" and meta.get("source_status") not in {"expired", "unavailable"}:
                    warnings.append(f"historical audit without expired/unavailable status: {rel}")
                if "market_frequency" in body or "market_frequency" in meta:
                    errors.append(f"applied job-sample must not claim market_frequency: {rel}")
                if re.search(r"(?<!\w)\d+(?:\.\d+)?\s*%", body):
                    warnings.append(f"applied job-sample contains percentage; verify it is not a market-frequency claim: {rel}")
                rows, parse_error = parse_skill_extraction_table(body)
                if parse_error:
                    errors.append(f"applied job-sample {rel}: {parse_error}")
                if not rows:
                    errors.append(f"applied job-sample has no evidence rows: {rel}")
                traces = parse_evidence_traces(body)
                for index, row in enumerate(rows, 1):
                    kind_value = row.get("evidence type", "").strip()
                    strength_value = row.get("requirement strength", "").strip()
                    confidence_value = row.get("confidence", "").strip()
                    if kind_value not in EVIDENCE_TYPES:
                        errors.append(f"invalid Evidence Type in {rel} row {index}: {kind_value}")
                    if strength_value not in EVIDENCE_STRENGTHS:
                        errors.append(f"invalid Requirement Strength in {rel} row {index}: {strength_value}")
                    if confidence_value not in CONFIDENCE:
                        errors.append(f"invalid Confidence in {rel} row {index}: {confidence_value}")
                    if not WIKILINK.findall(row.get("skill", "")):
                        errors.append(f"Skill Extraction row has no mapped wikilink in {rel} row {index}")
                    if not row.get("raw", "").strip():
                        errors.append(f"Skill Extraction row has no Raw Evidence in {rel} row {index}")
                    if kind_value == "inferred-prerequisite" and strength_value != "inferred":
                        errors.append(f"inferred-prerequisite must have inferred strength in {rel} row {index}")
                    if kind_value in {"required", "preferred", "responsibility"} and strength_value != "explicit":
                        errors.append(f"explicit evidence type must have explicit strength in {rel} row {index}")
                    trace = traces.get(index, {})
                    fidelity = trace.get("source fidelity", "")
                    if fidelity not in SOURCE_FIDELITY:
                        errors.append(f"invalid/missing Source Fidelity in {rel} row {index}: {fidelity}")
                    if kind_value == "inferred-prerequisite" and fidelity == "direct":
                        errors.append(f"inferred-prerequisite cannot use direct Source Fidelity in {rel} row {index}")
                    if not trace.get("mapping rationale", "").strip():
                        errors.append(f"missing semantic Mapping Rationale in {rel} row {index}")
                    source_section = trace.get("source section", "").casefold()
                    if kind_value in {"required", "preferred"} and "responsibil" in source_section:
                        errors.append(f"{kind_value} evidence cannot come from Responsibilities in {rel} row {index}")
                    if kind_value == "required" and any(token in source_section for token in ("historical", "page shell", "redirected", "unavailable")):
                        errors.append(f"required evidence cannot come from historical/unavailable section in {rel} row {index}")
                    access = meta.get("source_access", "").casefold()
                    if access in {"partial", "blocked", "page-shell-only"}:
                        if confidence_value == "high":
                            warnings.append(f"partial/blocked source with high confidence in {rel} row {index}")
                        if kind_value in {"required", "preferred"}:
                            errors.append(f"partial/blocked source cannot support required/preferred evidence in {rel} row {index}")
                    if meta.get("evidence_audit_status") == "historical" and kind_value in {"required", "preferred"}:
                        errors.append(f"historical audit cannot have required/preferred evidence in {rel} row {index}")
                    if access == "dynamic-partial" and confidence_value == "high":
                        warnings.append(f"dynamic source with high confidence in {rel} row {index}")
                    raw_lower = row.get("raw", "").casefold()
                    alt = row.get("alternative group", "").strip().casefold()
                    if re.search(r"\b(or|one of|at least one)\b", raw_lower) and not alt:
                        warnings.append(f"one-of wording without Alternative Group in {rel} row {index}")
                    skill_lower = row.get("skill", "").casefold()
                    eval_terms = re.search(r"\b(eval|evaluation|quality|trajectory|benchmark|judge|regression)\b", raw_lower)
                    if re.search(r"\b(observability|monitoring|metrics|tracing|latency|reliability)\b", raw_lower) and "agent-evals-and-trace-debugging" in skill_lower and not eval_terms:
                        warnings.append(f"observability signal mapped to Agent Evals without eval term in {rel} row {index}")
                    if "debug" in raw_lower and "agent-evals-and-trace-debugging" in skill_lower and not eval_terms:
                        warnings.append(f"debugging signal mapped to Agent Evals without eval term in {rel} row {index}")
                    if re.search(r"\b(mcp|a2a)\b", raw_lower) and "tool-calling-and-action-contracts" in skill_lower and not re.search(r"\b(tool|action|execution)\b", raw_lower):
                        warnings.append(f"MCP/A2A signal mapped to Tool Calling without action term in {rel} row {index}")
                    if re.search(r"\b(rag|retrieval|grounding)\b", raw_lower) and kind_value == "inferred-prerequisite" and "preferred" in trace.get("source section", "").casefold():
                        warnings.append(f"explicit preferred retrieval downgraded to inferred in {rel} row {index}")
                groups = defaultdict(list)
                for index, row in enumerate(rows, 1):
                    group = row.get("alternative group", "").strip()
                    if group and group not in {"—", "-", "none"}:
                        groups[group].append((index, row))
                # A non-empty group preserves an explicit one-of or at-least-N
                # relation. Some alternatives (for example Go) have no
                # dedicated vault Skill, so one mapped member is valid when
                # Raw Evidence and Notes retain the full set.
                trace_count = len(re.findall(r"(?mi)^###\s+Evidence\s+\d+", body))
                if trace_count != len(rows):
                    errors.append(f"Evidence Trace count {trace_count} != table rows {len(rows)} in {rel}")
                for index in range(1, len(rows) + 1):
                    trace = traces.get(index, {})
                    for trace_field in ("source section", "source fidelity", "raw evidence", "mapped skill", "evidence type", "requirement strength", "alternative group", "depth signal", "confidence", "mapping rationale", "notes"):
                        if not trace.get(trace_field, "").strip():
                            errors.append(f"applied Evidence Trace missing {trace_field} in {rel} evidence {index}")
                    if trace.get("evidence type", "").strip() != rows[index - 1].get("evidence type", "").strip():
                        errors.append(f"Evidence Trace type mismatch in {rel} evidence {index}")
                trace_notes = [t.get("notes", "") for t in traces.values() if t.get("notes")]
                rationales = [t.get("mapping rationale", "") for t in traces.values() if t.get("mapping rationale")]
                if len(trace_notes) >= 3 and len(set(trace_notes)) == 1:
                    warnings.append(f"generic repeated Notes in {rel}")
                if len(rationales) >= 3 and len(set(rationales)) == 1:
                    warnings.append(f"generic repeated Mapping Rationale in {rel}")
                if meta.get("evidence_audit_status") == "historical" and any(r.get("evidence type") in {"required", "preferred"} for r in rows):
                    errors.append(f"historical sample contains current requirement evidence: {rel}")
                resp = section_body(body, "Responsibilities")
                req = section_body(body, "Explicit Requirements")
                if similarity(resp, req) >= 0.86 and len(resp) > 40 and len(req) > 40:
                    warnings.append(f"possible templated evidence extraction: {rel}")

        if kind == "skill" and not is_template:
            for key in ("skill_category", "roles", "prerequisites"):
                if not meta.get(key) and key != "prerequisites":
                    errors.append(f"skill missing {key}: {rel}")
            for heading in ("为什么岗位需要它", "Role Demand", "Job Evidence", "前置 Skills", "Practice", "Pass Evidence", "常见失败", "Related Knowledge"):
                if not heading_present(body, heading):
                    errors.append(f"skill missing {heading}: {rel}")
            if not meta.get("roles"):
                warnings.append(f"skill has no role: {rel}")
            if not job_sample_skill_evidence.get(path.stem.casefold()) and meta.get("evidence_mode") != "prerequisite-synthesis":
                warnings.append(f"skill has no Job Sample evidence: {rel}")

        if kind == "role" and not is_template:
            for heading in ("Skill Profile", "Portfolio Evidence", "Source Limitations"):
                if not heading_present(body, heading):
                    errors.append(f"role missing {heading}: {rel}")
            if not heading_present(body, "Sample Basis") and not heading_present(body, "Evidence Basis"):
                warnings.append(f"role missing sample basis: {rel}")
            if not meta.get("sample_count"):
                warnings.append(f"role missing sample_count: {rel}")
            elif meta.get("sample_count") == "0":
                warnings.append(f"role sample_count is zero: {rel}")

        if rel == "00-Home/Learning-Path.md" and kind == "path":
            for section in ("Job Samples", "Role Skill Profile", "Prerequisites", "Practice", "Evidence", "Next Skill"):
                if section.lower() not in body.lower():
                    errors.append(f"learning path missing {section}: {rel}")
        if kind in {"evidence", "lab", "project", "review"} and not is_template:
            for section in ("Problem", "Action", "Result", "Failure", "Judgment"):
                if not heading_present(body, section):
                    errors.append(f"{kind} page missing {section}: {rel}")

    # The Applied AI matrix is a derived view, not a hand-written frequency
    # claim.  Recompute counts from the Job Sample tables and cross-check the
    # published rows when the matrix uses the v2 columns.
    derived = derive_skill_evidence_counts(applied_rows)
    matrix_path = ROOT / "04-Skills" / "Skill-Evidence-Matrix.md"
    if matrix_path.exists():
        matrix_text = matrix_path.read_text(encoding="utf-8")
        matrix_lines = matrix_text.splitlines()
        matrix_header = next((line for line in matrix_lines if line.startswith("| Skill | Required Direct | Required One-of | Preferred | Responsibility | Inferred | High/Medium Source N | Low/Historical N | Sample N |")), None)
        if matrix_header:
            matrix_rows: dict[str, list[str]] = {}
            for line in matrix_lines:
                if not line.startswith("| [["):
                    continue
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if len(cells) >= 9:
                    skill_match = WIKILINK.search(cells[0])
                    if skill_match:
                        matrix_rows[skill_match.group(1).casefold()] = cells
            kind_columns = {"required": None, "preferred": 3, "responsibility": 4, "inferred-prerequisite": 5}
            for skill_key, counts in derived.items():
                if skill_key not in matrix_rows:
                    errors.append(f"Skill Evidence Matrix missing derived skill row: {skill_key}")
                    continue
                cells = matrix_rows[skill_key]
                direct = sum(1 for path, rows in applied_rows.items() for row in rows if row.get("skill", "").casefold().find(skill_key) >= 0 and row.get("evidence type") == "required" and row.get("alternative group", "").strip().casefold() in {"", "none", "—", "-"})
                one_of = counts.get("required", 0) - direct
                if cells[1] != str(direct):
                    errors.append(f"Skill Evidence Matrix mismatch {skill_key} required direct: {cells[1]} != {direct}")
                if cells[2] != str(one_of):
                    errors.append(f"Skill Evidence Matrix mismatch {skill_key} required one-of: {cells[2]} != {one_of}")
                for kind_value, column in {"preferred":3, "responsibility":4, "inferred-prerequisite":5}.items():
                    expected = str(counts.get(kind_value, 0))
                    if cells[column] != expected:
                        errors.append(f"Skill Evidence Matrix mismatch {skill_key} {kind_value}: {cells[column]} != {expected}")
                sample_cell = cells[8]
                if sample_cell.isdigit() and int(sample_cell) < 1:
                    errors.append(f"Skill Evidence Matrix Sample N is zero for {skill_key}")

    # Resolve wikilinks in both body and frontmatter metadata.
    incoming: defaultdict[Path, int] = defaultdict(int)
    for path, (meta, body, _) in records.items():
        # Imported external Markdown is preserved as a source artifact. Its
        # body may contain the publisher's own wikilinks, which are not part
        # of this vault's graph; only our controlled frontmatter links are
        # validated below.
        if not (meta.get("type") == "source" and meta.get("page_kind") == "imported-source"):
            check_wikilinks(path, body, stem_map, incoming, errors)
        for field, value in meta.items():
            if "[[" in value:
                check_wikilinks(path, value, stem_map, incoming, errors, f"frontmatter {field}")
        if path.name == "README.md":
            for target in MARKDOWN_LINK.findall(body):
                if target.startswith(("http://", "https://", "#")):
                    continue
                target_path = (path.parent / target.split("#", 1)[0]).resolve()
                if not target_path.exists():
                    errors.append(f"broken README link: {target}")
                else:
                    incoming[target_path] += 1

        # Old monolithic Agent Skill links are allowed only on the migration
        # bridge and index/navigation pages; new evidence should use the split
        # Skills so the graph remains unambiguous.
        if "[[Tool-Calling-Agent-Workflow]]" in body:
            rel = path.relative_to(ROOT).as_posix()
            allowed = {
                "04-Skills/LLM-Applications/Tool-Calling-Agent-Workflow.md",
                "04-Skills/Skill-Index.md",
                "03-Roles/Role-Skill-Matrix.md",
            }
            if rel not in allowed:
                warnings.append(f"legacy Tool-Calling-Agent-Workflow link outside bridge/index: {rel}")

    # Canvas nodes are content-bearing notes too; validate their wikilinks.
    for canvas in sorted(ROOT.rglob("*.canvas")):
        if ".git" in canvas.parts:
            continue
        try:
            canvas_text = canvas.read_text(encoding="utf-8")
        except OSError:
            continue
        check_wikilinks(canvas, canvas_text, stem_map, incoming, errors, "canvas")

    for path in notes:
        rel = path.relative_to(ROOT).as_posix()
        exempt = rel in FORMAL_EXEMPT or rel.startswith("99-Templates/") or rel.startswith("99-System/")
        if not exempt and incoming[path] == 0:
            warnings.append(f"orphan note: {rel}")

    current_pages = [p for p, (m, _, _) in records.items() if m.get("page_kind") == "current-state"]
    if len(current_pages) != 1:
        errors.append(f"expected exactly one current-state page, found {len(current_pages)}")
    else:
        meta = records[current_pages[0]][0]
        if not meta.get("current"):
            errors.append("current-state has no current value")
        if not meta.get("next"):
            errors.append("current-state has no next value")
        if meta.get("current") == meta.get("next"):
            errors.append("current-state current equals next")
    for path, (meta, _, _) in records.items():
        if meta.get("page_kind") != "current-state" and ("current" in meta or "next" in meta):
            errors.append(f"dynamic current/next field outside Current-State: {path.relative_to(ROOT)}")

    evidence_index = ROOT / "06-Evidence" / "Evidence-Index.md"
    if not evidence_index.exists():
        errors.append("missing 06-Evidence/Evidence-Index.md")

    # Detect cycles in Skill prerequisites so the learning graph remains schedulable.
    skill_nodes = {
        path: meta
        for path, (meta, _, _) in records.items()
        if meta.get("type") == "skill" and not path.relative_to(ROOT).as_posix().startswith("99-Templates/")
    }
    skill_edges: dict[Path, set[Path]] = defaultdict(set)
    for path, meta in skill_nodes.items():
        for raw_target in WIKILINK.findall(meta.get("prerequisites", "")):
            candidates = resolve_target(raw_target, stem_map)
            if len(candidates) == 1 and candidates[0] in skill_nodes:
                skill_edges[path].add(candidates[0])
    visiting: set[Path] = set()
    visited: set[Path] = set()

    def visit_skill(node: Path, stack: tuple[Path, ...] = ()) -> None:
        if node in visiting:
            cycle = " -> ".join(p.stem for p in stack + (node,))
            errors.append(f"skill prerequisite cycle: {cycle}")
            return
        if node in visited:
            return
        visiting.add(node)
        for prerequisite in skill_edges.get(node, set()):
            visit_skill(prerequisite, stack + (node,))
        visiting.remove(node)
        visited.add(node)

    for skill in skill_nodes:
        visit_skill(skill)

    for path in scan_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        if SECRET.search(text):
            errors.append(f"possible credential pattern in {path.relative_to(ROOT)}")

    print("Vault QA")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    print(f"Review due: {review_due}")
    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARN: {item}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
