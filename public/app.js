let allEntries = [];
let activeTag = "全部";

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
    <span class="pill">${item.model}</span>
    <h3><a href="./${item.path}">${item.title}</a></h3>
    <p class="meta">
      <span>${item.author_alias}</span>
      <span>${item.tags.join(" / ")}</span>
    </p>
    <p class="question">${item.question}</p>
    <p class="reason">${item.summary}</p>
  </article>
`;

const itemRow = (item) => `
  <article class="row">
    <h3><a href="./${item.path}">${item.title}</a></h3>
    <p class="question">${item.question}</p>
    <p class="reason">${item.summary}</p>
    <p class="meta">
      <span>${item.model}</span>
      <span>${item.author_alias}</span>
      <span>${item.tags.join(" / ")}</span>
    </p>
  </article>
`;

const renderTags = (tags) => {
  const values = ["全部", ...tags];
  document.querySelector("#tags").innerHTML = values
    .map((tag) => `<button class="${tag === activeTag ? "active" : ""}" data-tag="${tag}">${tag}</button>`)
    .join("");
};

const renderEntries = () => {
  const query = document.querySelector("#search").value.trim().toLowerCase();
  const filtered = allEntries.filter((item) => {
    const haystack = [item.title, item.question, item.answer, item.summary, item.tags.join(" ")]
      .join(" ")
      .toLowerCase();
    const tagMatches = activeTag === "全部" || item.tags.includes(activeTag);
    const queryMatches = !query || haystack.includes(query);
    return tagMatches && queryMatches;
  });
  document.querySelector("#entries").innerHTML = filtered.map(itemRow).join("");
};

async function loadDigest() {
  document.querySelector("#repo-link").href = inferRepoUrl();

  const [digest, archive] = await Promise.all([
    fetch("./qa.json").then((response) => response.json()),
    fetch("./archive.json").then((response) => response.json()).catch(() => []),
  ]);

  allEntries = digest.entries;
  document.title = "Hot Q&A with AI";
  document.querySelector("#generated").textContent = `Generated: ${new Date(
    digest.generated_at,
  ).toLocaleString()}`;
  document.querySelector("#item-count").textContent = digest.summary.items;
  document.querySelector("#source-count").textContent = digest.summary.tags.length;
  document.querySelector("#highlights").innerHTML = digest.featured.map(itemCard).join("");
  renderTags(digest.summary.tags);
  renderEntries();
  document.querySelector("#archive").innerHTML = archive
    .map((entry) => `<a href="./${entry.path}">${entry.title}</a>`)
    .join("");

  document.querySelector("#search").addEventListener("input", renderEntries);
  document.querySelector("#tags").addEventListener("click", (event) => {
    if (!event.target.matches("button")) return;
    activeTag = event.target.dataset.tag;
    renderTags(digest.summary.tags);
    renderEntries();
  });
}

loadDigest().catch((error) => {
  document.querySelector("#generated").textContent = "Could not load latest digest.";
  console.error(error);
});
