#!/usr/bin/env python3
"""Collect public AI-related questions and discussions for the daily digest."""

from __future__ import annotations

import json
import html
import os
import re
import sys
import textwrap
import urllib.parse
import urllib.request
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
POSTS_DIR = ROOT / "public" / "posts"
LATEST_JSON = ROOT / "public" / "latest.json"
ARCHIVE_JSON = ROOT / "public" / "archive.json"

KEYWORDS = [
    "ai",
    "artificial intelligence",
    "agent",
    "agents",
    "llm",
    "openai",
    "chatgpt",
    "claude",
    "gemini",
    "model",
    "prompt",
    "rag",
]


@dataclass
class Item:
    id: str
    source: str
    kind: str
    title: str
    url: str
    score: int
    comments: int
    published_at: str
    why_it_matters: str


def fetch_json(url: str, timeout: int = 20) -> Any:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "hotchatwithAI/0.1 (+https://github.com/)",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def text_has_ai_signal(text: str) -> bool:
    text = text.lower()
    return any(keyword in text for keyword in KEYWORDS)


def clean_title(title: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(title)).strip()


def plural(value: int, singular: str, plural_word: Optional[str] = None) -> str:
    word = singular if value == 1 else plural_word or f"{singular}s"
    return f"{value} {word}"


def simple_reason(title: str, source: str, score: int, comments: int) -> str:
    title_lower = title.lower()
    if "agent" in title_lower:
        theme = "agent workflows and automation"
    elif "prompt" in title_lower:
        theme = "prompt design and practical AI use"
    elif "openai" in title_lower or "model" in title_lower or "llm" in title_lower:
        theme = "model behavior, APIs, or deployment choices"
    elif "question" in title_lower or title.endswith("?"):
        theme = "a question people are actively trying to answer"
    else:
        theme = "a public AI discussion with measurable attention"

    signals = []
    if score > 0:
        signals.append(plural(score, "point"))
    if comments > 0:
        signals.append(plural(comments, "comment"))
    signal_text = " and ".join(signals) if signals else "fresh public activity"
    return f"Useful because it touches {theme}, with {signal_text} on {source}."


def hn_items(since: datetime) -> list[Item]:
    numeric_since = int(since.timestamp())
    queries = ["AI", "LLM", "OpenAI", "ChatGPT", "agent", "Claude", "Gemini"]
    items: list[Item] = []

    for query in queries:
        url = (
            "https://hn.algolia.com/api/v1/search_by_date?"
            f"query={urllib.parse.quote(query)}&tags=story"
            f"&numericFilters=created_at_i>{numeric_since}&hitsPerPage=20"
        )
        payload = fetch_json(url)

        for hit in payload.get("hits", []):
            title = clean_title(hit.get("title") or hit.get("story_title") or "")
            if not title or not text_has_ai_signal(title):
                continue

            object_id = str(hit.get("objectID"))
            comments = int(hit.get("num_comments") or 0)
            points = int(hit.get("points") or 0)
            created = hit.get("created_at") or datetime.now(timezone.utc).isoformat()
            story_url = hit.get("url") or f"https://news.ycombinator.com/item?id={object_id}"

            items.append(
                Item(
                    id=f"hn-{object_id}",
                    source="Hacker News",
                    kind="discussion",
                    title=title,
                    url=story_url,
                    score=points,
                    comments=comments,
                    published_at=created,
                    why_it_matters=simple_reason(title, "Hacker News", points, comments),
                )
            )
    return items


def stackexchange_items(since: datetime) -> list[Item]:
    fromdate = int(since.timestamp())
    tags = ["openai-api", "artificial-intelligence", "chatgpt", "llm", "langchain"]
    items: list[Item] = []

    for tag in tags:
        url = (
            "https://api.stackexchange.com/2.3/questions?"
            f"fromdate={fromdate}&order=desc&sort=activity&tagged={urllib.parse.quote(tag)}"
            "&site=stackoverflow&filter=default&pagesize=20"
        )
        try:
            payload = fetch_json(url)
        except Exception as exc:  # noqa: BLE001
            print(f"warning: Stack Exchange fetch failed for {tag}: {exc}", file=sys.stderr)
            continue

        for question in payload.get("items", []):
            title = clean_title(question.get("title", ""))
            if not title:
                continue
            qid = str(question.get("question_id"))
            score = int(question.get("score") or 0)
            answers = int(question.get("answer_count") or 0)
            created = datetime.fromtimestamp(
                int(question.get("creation_date") or datetime.now(timezone.utc).timestamp()),
                tz=timezone.utc,
            ).isoformat()
            items.append(
                Item(
                    id=f"so-{qid}",
                    source="Stack Overflow",
                    kind="question",
                    title=title,
                    url=question.get("link", ""),
                    score=score,
                    comments=answers,
                    published_at=created,
                    why_it_matters=simple_reason(title, "Stack Overflow", score, answers),
                )
            )
    return items


