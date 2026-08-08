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

TARGET_STATIONS = ['préfontaine', 'prefontaine', 'joliette', 'pie-ix', 'pie ix',
    'rosemont', 'beaubien', 'jean-talon', 'jean talon',
    'mont-royal', 'mont royal', 'laurier', 'sherbrooke',
    'jarry', 'de castelnau', 'castelnau', 'frontenac', 'beaudry', "d'iberville"]

EXCLUDED_STATIONS = ['viau', 'assomption', "l'assomption", 'cadillac', 'langelier',
    'radisson', 'honoré-beaugrand', 'honore-beaugrand']

def find_stations(text):
    tl = text.lower()
    found = [s for s in TARGET_STATIONS if s in tl]
    excluded = [s for s in EXCLUDED_STATIONS if s in tl]
    return found, excluded

def find_superficie(text):
    m = re.search(r'(\d{3,4})\s*(?:square feet|pi2|pi²|sq ?ft)', text, re.I)
    return int(m.group(1)) if m else None

def find_balcon(text):
    tl = text.lower()
    return any(k in tl for k in ['balcon', 'terrasse'])

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
    found_stations, excluded_stations = find_stations(extrait)
    superficie = find_superficie(extrait)
    balcon = find_balcon(extrait)
    results.append({
        'id': id_, 'url': it['url'], 'price': price, 'beds': beds,
        'superficie': superficie, 'balcon': balcon,
        'stations': found_stations, 'excluded_stations': excluded_stations,
    })

promising = [r for r in results if r['stations'] and not r['excluded_stations']]
print(f'total candidates: {len(results)}, promising (target metro mentioned): {len(promising)}')
for r in promising:
    print(r['id'], r['price'], r['beds'], 'sqft=', r['superficie'], 'balcon=', r['balcon'], 'stations=', r['stations'])
