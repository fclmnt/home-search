import json, re, csv

existing_links = set()
with open('annonces.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        existing_links.add(row['lien'].strip())

d = json.load(open('marketplace-raw.json'))
items = d['items']

candidates = []
for it in items:
    url = it.get('url', '')
    if url in existing_links:
        continue
    carte = it.get('carte', [])
    extrait = it.get('extrait', '')
    combined = ' '.join(carte)

    m = re.search(r'CA\$([\d,]+)', combined)
    if not m:
        continue
    price = int(m.group(1).replace(',', ''))
    if price < 1900 or price > 2400:
        continue

    bedm = re.search(r'(\d+)\s*(?:Beds|Bed|chambres|chambre)', combined, re.I)
    beds = int(bedm.group(1)) if bedm else None
    if beds is not None and beds < 2:
        continue

    # Only Montréal city (exclude clearly off-target suburbs)
    loc_line = carte[-1] if carte else ''
    excluded_cities = ['Laval', 'Longueuil', 'Brossard', 'Boucherville', 'Charlemagne',
                        'Otterburn Park', 'Salaberry-de-Valleyfield', 'Piedmont',
                        'Vaudreuil-Dorion', 'Mascouche', 'Ste-Thérèse', "Ste-Sophie",
                        'Hampstead', 'Westmount', 'Delson', 'Mirabel', 'Dollard-des Ormeaux',
                        'Montréal-Est']
    if any(c.lower() in loc_line.lower() for c in excluded_cities):
        continue

    candidates.append({
        'url': url, 'price': price, 'beds': beds, 'carte': carte,
        'extrait': extrait,
    })

print('candidates:', len(candidates))
with open('_mp_candidates_20260806.json', 'w') as f:
    json.dump(candidates, f, ensure_ascii=False, indent=1)
