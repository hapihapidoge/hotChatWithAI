# Hot Q&A with AI

A public, GitHub-backed knowledge base for high-quality questions people ask AI and the answers worth preserving.

## What It Does

- Stores curated AI Q&A entries in `content/curated/*.json`.
- Builds `public/qa.json`, `public/latest.json`, `public/archive.json`, and Markdown pages in `public/posts/`.
- Publishes `public/` to GitHub Pages.
- Supports search, tags, featured questions, and a public archive.
- Keeps every change in GitHub history.

This is not an AI news collector. It is closer to a lightweight Zhihu-style library for excellent human questions and useful AI answers.

## Local Run

```bash
python scripts/build_site.py
python -m http.server 8080 --directory public
```

Open `http://localhost:8080`.

## GitHub Setup

1. Create a public GitHub repository and push this folder.
2. In GitHub, open `Settings -> Pages`.
3. Set `Build and deployment` to `GitHub Actions`.
4. Run `Daily AI Q&A Build` manually once from the Actions tab.

After the first successful run, your public site should be available at:

```text
https://<your-github-name>.github.io/<repo-name>/
```

## Add More Sources

The safest MVP workflow is:

1. Put raw candidate conversations in `content/submissions/`.
2. Remove private or identifying details.
3. Rewrite the entry into the schema used by `content/curated/*.json`.
4. Run `python scripts/build_site.py`.
5. Commit and push.

You can also enable GitHub Issues using `.github/ISSUE_TEMPLATE/qa-submission.yml`, then manually review good submissions and move them into `content/curated/`.

## Curation Standard

A good entry should have:

- a question that many people may also have,
- enough context to make the answer meaningful,
- a reusable answer, framework, checklist, example, or decision,
- no private data,
- a clear reason why it is worth saving.

Do not publish private chats without explicit consent from the account owner.
