#!/usr/bin/env python3
"""Import Q&A submissions from GitHub Issues into the private review inbox."""

from __future__ import annotations

import json
import os
import re
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional


ROOT = Path(__file__).resolve().parents[1]
SUBMISSIONS_DIR = ROOT / "content" / "submissions"


def fetch_json(url: str, token: Optional[str]) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "hot-qa-with-ai/0.1",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"^\[q&a\]\s*", "", value)
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:72] or "submission"


def extract_field(body: str, label: str) -> str:
    pattern = rf"### {re.escape(label)}\s*(.*?)(?=\n### |\Z)"
    match = re.search(pattern, body, flags=re.S)
    if not match:
        return ""
    value = match.group(1).strip()
    return re.sub(r"\n{3,}", "\n\n", value)


def parse_issue(issue: dict[str, Any]) -> dict[str, Any]:
    body = issue.get("body") or ""
    title = extract_field(body, "Title") or re.sub(r"^\[Q&A\]\s*", "", issue.get("title", ""))
    tags = [
        tag.strip()
        for tag in extract_field(body, "Tags").replace("，", ",").split(",")
        if tag.strip()
    ]
    return {
        "id": f"issue-{issue['number']}-{slugify(title)}",
        "title": title.strip(),
        "question": extract_field(body, "Question"),
        "answer": extract_field(body, "AI Answer"),
        "model": extract_field(body, "Model") or "Unknown",
        "tags": tags,
        "why": extract_field(body, "Why is this good?"),
        "author_alias": issue.get("user", {}).get("login", "unknown"),
        "source_url": issue.get("html_url"),
        "submitted_at": issue.get("created_at"),
        "imported_at": datetime.now(timezone.utc).isoformat(),
        "status": "needs_review",
    }


def import_issues(repo: str, token: Optional[str]) -> int:
    SUBMISSIONS_DIR.mkdir(parents=True, exist_ok=True)
    query = urllib.parse.urlencode(
        {
            "state": "open",
            "labels": "submission",
            "per_page": "100",
        }
    )
    url = f"https://api.github.com/repos/{repo}/issues?{query}"
    issues = [issue for issue in fetch_json(url, token) if "pull_request" not in issue]
    count = 0

    for issue in issues:
        parsed = parse_issue(issue)
        if not parsed["question"] or not parsed["answer"]:
            continue
        path = SUBMISSIONS_DIR / f"{parsed['id']}.json"
        path.write_text(json.dumps(parsed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        count += 1
    return count


def main() -> int:
    repo = os.getenv("GITHUB_REPOSITORY")
    if not repo:
        print("GITHUB_REPOSITORY is not set; skipping GitHub Issues import.")
        return 0

    count = import_issues(repo, os.getenv("GITHUB_TOKEN"))
    print(f"Imported {count} Q&A submission issue(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
