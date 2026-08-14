import json, csv, re

with open('marketplace-raw.json') as f:
    data = json.load(f)
items = data['items']

existing_links = set()
with open('annonces.csv') as f:
    r = csv.DictReader(f)
    for row in r:
        existing_links.add(row['lien'])

EXCLUDE_STATIONS = ['radisson', 'viau', 'assomption', 'cadillac', 'langelier', 'honoré-beaugrand', 'honore-beaugrand', 'mercier']

candidates = []
for it in items:
    url = it['url']
    if url in existing_links:
        continue
    prix_str = it.get('prix', '')
    m = re.search(r'CA(\d[\d,]*)', prix_str.replace('$', ''))
    if not m:
        continue
    prix = int(m.group(1).replace(',', ''))
    if prix < 1900 or prix > 2400:
        continue
    extrait = it.get('extrait', '')
    carte = it.get('carte', [])
    text = (extrait + ' ' + ' '.join(carte)).lower()
    if any(s in text for s in EXCLUDE_STATIONS):
        continue
    bed_m = re.search(r'(\d+)\s*beds?', text)
    bedrooms = int(bed_m.group(1)) if bed_m else None
    candidates.append({
        'url': url,
        'prix': prix,
        'carte': carte,
        'extrait': extrait[:800],
        'image': it.get('image', ''),
        'bedrooms_guess': bedrooms,
    })

print(len(candidates))
with open('_candidates_20260814_2.json', 'w') as f:
    json.dump(candidates, f, ensure_ascii=False, indent=2)
