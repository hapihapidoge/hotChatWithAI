#!/usr/bin/env python3
"""Build the public Q&A site from curated AI conversation entries."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content" / "curated"
AUTO_DIR = ROOT / "content" / "auto"
PUBLIC_DIR = ROOT / "public"
POSTS_DIR = PUBLIC_DIR / "posts"
ALL_JSON = PUBLIC_DIR / "qa.json"
LATEST_JSON = PUBLIC_DIR / "latest.json"
ARCHIVE_JSON = PUBLIC_DIR / "archive.json"


@dataclass
class QAEntry:
    id: str
    title: str
    question: str
    answer: str
    summary: str
    tags: list[str]
    model: str
    author_alias: str
    source_url: Optional[str]
    quality_signals: list[str]
    created_at: str
    curated_at: str


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:80] or "qa"


def read_entries_from(directory: Path) -> list[QAEntry]:
    entries: list[QAEntry] = []
    for path in sorted(directory.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload = {key: value for key, value in payload.items() if key in QAEntry.__annotations__}
        entries.append(QAEntry(**payload))
    return entries


def read_entries() -> list[QAEntry]:
    entries = read_entries_from(CONTENT_DIR) + read_entries_from(AUTO_DIR)
    return sorted(entries, key=lambda item: item.curated_at, reverse=True)


def render_markdown(entry: QAEntry) -> str:
    source = f"\nSource: {entry.source_url}\n" if entry.source_url else ""
    signals = "\n".join(f"- {signal}" for signal in entry.quality_signals)
    tags = ", ".join(entry.tags)
    return f"""# {entry.title}

Curated at: `{entry.curated_at}`
Model: `{entry.model}`
Author: `{entry.author_alias}`
Tags: `{tags}`{source}

## Why It Is Good

{signals}

## Question

{entry.question}

## Answer

{entry.answer}
"""


def public_entry(entry: QAEntry) -> dict[str, Any]:
    data = asdict(entry)
    data["path"] = f"posts/{entry.id}.md"
    return data


def build_payload(entries: list[QAEntry]) -> dict[str, Any]:
    now = datetime.now(timezone.utc).isoformat()
    tags = sorted({tag for entry in entries for tag in entry.tags})
    models = sorted({entry.model for entry in entries})
    return {
        "generated_at": now,
        "summary": {
            "items": len(entries),
            "tags": tags,
            "models": models,
        },
        "featured": [public_entry(entry) for entry in entries[:6]],
        "entries": [public_entry(entry) for entry in entries],
    }


def build_archive(entries: list[QAEntry]) -> list[dict[str, str]]:
    return [
        {
            "id": entry.id,
            "title": entry.title,
            "path": f"posts/{entry.id}.md",
            "curated_at": entry.curated_at,
        }
        for entry in entries
    ]


def write_outputs(entries: list[QAEntry]) -> None:
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    payload = build_payload(entries)

    ALL_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LATEST_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    ARCHIVE_JSON.write_text(
        json.dumps(build_archive(entries), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    for entry in entries:
        post_path = POSTS_DIR / f"{entry.id}.md"
        post_path.write_text(render_markdown(entry), encoding="utf-8")


def main() -> int:
    entries = read_entries()
    write_outputs(entries)
    print(f"Built {len(entries)} curated Q&A entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
