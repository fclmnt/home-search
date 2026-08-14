import json, re, csv

d = json.load(open('marketplace-raw.json'))
items = d['items']

existing_links = set()
with open('annonces.csv') as f:
    r = csv.DictReader(f)
    for row in r:
        existing_links.add(row['lien'].strip())

excluded_stations = ['viau', 'assomption', 'cadillac', 'langelier', 'radisson', 'honoré-beaugrand', 'honore-beaugrand', 'mercier']

candidates = []
for it in items:
    url = it.get('url', '')
    if url in existing_links:
        continue
    carte = it.get('carte', [])
    extrait = it.get('extrait', '')
    prix_raw = it.get('prix', '')
    m = re.search(r'CA\$([\d,]+)', prix_raw)
    if not m:
        continue
    price = int(m.group(1).replace(',', ''))
    if price < 1900 or price > 2400:
        continue
    full_text = extrait.lower()
    if 'rentals' not in full_text and 'month' not in prix_raw.lower():
        continue
    bed_m = re.search(r'(\d+)\s*beds?', full_text)
    beds = int(bed_m.group(1)) if bed_m else None
    if beds is not None and beds < 2:
        continue
    if any(st in full_text for st in excluded_stations):
        continue
    candidates.append({'id': it['id'], 'url': url, 'price': price, 'beds': beds, 'carte': carte, 'extrait_snip': extrait[:600], 'image': it.get('image','')})

print(len(candidates))
for c in candidates:
    print('====', c['id'], c['price'], c['beds'])
    print(c['carte'])
    print(c['extrait_snip'][:500])
    print()

with open('_candidates_20260814.json', 'w') as f:
    json.dump(candidates, f, ensure_ascii=False, indent=2)
