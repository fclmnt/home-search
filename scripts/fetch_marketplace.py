#!/usr/bin/env python3
"""Scrape Facebook Marketplace (compte dédié, profil .fb-profile/) et dépose
les annonces brutes dans marketplace-raw.json pour l'agent de recherche.

Volontairement léger et poli : quelques recherches pré-filtrées, défilement
limité, pauses aléatoires, max ~10 visites de fiches par exécution.
Ne filtre PAS selon les critères fins (superficie, métro) — c'est le travail
de l'agent qui lit le JSON.
"""
import json
import os
import random
import re
import sys
import time

from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(BASE, ".fb-profile")
OUT = os.path.join(BASE, "marketplace-raw.json")
CSV_PATH = os.path.join(BASE, "annonces.csv")

SEARCHES = [
    "https://www.facebook.com/marketplace/montreal/propertyrentals?minPrice=1900&maxPrice=2400&minBedrooms=2&exact=false",
    "https://www.facebook.com/marketplace/montreal/search?query=5%201%2F2%20hochelaga&minPrice=1900&maxPrice=2400",
    "https://www.facebook.com/marketplace/montreal/search?query=5%201%2F2%20rosemont&minPrice=1900&maxPrice=2400",
    "https://www.facebook.com/marketplace/montreal/search?query=5%201%2F2%20villeray&minPrice=1900&maxPrice=2400",
    "https://www.facebook.com/marketplace/montreal/search?query=5%201%2F2%20plateau&minPrice=1900&maxPrice=2400",
]
MAX_DETAIL_VISITS = 10
SCROLLS_PER_SEARCH = 4

def pause(a=1.5, b=4.0):
    time.sleep(random.uniform(a, b))

def known_links():
    """Liens Marketplace déjà dans annonces.csv (pour ne pas revisiter les fiches)."""
    ids = set()
    if os.path.exists(CSV_PATH):
        import csv
        for r in csv.DictReader(open(CSV_PATH, newline="", encoding="utf-8")):
            m = re.search(r"/marketplace/item/(\d+)", r.get("lien", ""))
            if m:
                ids.add(m.group(1))
    return ids

def main():
    if not os.path.isdir(PROFILE):
        print("Profil .fb-profile/ absent — lancez d'abord scripts/fb_login.py")
        sys.exit(1)

    deja = known_links()
    items = {}
    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            PROFILE, headless=True, locale="fr-CA",
            viewport={"width": 1240, "height": 900},
            args=["--disable-blink-features=AutomationControlled"],
        )
        if not any(c["name"] == "c_user" for c in ctx.cookies("https://www.facebook.com")):
            print("SESSION EXPIRÉE — relancez scripts/fb_login.py pour vous reconnecter.")
            ctx.close()
            sys.exit(1)
        page = ctx.pages[0] if ctx.pages else ctx.new_page()

        for url in SEARCHES:
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=45000)
                pause(3, 6)
                for _ in range(SCROLLS_PER_SEARCH):
                    page.mouse.wheel(0, random.randint(1200, 2200))
                    pause(1.2, 2.8)
                cards = page.eval_on_selector_all(
                    'a[href*="/marketplace/item/"]',
                    """els => els.map(a => ({
                        href: a.href,
                        text: a.innerText,
                        img: (a.querySelector('img') || {}).src || ""
                    }))""")
            except Exception as e:
                print(f"recherche échouée ({e.__class__.__name__}): {url}")
                continue
            for c in cards:
                m = re.search(r"/marketplace/item/(\d+)", c["href"])
                if not m:
                    continue
                iid = m.group(1)
                if iid in items or iid in deja:
                    continue
                lines = [l.strip() for l in c["text"].split("\n") if l.strip()]
                prix = next((l for l in lines if "$" in l), "")
                items[iid] = {
                    "id": iid,
                    "url": f"https://www.facebook.com/marketplace/item/{iid}",
                    "prix": prix,
                    "carte": lines[:5],
                    "image": c["img"],
                    "extrait": "",
                }
            print(f"{len(items)} items cumulés après {url[:70]}...")
            pause(2, 5)

        # Visiter quelques fiches pour enrichir (description = superficie, chambres...)
        for it in list(items.values())[:MAX_DETAIL_VISITS]:
            try:
                page.goto(it["url"], wait_until="domcontentloaded", timeout=45000)
                pause(2.5, 5)
                try:
                    page.get_by_text("Voir plus", exact=False).first.click(timeout=2000)
                    pause(0.5, 1.2)
                except Exception:
                    pass
                body = page.evaluate("document.body.innerText")
                body = re.sub(r"\n{2,}", "\n", body)
                start = body.find(it["prix"][:6]) if it["prix"] else 0
                it["extrait"] = body[max(0, start):max(0, start) + 1800]
            except Exception as e:
                print(f"fiche {it['id']} : échec ({e.__class__.__name__})")
        ctx.close()

    out = {"scraped_at": time.strftime("%Y-%m-%d %H:%M"), "items": list(items.values())}
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"OK : {OUT} ({len(items)} items, {min(len(items), MAX_DETAIL_VISITS)} fiches enrichies)")

if __name__ == "__main__":
    main()