def dedupe(items: list[Item]) -> list[Item]:
    seen: set[str] = set()
    unique: list[Item] = []
    for item in items:
        key = item.url or item.id
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


def item_rank(item: Item) -> int:
    source_bonus = 15 if item.source == "Hacker News" else 8
    question_bonus = 12 if item.kind == "question" or item.title.endswith("?") else 0
    return item.score * 3 + item.comments * 2 + source_bonus + question_bonus


def build_digest(items: list[Item], now: datetime) -> dict[str, Any]:
    ranked = sorted(dedupe(items), key=item_rank, reverse=True)
    top_questions = [item for item in ranked if item.kind == "question" or item.title.endswith("?")][:8]
    hot_discussions = [item for item in ranked if item not in top_questions][:12]
    highlights = ranked[:5]

    return {
        "date": now.date().isoformat(),
        "generated_at": now.isoformat(),
        "summary": {
            "items_collected": len(ranked),
            "sources": sorted({item.source for item in ranked}),
        },
        "highlights": [asdict(item) for item in highlights],
        "top_questions": [asdict(item) for item in top_questions],
        "hot_discussions": [asdict(item) for item in hot_discussions],
    }


def markdown_digest(digest: dict[str, Any]) -> str:
    date = digest["date"]
    lines = [
        f"# Hot AI Digest - {date}",
        "",
        f"Generated at: `{digest['generated_at']}`",
        "",
        "## Highlights",
        "",
    ]

    for item in digest["highlights"]:
        lines.extend(
            [
                f"- [{item['title']}]({item['url']})",
                f"  - Source: {item['source']} | Score: {item['score']} | Activity: {item['comments']}",
                f"  - {item['why_it_matters']}",
            ]
        )

    lines.extend(["", "## Good Questions", ""])
    for item in digest["top_questions"]:
        lines.append(f"- [{item['title']}]({item['url']}) - {item['source']}")

    lines.extend(["", "## Hot Discussions", ""])
    for item in digest["hot_discussions"]:
        lines.append(f"- [{item['title']}]({item['url']}) - {item['source']}")

    return "\n".join(lines) + "\n"


def update_archive(digest: dict[str, Any]) -> list[dict[str, str]]:
    archive: list[dict[str, str]] = []
    if ARCHIVE_JSON.exists():
        archive = json.loads(ARCHIVE_JSON.read_text(encoding="utf-8"))

    entry = {
        "date": digest["date"],
        "path": f"posts/{digest['date']}.md",
        "items": str(digest["summary"]["items_collected"]),
    }
    archive = [row for row in archive if row["date"] != digest["date"]]
    archive.insert(0, entry)
    return archive[:90]


def write_outputs(digest: dict[str, Any]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    POSTS_DIR.mkdir(parents=True, exist_ok=True)

    date = digest["date"]
    daily_json = DATA_DIR / f"{date}.json"
    daily_md = POSTS_DIR / f"{date}.md"

    daily_json.write_text(json.dumps(digest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    LATEST_JSON.write_text(json.dumps(digest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    daily_md.write_text(markdown_digest(digest), encoding="utf-8")
    ARCHIVE_JSON.write_text(json.dumps(update_archive(digest), indent=2) + "\n", encoding="utf-8")


def main() -> int:
    now = datetime.now(timezone.utc)
    lookback_hours = int(os.getenv("LOOKBACK_HOURS", "36"))
    since = now - timedelta(hours=lookback_hours)

    collectors = [hn_items, stackexchange_items]
    items: list[Item] = []
    for collector in collectors:
        try:
            items.extend(collector(since))
        except Exception as exc:  # noqa: BLE001
            print(f"warning: {collector.__name__} failed: {exc}", file=sys.stderr)

    digest = build_digest(items, now)
    write_outputs(digest)
    print(
        textwrap.dedent(
            f"""
            Wrote digest for {digest['date']}
            Items collected: {digest['summary']['items_collected']}
            Sources: {', '.join(digest['summary']['sources']) or 'none'}
            """
        ).strip()
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
