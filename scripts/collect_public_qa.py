#!/usr/bin/env python3
"""Collect high-signal public Q&A entries from public APIs."""

from __future__ import annotations

import html
import json
import re
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional


ROOT = Path(__file__).resolve().parents[1]
AUTO_DIR = ROOT / "content" / "auto"

SOURCES = [
    {
        "site": "genai",
        "tags": [],
        "label": "GenAI Stack Exchange",
    },
    {
        "site": "ai",
        "tags": [],
        "label": "AI Stack Exchange",
    },
    {
        "site": "stackoverflow",
        "tags": ["openai-api", "chatgpt", "llm", "langchain", "rag"],
        "label": "Stack Overflow",
    },
]


def fetch_json(url: str) -> Any:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "hot-qa-with-ai/0.1",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def strip_html(value: str) -> str:
    value = re.sub(r"<pre><code>.*?</code></pre>", " [code omitted] ", value, flags=re.S)
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def truncate(value: str, limit: int = 1200) -> str:
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "..."


def slugify(value: str) -> str:
    value = html.unescape(value).lower().strip()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:72] or "public-qa"


def stackexchange_url(site: str, fromdate: int, tag: Optional[str] = None) -> str:
    query = {
        "fromdate": str(fromdate),
        "order": "desc",
        "sort": "votes",
        "site": site,
        "pagesize": "40",
        "filter": "withbody",
    }
    if tag:
        query["tagged"] = tag
    return f"https://api.stackexchange.com/2.3/questions?{urllib.parse.urlencode(query)}"


def answer_url(site: str, answer_id: int) -> str:
    query = {
        "order": "desc",
        "sort": "votes",
        "site": site,
        "filter": "withbody",
    }
    return f"https://api.stackexchange.com/2.3/answers/{answer_id}?{urllib.parse.urlencode(query)}"


def best_answer_url(site: str, question_id: int) -> str:
    query = {
        "order": "desc",
        "sort": "votes",
        "site": site,
        "filter": "withbody",
        "pagesize": "1",
    }
    return (
        f"https://api.stackexchange.com/2.3/questions/{question_id}/answers?"
        f"{urllib.parse.urlencode(query)}"
    )


def fetch_answer(site: str, question: dict[str, Any]) -> Optional[dict[str, Any]]:
    accepted = question.get("accepted_answer_id")
    if accepted:
        payload = fetch_json(answer_url(site, int(accepted)))
        items = payload.get("items", [])
        return items[0] if items else None

    if int(question.get("answer_count") or 0) <= 0:
        return None

    payload = fetch_json(best_answer_url(site, int(question["question_id"])))
    items = payload.get("items", [])
    if not items:
        return None
    answer = items[0]
    if int(answer.get("score") or 0) < 1:
        return None
    return answer


def quality_signals(question: dict[str, Any], answer: dict[str, Any], source_label: str) -> list[str]:
    signals = [
        f"Public Q&A from {source_label}.",
        f"Question score: {question.get('score', 0)}; answer score: {answer.get('score', 0)}.",
    ]
    if question.get("accepted_answer_id"):
        signals.append("The answer was accepted by the question author.")
    if int(question.get("view_count") or 0) > 0:
        signals.append(f"Viewed {question.get('view_count')} times on the source site.")
    return signals


def public_entry(source: dict[str, Any], question: dict[str, Any], answer: dict[str, Any]) -> dict[str, Any]:
    title = html.unescape(question.get("title", "")).strip()
    qid = question["question_id"]
    created = datetime.fromtimestamp(int(question["creation_date"]), tz=timezone.utc).isoformat()
    tags = ["public-q&a", source["label"], *question.get("tags", [])]
    answer_text = truncate(strip_html(answer.get("body", "")), 1400)
    question_text = truncate(strip_html(question.get("body", "")), 700)
    answer_owner = answer.get("owner", {}).get("display_name", "unknown")

    return {
        "id": f"se-{source['site']}-{qid}-{slugify(title)}",
        "title": title,
        "question": question_text,
        "answer": answer_text,
        "summary": truncate(answer_text, 220),
        "tags": tags[:8],
        "model": "Public Q&A",
        "author_alias": answer_owner,
        "source_url": question.get("link"),
        "quality_signals": quality_signals(question, answer, source["label"]),
        "created_at": created,
        "curated_at": datetime.now(timezone.utc).isoformat(),
        "license": "Stack Exchange content is user-contributed and requires source attribution.",
        "source": source["label"],
    }


def collect_source(source: dict[str, Any], since: datetime) -> list[dict[str, Any]]:
    fromdate = int(since.timestamp())
    tags = source["tags"] or [None]
    entries: list[dict[str, Any]] = []

    for tag in tags:
        payload = fetch_json(stackexchange_url(source["site"], fromdate, tag))
        for question in payload.get("items", []):
            if int(question.get("score") or 0) < 1 and not question.get("accepted_answer_id"):
                continue
            answer = fetch_answer(source["site"], question)
            if not answer:
                continue
            entries.append(public_entry(source, question, answer))
    return entries


def write_entries(entries: list[dict[str, Any]]) -> None:
    AUTO_DIR.mkdir(parents=True, exist_ok=True)
    for entry in entries:
        path = AUTO_DIR / f"{entry['id']}.json"
        path.write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    since = datetime.now(timezone.utc) - timedelta(days=14)
    entries: list[dict[str, Any]] = []
    seen: set[str] = set()

    for source in SOURCES:
        try:
            for entry in collect_source(source, since):
                if entry["source_url"] in seen:
                    continue
                seen.add(entry["source_url"])
                entries.append(entry)
        except Exception as exc:  # noqa: BLE001
            print(f"warning: failed to collect {source['label']}: {exc}")

    entries = sorted(entries, key=lambda item: item["curated_at"], reverse=True)[:80]
    write_entries(entries)
    print(f"Collected {len(entries)} public Q&A entr{'y' if len(entries) == 1 else 'ies'}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
