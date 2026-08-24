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


def scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


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


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    notes = sorted(ROOT.rglob("*.md"))
    notes = [p for p in notes if ".git" not in p.parts]
    records: dict[Path, tuple[dict[str, str], str, bool]] = {}
    stem_map: defaultdict[str, list[Path]] = defaultdict(list)

    for path in notes:
        meta, body, has_frontmatter = read_note(path)
        records[path] = (meta, body, has_frontmatter)
        stem_map[path.stem.casefold()].append(path)

    for stem, paths in stem_map.items():
        if len(paths) > 1:
            errors.append("duplicate note name: " + ", ".join(str(p.relative_to(ROOT)) for p in paths))

    formal_exempt = {"README.md", "AGENTS.md"}
    for path, (meta, body, has_frontmatter) in records.items():
        rel = path.relative_to(ROOT).as_posix()
        is_template = rel.startswith("99-Templates/")
        if rel in formal_exempt:
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
        if not is_template and (kind in {"radar", "snapshot"} or stability in {"current", "emerging"} or kind == "role"):
            if not meta.get("review_after"):
                errors.append(f"missing review_after for time-sensitive page: {rel}")
        if status == "seed" and not is_template and meta.get("created"):
            created = date_value(meta["created"])
            if created and (dt.date.today() - created).days > CONFIG["seed_warn_days"]:
                warnings.append(f"old seed note: {rel}")
        if SECRET.search(path.read_text(encoding="utf-8")):
            errors.append(f"possible credential pattern in {rel}")
        if kind == "concept" and not is_template:
            text = re.sub(r"```.*?```", "", body, flags=re.S)
            text = re.sub(r"[#|`*_\-]", "", text)
            if len(re.sub(r"\s+", "", text)) < 240:
                warnings.append(f"near-empty concept: {rel}")

    # Resolve wikilinks by full relative path first, then unique basename.
    incoming: defaultdict[Path, int] = defaultdict(int)
    for path, (_, body, _) in records.items():
        for raw_target in WIKILINK.findall(body):
            target = raw_target.strip().replace("\\", "/")
            target_path = Path(target[:-3] if target.endswith(".md") else target)
            candidates: list[Path] = []
            direct = ROOT / str(target_path)
            if direct.exists():
                candidates = [direct]
            else:
                md_direct = ROOT / (str(target_path) + ".md")
                if md_direct.exists():
                    candidates = [md_direct]
                else:
                    candidates = stem_map.get(target_path.name.casefold(), [])
            if not candidates:
                errors.append(f"broken wikilink in {path.relative_to(ROOT)}: [[{raw_target}]]")
            elif len(candidates) == 1:
                incoming[candidates[0]] += 1

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
        meta, _, _ = records[path]
        exempt = rel in {"README.md", "AGENTS.md"} or rel.startswith("99-Templates/") or rel.startswith("99-System/")
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
    for path, (meta, _, _) in records.items():
        if meta.get("page_kind") != "current-state" and ("current" in meta or "next" in meta):
            errors.append(f"dynamic current/next field outside Current-State: {path.relative_to(ROOT)}")

    evidence_index = ROOT / "09-Evidence" / "Evidence-Index.md"
    if not evidence_index.exists():
        errors.append("missing 09-Evidence/Evidence-Index.md")

    print("Vault QA")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARN: {item}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
