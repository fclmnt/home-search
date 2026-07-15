#!/usr/bin/env python3
"""Retire de annonces.csv les annonces dont le lien est mort ou expiré.

Prudent par design :
- suppression uniquement sur signal définitif (404/410, statut structuré
  EXPIRED/DELETED/SoldOut, redirection hors de la page d'annonce, ou
  mention d'expiration pour les sites sans données structurées) ;
- les erreurs transitoires (timeout, 403, 5xx) conservent l'annonce ;
- garde-fou : si plus de 50 % des liens semblent morts d'un coup, on
  n'efface rien (probable changement de structure d'un site, pas une
  expiration massive).
"""
import csv
import os
import re
import sys
import urllib.error
import urllib.request

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE, "annonces.csv")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

# Statuts structurés (JSON embarqué / schema.org) — fiables.
DEAD_STATUS_RE = re.compile(
    r'"status"\s*:\s*"(?:EXPIRED|DELETED|REMOVED|SOLD)[^"]*"'
    r'|schema\.org/(?:SoldOut|OutOfStock|Discontinued)', re.IGNORECASE)
ALIVE_STATUS_RE = re.compile(
    r'"status"\s*:\s*"ACTIVE"|schema\.org/InStock', re.IGNORECASE)

# Marqueurs texte — uniquement pour les sites SANS catalogue i18n embarqué
# (Kijiji inclut « This ad is no longer available » dans le JS de CHAQUE page,
# active ou non : ne jamais appliquer ces marqueurs à Kijiji).
TEXT_MARKERS = [
    "n'est plus disponible", "n&#039;est plus disponible", "n’est plus disponible",
    "annonce a expiré", "a été supprimée", "n'est plus en vigueur",
    "n’est plus en vigueur", "cette inscription est introuvable",
]

def status(url):
    """Retourne 'dead', 'alive' ou 'unknown'."""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "fr-CA,fr;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            final = resp.geturl()
            body = resp.read(600_000).decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return "dead" if e.code in (404, 410) else "unknown"
    except Exception:
        return "unknown"

    if "kijiji.ca" in url:
        # Annonce retirée : redirection vers les résultats (/b-) au lieu de /v-
        if "/v-" in url and "/v-" not in final:
            return "dead"
        if DEAD_STATUS_RE.search(body):
            return "dead"
        # Statut ACTIVE explicite -> vivante ; sinon on ne conclut pas.
        return "alive" if ALIVE_STATUS_RE.search(body) else "unknown"

    if DEAD_STATUS_RE.search(body):
        return "dead"
    low = body.lower()
    if any(m in low for m in TEXT_MARKERS):
        return "dead"
    return "alive"

def main():
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)

    kept, removed, unknown = [], [], 0
    for r in rows:
        # Marketplace exige une connexion : impossible à vérifier sans session, on conserve
        if not r["lien"].startswith("http") or "facebook.com" in r["lien"]:
            kept.append(r)
            continue
        s = status(r["lien"])
        if s == "dead":
            removed.append(r)
            print(f"RETIRÉ (lien mort) : {r['titre']} — {r['lien']}")
        else:
            if s == "unknown":
                unknown += 1
            kept.append(r)

    checked = len(removed) + len(kept)
    if removed and len(removed) > checked / 2:
        print(f"GARDE-FOU : {len(removed)}/{checked} liens semblent morts — trop pour être "
              "crédible, aucune suppression effectuée (structure de site probablement changée).")
        sys.exit(1)

    if removed:
        with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(kept)
    print(f"{len(rows)} annonces : {len(removed)} retirées, {unknown} injoignables (conservées), {len(kept)} restantes")

if __name__ == "__main__":
    main()
