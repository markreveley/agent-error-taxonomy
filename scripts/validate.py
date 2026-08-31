#!/usr/bin/env python3
"""Validate incident metadata and verbatim evidence against a source checkout."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECORD_ID = re.compile(r"AET-[A-Z0-9]+-\d{4}$")
STATUSES = {"confirmed", "probable", "contested"}
REQUIRED = {
    "id",
    "title",
    "status",
    "corpus",
    "source_repository",
    "source_revision",
    "source_path",
    "source_lines",
    "agent_system",
    "agent_model",
    "detection",
    "primary_type",
    "secondary_types",
    "confidence",
}


def frontmatter(text: str, path: Path) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing opening frontmatter delimiter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"{path}: missing closing frontmatter delimiter")
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line or line[0].isspace() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"\'')
    return result


def list_value(raw: str) -> list[str]:
    raw = raw.strip()
    if not (raw.startswith("[") and raw.endswith("]")):
        return []
    return [part.strip().strip('"\'') for part in raw[1:-1].split(",") if part.strip()]


def git_head(path: Path) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(path), "rev-parse", "HEAD"],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-root",
        type=Path,
        help="optional elixir-mind checkout used to validate quoted evidence",
    )
    args = parser.parse_args()

    errors: list[str] = []
    type_ids: set[str] = set()
    for path in sorted((ROOT / "taxonomy").glob("*.md")):
        if path.name == "README.md":
            continue
        try:
            metadata = frontmatter(path.read_text(), path)
        except ValueError as error:
            errors.append(str(error))
            continue
        if metadata.get("id"):
            type_ids.add(metadata["id"])

    records: list[tuple[Path, str, dict[str, str]]] = []
    seen_ids: dict[str, Path] = {}
    for path in sorted((ROOT / "records").glob("**/*.md")):
        if path.name in {"README.md", "_template.md", "index.md"}:
            continue
        text = path.read_text()
        try:
            metadata = frontmatter(text, path)
        except ValueError as error:
            errors.append(str(error))
            continue
        records.append((path, text, metadata))
        missing = REQUIRED - metadata.keys()
        if missing:
            errors.append(f"{path}: missing fields: {', '.join(sorted(missing))}")
        record_id = metadata.get("id", "")
        if not RECORD_ID.fullmatch(record_id):
            errors.append(f"{path}: invalid record id {record_id!r}")
        if record_id in seen_ids:
            errors.append(f"{path}: duplicate id also used by {seen_ids[record_id]}")
        else:
            seen_ids[record_id] = path
        if metadata.get("status") not in STATUSES:
            errors.append(f"{path}: invalid status {metadata.get('status')!r}")
        primary = metadata.get("primary_type", "")
        if primary not in type_ids:
            errors.append(f"{path}: undefined primary type {primary!r}")
        for secondary in list_value(metadata.get("secondary_types", "")):
            if secondary not in type_ids:
                errors.append(f"{path}: undefined secondary type {secondary!r}")

    if args.source_root:
        source_root = args.source_root.resolve()
        source_head = git_head(source_root)
        for path, text, metadata in records:
            source_path = source_root / metadata.get("source_path", "")
            if not source_path.is_file():
                errors.append(f"{path}: source file not found: {source_path}")
                continue
            if source_head and metadata.get("source_revision") != source_head:
                errors.append(
                    f"{path}: source revision {metadata.get('source_revision')!r} "
                    f"does not match checkout HEAD {source_head}"
                )
            source_text = source_path.read_text()
            blocks = re.findall(r"````text\n(.*?)\n````", text, flags=re.DOTALL)
            if not blocks:
                errors.append(f"{path}: no four-backtick verbatim evidence block")
            ranges = list_value(metadata.get("source_lines", ""))
            if len(blocks) != len(ranges):
                errors.append(
                    f"{path}: {len(blocks)} evidence blocks but "
                    f"{len(ranges)} source line ranges"
                )
                continue
            source_lines = source_text.splitlines()
            for number, (block, line_range) in enumerate(
                zip(blocks, ranges), start=1
            ):
                if not re.match(
                    r"[ \t\r\n]*## (?:User|Assistant)[ \t]*(?:\n|$)", block
                ):
                    errors.append(
                        f"{path}: verbatim evidence block {number} must begin with an "
                        "exact '## User' or '## Assistant' source header"
                    )
                match = re.fullmatch(r"(\d+)(?:-(\d+))?", line_range)
                if not match:
                    errors.append(
                        f"{path}: invalid source line range {line_range!r}"
                    )
                    continue
                start = int(match.group(1))
                end = int(match.group(2) or start)
                excerpt = "\n".join(source_lines[start - 1 : end])
                if block != excerpt:
                    errors.append(
                        f"{path}: verbatim evidence block {number} is not an exact "
                        f"copy of source lines {line_range}"
                    )

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"validated {len(records)} records and {len(type_ids)} taxonomy types")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
