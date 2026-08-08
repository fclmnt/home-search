import json, re, csv

with open('marketplace-raw.json') as f:
    d = json.load(f)
items = {it['id']: it for it in d['items']}

with open('annonces.csv') as f:
    existing_links = set(row['lien'] for row in csv.DictReader(f))

def parse_price(s):
    m = re.search(r'CA\$([\d,]+)', s or '')
    return int(m.group(1).replace(',', '')) if m else None

def parse_beds(carte_text):
    for pat in [r'(\d+)\s*Beds', r'(\d+)\s*chambres?', r'(\d+)\s*habitaciones']:
        m = re.search(pat, carte_text)
        if m:
            return int(m.group(1))
    return None

TARGET_NEIGHBORHOODS = ['hochelaga', 'maisonneuve', 'rosemont', 'petite-patrie',
    'petite patrie', 'plateau', 'villeray', 'centre-sud', 'centre sud']
EXCLUDED_NEIGHBORHOODS = ['mercier', 'anjou', 'saint-léonard', 'st-léonard',
    'saint leonard', 'rivière-des-prairies', "pointe-aux-trembles", 'montréal-nord',
    'montreal nord', 'lasalle', 'longueuil', 'laval', 'ndg', 'notre-dame-de-grace',
    'notre-dame-de-grâce', 'côte-des-neiges', 'verdun', 'ahuntsic']

def find_kw(text, kws):
    tl = text.lower()
    return [k for k in kws if k in tl]

results = []
for id_, it in items.items():
    if it['url'] in existing_links:
        continue
    carte = it.get('carte', [])
    carte_text = ' | '.join(carte) if isinstance(carte, list) else str(carte)
    price = parse_price(it.get('prix', '') or carte_text)
    if price is None or price < 1900 or price > 2400:
        continue
    if 'Montréal, QC' not in carte_text and 'Montreal' not in carte_text:
        continue
    beds = parse_beds(carte_text)
    if beds is None or beds < 2:
        continue
    extrait = it.get('extrait', '') or ''
    neigh = find_kw(extrait, TARGET_NEIGHBORHOODS)
    excl_neigh = find_kw(extrait, EXCLUDED_NEIGHBORHOODS)
    if neigh and not excl_neigh:
        results.append((id_, it['url'], price, beds, neigh, extrait[:600]))

print(len(results))
for r in results:
    print('====', r[0], r[2], r[3], r[4])
    print(r[5])
    print()
