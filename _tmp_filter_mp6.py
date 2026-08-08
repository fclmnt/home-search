import json, re, csv

with open('marketplace-raw.json') as f:
    d = json.load(f)
items = d['items']

with open('annonces.csv') as f:
    existing_links = set(row['lien'] for row in csv.DictReader(f))

def parse_price(s):
    if not s:
        return None
    m = re.search(r'CA\$([\d,]+)', s)
    if m:
        return int(m.group(1).replace(',', ''))
    return None

def parse_beds(carte_text):
    m = re.search(r'(\d+)\s*Beds', carte_text)
    if m:
        return int(m.group(1))
    m = re.search(r'(\d+)\s*chambres?', carte_text)
    if m:
        return int(m.group(1))
    m = re.search(r'(\d+)\s*habitaciones', carte_text)
    if m:
        return int(m.group(1))
    return None

by_id = {}
for it in items:
    by_id[it['id']] = it

candidates = []
for it in items:
    if it['url'] in existing_links:
        continue
    price = parse_price(it.get('prix', ''))
    carte = it.get('carte', [])
    carte_text = ' | '.join(carte) if isinstance(carte, list) else str(carte)
    if price is None or price < 1900 or price > 2400:
        continue
    if 'Montréal, QC' not in carte_text:
        continue
    beds = parse_beds(carte_text)
    if beds is None or beds < 2:
        continue
    candidates.append({
        'id': it['id'],
        'url': it['url'],
        'price': price,
        'beds': beds,
        'carte': carte_text,
    })

print('candidates montreal + beds>=2:', len(candidates))
for c in candidates:
    print(c['id'], c['price'], c['beds'], '|', c['carte'][:150])
