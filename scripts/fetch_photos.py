#!/usr/bin/env python3
"""Remplit la colonne `photo` de annonces.csv (og:image de chaque annonce)."""
import csv
import html
import os
import re
import urllib.request

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE, "annonces.csv")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

OG_RE = re.compile(
    r'<meta[^>]+(?:property|name)=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']'
    r'|<meta[^>]+content=["\']([^"\']+)["\'][^>]+(?:property|name)=["\']og:image["\']',
    re.IGNORECASE)

def og_image(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "fr-CA,fr;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            page = resp.read(1_500_000).decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  erreur ({e.__class__.__name__}): {url}")
        return ""
    m = OG_RE.search(page)
    if m:
        return html.unescape(m.group(1) or m.group(2) or "")
    return ""

def main():
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    if "photo" not in fields:
        fields = fields + ["photo"]

    filled = 0
    for r in rows:
        r.setdefault("photo", "")
        if r["photo"].strip() or not r["lien"].startswith("http"):
            continue
        r["photo"] = og_image(r["lien"])
        if r["photo"]:
            filled += 1

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    missing = sum(1 for r in rows if not r["photo"].strip())
    print(f"{filled} photos récupérées, {missing} sans photo, {len(rows)} annonces")

if __name__ == "__main__":
    main()
