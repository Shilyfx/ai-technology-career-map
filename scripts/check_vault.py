#!/usr/bin/env python3
"""Dependency-free structural checks for this Obsidian vault."""

from __future__ import annotations

import datetime as dt
import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = {
    "seed_warn_days": 90,
    "required_dates": ("created", "updated"),
}
STATUS = {"seed", "developing", "validated", "reference", "deprecated"}
STABILITY = {"stable", "current", "emerging"}
DEPTH = {"recognize", "explain", "use", "implement", "optimize", "research"}
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
    "snapshot",
    "inbox",
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
    return stem_map.get(target_path.name.casefold(), [])


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

        if rel == "00-Home/Learning-Path.md" and kind == "path":
            for section in ("Goal", "Prerequisites", "Concepts", "Practice", "Pass Evidence", "Next"):
                if section.lower() not in body.lower():
                    errors.append(f"learning path missing {section}: {rel}")
        if kind in {"evidence", "lab", "project", "review"} and not is_template:
            for section in ("Problem", "Action", "Result", "Failure", "Judgment"):
                if not heading_present(body, section):
                    errors.append(f"{kind} page missing {section}: {rel}")

    # Resolve wikilinks in both body and frontmatter metadata.
    incoming: defaultdict[Path, int] = defaultdict(int)
    for path, (meta, body, _) in records.items():
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

    evidence_index = ROOT / "09-Evidence" / "Evidence-Index.md"
    if not evidence_index.exists():
        errors.append("missing 09-Evidence/Evidence-Index.md")

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
