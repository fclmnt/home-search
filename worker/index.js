// Micro-backend de votes partagés pour la recherche d'appartements.
// Stockage : une seule clé KV "all" = { [lienAnnonce]: { [voterId]: 1 | -1 } }
const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};

export default {
  async fetch(req, env) {
    if (req.method === "OPTIONS") return new Response(null, { headers: CORS });
    const url = new URL(req.url);

    if (url.pathname === "/votes" && req.method === "GET") {
      const raw = (await env.VOTES.get("all")) || "{}";
      return new Response(raw, { headers: { ...CORS, "Content-Type": "application/json" } });
    }

    if (url.pathname === "/vote" && req.method === "POST") {
      let body;
      try { body = await req.json(); } catch { body = null; }
      const { listing, voter, vote } = body || {};
      if (typeof listing !== "string" || !listing || listing.length > 500 ||
          typeof voter !== "string" || !voter || voter.length > 64 ||
          ![1, -1, 0].includes(vote)) {
        return new Response("bad request", { status: 400, headers: CORS });
      }
      const all = JSON.parse((await env.VOTES.get("all")) || "{}");
      const entry = all[listing] || {};
      if (vote === 0) delete entry[voter];
      else entry[voter] = vote;
      if (Object.keys(entry).length) all[listing] = entry;
      else delete all[listing];
      await env.VOTES.put("all", JSON.stringify(all));
      return new Response(JSON.stringify(entry), { headers: { ...CORS, "Content-Type": "application/json" } });
    }

    return new Response("not found", { status: 404, headers: CORS });
  },
};
