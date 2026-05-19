# Hot Chat with AI

Daily public AI digest: collect high-signal AI questions, answers, and discussions, commit them to GitHub, and publish them as a GitHub Pages site.

## What It Does

- Runs every day at 08:15 Asia/Shanghai with GitHub Actions.
- Collects public AI-related activity from Hacker News and Stack Overflow.
- Writes a dated JSON file in `data/`, a Markdown post in `public/posts/`, and the current digest in `public/latest.json`.
- Publishes `public/` to GitHub Pages so it can be viewed publicly.

## Local Run

```bash
python scripts/collect.py
python -m http.server 8080 --directory public
```

Open `http://localhost:8080`.

## GitHub Setup

1. Create a public GitHub repository and push this folder.
2. In GitHub, open `Settings -> Pages`.
3. Set `Build and deployment` to `GitHub Actions`.
4. Run `Daily AI Digest` manually once from the Actions tab.

After the first successful run, your public site should be available at:

```text
https://<your-github-name>.github.io/<repo-name>/
```

## Add More Sources

Add another collector function in `scripts/collect.py` that returns `Item` objects, then include it in the `collectors` list inside `main()`.

Good next sources:

- Reddit AI communities, if you add API credentials.
- Product Hunt AI launches.
- GitHub trending repositories tagged with AI.
- Your own saved ChatGPT/Claude/Gemini conversations, if you export them intentionally.

Do not collect private chats without explicit consent from the account owner.
