#!/usr/bin/env python3
"""Validate the public growth-skills repository with the Python standard library."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

MAX_DESCRIPTION_CHARS = 200
MAX_SKILL_LINES = 250
PRIVATE_PATTERNS = (
    "adi" + "tya",
    "ez" + " money",
    "coo" + "kunity",
    "juice" + "box",
    "good" + "labs",
    "rh" + "iz",
    "her" + "mes",
    "search_" + "growth_vault",
    "vault" + "/",
    "startups" + "/",
    "." + "agent" + "/",
)
HOME_PATH = re.compile(r"/(?:Users|home)/[^/\s]+/", re.IGNORECASE)
SECRET_PATTERNS = (
    ("cloud key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("provider token", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b")),
    ("source-control token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b")),
    ("chat token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    ("platform key", re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b")),
    ("payment key", re.compile(r"\b(?:sk|rk)_live_[0-9A-Za-z]{16,}\b")),
    ("signed token", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b")),
    (
        "assigned credential",
        re.compile(
            r"\b(?:api[_-]?key|access[_-]?token|client[_-]?secret|secret)\s*[:=]\s*[\"'][A-Za-z0-9/+_.=-]{16,}[\"']",
            re.IGNORECASE,
        ),
    ),
)
SKIP_PARTS = {".git", "__pycache__", ".pytest_cache"}


def decode_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return json.loads(value)
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return value[1:-1].replace("''", "'")
    return value


def parse_frontmatter(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("must start with YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("frontmatter is not closed") from exc

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        if key in {"name", "description"}:
            fields[key] = decode_scalar(value)

    if not fields.get("name"):
        raise ValueError("frontmatter requires a one-line name")
    if not fields.get("description"):
        raise ValueError("frontmatter requires a one-line description")
    return fields["name"], fields["description"]


def text_files(root: Path):
    for path in sorted(root.rglob("*")):
        if path.is_symlink() or not path.is_file() or any(part in SKIP_PARTS for part in path.parts):
            continue
        try:
            path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        yield path


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    catalog_path = root / "catalog.json"
    skills_root = root / "skills"

    try:
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"catalog.json: {exc}"]

    if not isinstance(catalog, list):
        return ["catalog.json: top level must be a list"]

    entries: dict[str, str] = {}
    for index, item in enumerate(catalog):
        if not isinstance(item, dict) or not isinstance(item.get("name"), str) or not isinstance(item.get("description"), str):
            errors.append(f"catalog.json[{index}]: requires string name and description")
            continue
        name = item["name"]
        if name in entries:
            errors.append(f"catalog.json: duplicate skill {name}")
        entries[name] = item["description"]

    disk_names = {
        path.name
        for path in skills_root.iterdir()
        if path.is_dir()
    } if skills_root.is_dir() else set()

    if disk_names != set(entries):
        missing = sorted(set(entries) - disk_names)
        extra = sorted(disk_names - set(entries))
        if missing:
            errors.append(f"skills: missing directories for {', '.join(missing)}")
        if extra:
            errors.append(f"skills: uncataloged directories {', '.join(extra)}")

    chain_path = root / "chains" / "growth-system.json"
    try:
        chain = json.loads(chain_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"chains/growth-system.json: {exc}")
    else:
        stages = chain.get("stages") if isinstance(chain, dict) else None
        if not isinstance(stages, list):
            errors.append("chains/growth-system.json: stages must be a list")
        else:
            referenced: set[str] = set()
            for index, stage in enumerate(stages):
                skills = stage.get("skills") if isinstance(stage, dict) else None
                if not isinstance(skills, list) or not all(isinstance(name, str) for name in skills):
                    errors.append(f"chains/growth-system.json stages[{index}]: skills must be a string list")
                    continue
                referenced.update(skills)
                unknown = sorted(set(skills) - set(entries))
                if unknown:
                    errors.append(f"chains/growth-system.json stages[{index}]: unknown skills {', '.join(unknown)}")
            omitted = sorted(set(entries) - referenced)
            if omitted:
                errors.append(f"chains/growth-system.json: catalog skills missing from chain {', '.join(omitted)}")

    for expected_name, catalog_description in sorted(entries.items()):
        path = skills_root / expected_name / "SKILL.md"
        if not path.is_file():
            errors.append(f"{path.relative_to(root)}: missing SKILL.md")
            continue
        try:
            name, description = parse_frontmatter(path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
            continue
        if name != expected_name:
            errors.append(f"{path.relative_to(root)}: name {name!r} does not match directory")
        if description != catalog_description:
            errors.append(f"{path.relative_to(root)}: description differs from catalog.json")
        if len(description) > MAX_DESCRIPTION_CHARS:
            errors.append(f"{path.relative_to(root)}: description has {len(description)} characters; maximum is {MAX_DESCRIPTION_CHARS}")
        line_count = len(path.read_text(encoding="utf-8").splitlines())
        if line_count > MAX_SKILL_LINES:
            errors.append(f"{path.relative_to(root)}: has {line_count} lines; maximum is {MAX_SKILL_LINES}")

    for path in sorted(root.rglob("*")):
        if path.is_symlink() and not any(part in SKIP_PARTS for part in path.parts):
            errors.append(f"{path.relative_to(root)}: symlink is not allowed")

    for path in text_files(root):
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        blocked_private = False
        for pattern in PRIVATE_PATTERNS:
            if pattern.lower() in lowered:
                errors.append(f"{path.relative_to(root)}: blocked private pattern")
                blocked_private = True
                break
        if not blocked_private and HOME_PATH.search(text):
            errors.append(f"{path.relative_to(root)}: absolute home path")
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"{path.relative_to(root)}: possible {label}")
                break

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("validated catalog, chain, skill frontmatter, size limits, and public-safety rules")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
