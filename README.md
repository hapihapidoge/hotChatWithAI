# Hot Q&A with AI

A public, GitHub-backed Q&A aggregation site for high-quality AI-related questions and answers.

## What It Does

- Automatically collects public Q&A into `content/auto/*.json`.
- Stores hand-curated AI Q&A entries in `content/curated/*.json`.
- Builds `public/qa.json`, `public/latest.json`, `public/archive.json`, and Markdown pages in `public/posts/`.
- Publishes `public/` to GitHub Pages.
- Supports search, tags, featured questions, and a public archive.
- Keeps every change in GitHub history.

This is not an AI news collector. It is closer to a lightweight Zhihu-style Q&A library. Automatic public aggregation is the default; user submissions can be added later as a second channel.

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

The default workflow is automatic:

```bash
python scripts/collect_public_qa.py
python scripts/build_site.py
```

The current collector uses public Stack Exchange APIs:

- GenAI Stack Exchange
- AI Stack Exchange
- Stack Overflow tags such as `openai-api`, `chatgpt`, `llm`, `langchain`, and `rag`

Manual curation is still supported:

1. Put raw candidate conversations in `content/submissions/`.
2. Remove private or identifying details.
3. Rewrite the entry into the schema used by `content/curated/*.json`.
4. Run `python scripts/build_site.py`.
5. Commit and push.

You can also enable GitHub Issues using `.github/ISSUE_TEMPLATE/qa-submission.yml`, then manually review good submissions and move them into `content/curated/`.

## Automatic Collection

There are three realistic collection modes over time:

- **Public Q&A aggregation:** enabled now. The workflow collects public questions and accepted or high-scoring answers into `content/auto/`.
- **Opt-in submissions:** supported. Users submit Q&A through GitHub Issues, and the workflow imports issues with the `submission` label into `content/submissions/`.
- **Your own exports:** you export your own ChatGPT/Claude/Gemini conversations, then run a separate importer after removing private details.

Imported GitHub Issue submissions intentionally do not publish directly. Imported files stay in `content/submissions/` with `status: needs_review`; only files moved into `content/curated/` appear on the public site.

To test the importer locally:

```bash
GITHUB_REPOSITORY=<owner>/<repo> GITHUB_TOKEN=<token> python scripts/import_github_issues.py
```

## Curation Standard

A good entry should have:

- a question that many people may also have,
- enough context to make the answer meaningful,
- a reusable answer, framework, checklist, example, or decision,
- no private data,
- a clear reason why it is worth saving.

Do not publish private chats without explicit consent from the account owner.
