#!/usr/bin/env python3
"""Génère index.html (site local) à partir de annonces.csv."""
import csv
import datetime
import json
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE, "annonces.csv")
HTML_PATH = os.path.join(BASE, "index.html")

with open(CSV_PATH, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

data = json.dumps(rows, ensure_ascii=False).replace("</", "<\\/")
stamp = datetime.datetime.now().strftime("%d %B %Y à %H:%M")

page = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Recherche d'appartements — Montréal</title>
<style>
  :root {
    --bg: #f5f3ef; --card: #ffffff; --ink: #1f2933; --muted: #6b7280;
    --line: #e5e1d8; --accent: #1f4e5f; --new: #2e7d32; --new-bg: #e2f0d9;
    --chip: #eef1f4;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #15181c; --card: #1f242b; --ink: #e8e6e1; --muted: #9aa2ad;
      --line: #2c333c; --accent: #7fb3c8; --new: #8fd19e; --new-bg: #23402a;
      --chip: #2a313a;
    }
  }
  * { box-sizing: border-box; margin: 0; }
  body { background: var(--bg); color: var(--ink); font: 16px/1.5 -apple-system, "Segoe UI", sans-serif; padding: 24px; }
  header { max-width: 1200px; margin: 0 auto 20px; }
  h1 { font-size: 26px; letter-spacing: -0.02em; }
  .sub { color: var(--muted); font-size: 14px; margin-top: 4px; }
  .toolbar { max-width: 1200px; margin: 0 auto 20px; display: flex; flex-wrap: wrap; gap: 12px; align-items: center; }
  .toolbar select, .toolbar label {
    background: var(--card); border: 1px solid var(--line); border-radius: 8px;
    padding: 7px 12px; font-size: 14px; color: var(--ink); cursor: pointer;
  }
  .toolbar label { display: flex; align-items: center; gap: 7px; user-select: none; }
  .count { margin-left: auto; color: var(--muted); font-size: 14px; }
  .grid { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 18px; }
  .card {
    background: var(--card); border: 1px solid var(--line); border-radius: 14px;
    overflow: hidden; display: flex; flex-direction: column; transition: opacity .25s;
  }
  .card.vu { opacity: .75; }
  .photo { position: relative; aspect-ratio: 16/10; background: linear-gradient(135deg, #3c5a6a, #1f4e5f); }
  .photo img { width: 100%; height: 100%; object-fit: cover; display: block; }
  .photo .noimg { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 42px; }
  .badge-new {
    position: absolute; top: 10px; left: 10px; background: var(--new-bg); color: var(--new);
    font-size: 12px; font-weight: 700; padding: 3px 10px; border-radius: 999px;
  }
  .badge-score {
    position: absolute; top: 10px; right: 10px; background: rgba(0,0,0,.65); color: #fff;
    font-size: 12px; font-weight: 700; padding: 3px 9px; border-radius: 999px;
  }
  .body { padding: 14px 16px 16px; display: flex; flex-direction: column; gap: 8px; flex: 1; }
  .price { font-size: 22px; font-weight: 800; }
  .price small { font-size: 13px; font-weight: 500; color: var(--muted); }
  .title { font-size: 15px; font-weight: 600; line-height: 1.35; }
  .chips { display: flex; flex-wrap: wrap; gap: 6px; }
  .chip { background: var(--chip); border-radius: 999px; padding: 2px 10px; font-size: 12.5px; color: var(--ink); }
  .metro { display: flex; align-items: center; gap: 7px; font-size: 13.5px; color: var(--muted); }
  .dot { width: 11px; height: 11px; border-radius: 50%; flex: none; }
  .dot.verte { background: #008E4F; } .dot.orange { background: #EF8122; }
  .dot.bleue { background: #0083CA; } .dot.autre { background: #9aa2ad; }
  .notes { font-size: 13px; color: var(--muted); display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
  .notes.open { -webkit-line-clamp: unset; }
  .actions { margin-top: auto; display: flex; gap: 10px; padding-top: 10px; }
  .btn {
    flex: 1; text-align: center; border-radius: 9px; padding: 9px 10px; font-size: 14px;
    font-weight: 600; cursor: pointer; border: 1px solid var(--line); background: transparent;
    color: var(--ink); text-decoration: none; font-family: inherit;
  }
  .btn.primary { background: var(--accent); border-color: var(--accent); color: #fff; }
  .card.vu .btn-vu { background: var(--new-bg); color: var(--new); border-color: transparent; }
  .empty { max-width: 1200px; margin: 40px auto; text-align: center; color: var(--muted); }
</style>
</head>
<body>
<header>
  <h1>🏠 Recherche d'appartements — Montréal</h1>
  <div class="sub">1900–2400 $ · 2+ chambres · 900+ pi² · métro ≤ 12 min (ligne verte, pas à l'est de Pie-IX) · mis à jour le __STAMP__</div>
</header>
<div class="toolbar">
  <select id="fQuartier"><option value="">Tous les quartiers</option></select>
  <select id="fTri">
    <option value="score">Tri : score</option>
    <option value="prix">Tri : prix croissant</option>
    <option value="pi2">Tri : superficie</option>
    <option value="date">Tri : plus récentes</option>
  </select>
  <label><input type="checkbox" id="fMasquer"> Masquer les annonces vues</label>
  <span class="count" id="count"></span>
</div>
<div class="grid" id="grid"></div>
<div class="empty" id="empty" hidden>Aucune annonce à afficher avec ces filtres.</div>
<script>
const DATA = __DATA__;
const LS_KEY = "home-search-vus";
const vus = new Set(JSON.parse(localStorage.getItem(LS_KEY) || "[]"));
const save = () => localStorage.setItem(LS_KEY, JSON.stringify([...vus]));
const num = v => { const m = String(v).match(/\\d+/); return m ? +m[0] : null; };
const esc = s => String(s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));

const quartiers = [...new Set(DATA.map(a => a.quartier))].sort();
const selQ = document.getElementById("fQuartier");
quartiers.forEach(q => selQ.append(new Option(q, q)));

function ligneClass(l) {
  l = (l || "").toLowerCase();
  if (l.includes("verte")) return "verte";
  if (l.includes("orange")) return "orange";
  if (l.includes("bleue")) return "bleue";
  return "autre";
}

function card(a) {
  const el = document.createElement("article");
  el.className = "card" + (vus.has(a.lien) ? " vu" : "");
  const sf = a.superficie_pi2 && a.superficie_pi2 !== "n/d" ? esc(a.superficie_pi2) + " pi²" : "superficie n/d";
  const balcon = a.balcon === "oui" ? "balcon ✓" : (a.balcon === "non" ? "sans balcon" : "balcon n/d");
  el.innerHTML = `
    <div class="photo">
      ${a.photo ? `<img src="${esc(a.photo)}" alt="" loading="lazy" onerror="this.remove()">` : ""}
      <div class="noimg" ${a.photo ? "hidden" : ""}>🏢</div>
      ${a.statut === "NOUVEAU" ? '<span class="badge-new">NOUVEAU</span>' : ""}
      <span class="badge-score">${esc(a.score)}/10</span>
    </div>
    <div class="body">
      <div class="price">${esc(a.prix)} $ <small>/ mois</small></div>
      <div class="title">${esc(a.titre)}</div>
      <div class="chips">
        <span class="chip">${esc(a.quartier)}</span>
        <span class="chip">${sf}</span>
        <span class="chip">${esc(a.chambres)} ch.</span>
        <span class="chip">${balcon}</span>
      </div>
      <div class="metro"><span class="dot ${ligneClass(a.ligne_metro)}"></span>${esc(a.station_metro)} · ${esc(a.minutes_a_pied)} min à pied</div>
      <div class="notes" onclick="this.classList.toggle('open')" title="${esc(a.notes)}">${esc(a.notes)}</div>
      <div class="actions">
        <a class="btn primary" href="${esc(a.lien)}" target="_blank" rel="noopener">Voir l'annonce ↗</a>
        <button class="btn btn-vu"></button>
      </div>
    </div>`;
  const btn = el.querySelector(".btn-vu");
  const paint = () => { btn.textContent = vus.has(a.lien) ? "✓ Vu" : "Marquer comme vu"; };
  paint();
  btn.onclick = () => {
    vus.has(a.lien) ? vus.delete(a.lien) : vus.add(a.lien);
    save();
    el.classList.toggle("vu", vus.has(a.lien));
    paint();
    if (document.getElementById("fMasquer").checked) render();
    else updateCount();
  };
  return el;
}

function updateCount() {
  const visible = document.querySelectorAll(".card").length;
  document.getElementById("count").textContent =
    `${visible} annonce${visible > 1 ? "s" : ""} affichée${visible > 1 ? "s" : ""} · ${vus.size} vue${vus.size > 1 ? "s" : ""} au total`;
}

function render() {
  const q = selQ.value, tri = document.getElementById("fTri").value;
  const masquer = document.getElementById("fMasquer").checked;
  let list = DATA.filter(a => (!q || a.quartier === q) && !(masquer && vus.has(a.lien)));
  const by = {
    score: (x, y) => (num(y.score) - num(x.score)) || (num(x.prix) - num(y.prix)),
    prix: (x, y) => num(x.prix) - num(y.prix),
    pi2: (x, y) => (num(y.superficie_pi2) || 0) - (num(x.superficie_pi2) || 0),
    date: (x, y) => y.date_ajout.localeCompare(x.date_ajout) || (num(y.score) - num(x.score)),
  }[tri];
  list.sort((x, y) => ((y.statut === "NOUVEAU") - (x.statut === "NOUVEAU")) || by(x, y));
  const grid = document.getElementById("grid");
  grid.replaceChildren(...list.map(card));
  document.getElementById("empty").hidden = list.length > 0;
  updateCount();
}

selQ.onchange = render;
document.getElementById("fTri").onchange = render;
document.getElementById("fMasquer").onchange = render;
render();
</script>
</body>
</html>
"""

page = page.replace("__DATA__", data).replace("__STAMP__", stamp)
with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(page)
print(f"OK : {HTML_PATH} ({len(rows)} annonces)")
