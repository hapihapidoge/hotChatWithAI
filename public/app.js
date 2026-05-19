const sourceClass = (source) => (source === "Hacker News" ? "hn" : "so");

const inferRepoUrl = () => {
  const host = window.location.hostname;
  const path = window.location.pathname.split("/").filter(Boolean)[0];
  if (host.endsWith(".github.io") && path) {
    return `https://github.com/${host.replace(".github.io", "")}/${path}`;
  }
  return "https://github.com/";
};

const itemCard = (item) => `
  <article class="card">
    <span class="pill ${sourceClass(item.source)}">${item.source}</span>
    <h3><a href="${item.url}" target="_blank" rel="noreferrer">${item.title}</a></h3>
    <p class="meta">
      <span>${item.kind}</span>
      <span>${item.score} points</span>
      <span>${item.comments} activity</span>
    </p>
    <p class="reason">${item.why_it_matters}</p>
  </article>
`;

const itemRow = (item) => `
  <article class="row">
    <h3><a href="${item.url}" target="_blank" rel="noreferrer">${item.title}</a></h3>
    <p class="meta">
      <span>${item.source}</span>
      <span>${item.score} points</span>
      <span>${item.comments} activity</span>
    </p>
  </article>
`;

async function loadDigest() {
  document.querySelector("#repo-link").href = inferRepoUrl();

  const [digest, archive] = await Promise.all([
    fetch("./latest.json").then((response) => response.json()),
    fetch("./archive.json").then((response) => response.json()).catch(() => []),
  ]);

  document.title = `Hot Chat with AI - ${digest.date}`;
  document.querySelector("#generated").textContent = `Latest digest: ${digest.date}`;
  document.querySelector("#item-count").textContent = digest.summary.items_collected;
  document.querySelector("#source-count").textContent = digest.summary.sources.length;
  document.querySelector("#highlights").innerHTML = digest.highlights.map(itemCard).join("");
  document.querySelector("#questions").innerHTML = digest.top_questions.map(itemRow).join("");
  document.querySelector("#discussions").innerHTML = digest.hot_discussions.map(itemRow).join("");
  document.querySelector("#archive").innerHTML = archive
    .map((entry) => `<a href="./${entry.path}">${entry.date} · ${entry.items} items</a>`)
    .join("");
}

loadDigest().catch((error) => {
  document.querySelector("#generated").textContent = "Could not load latest digest.";
  console.error(error);
});
