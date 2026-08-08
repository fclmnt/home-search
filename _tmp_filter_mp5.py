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

candidates = []
for it in items:
    if it['url'] in existing_links:
        continue
    price = parse_price(it.get('prix', ''))
    carte = it.get('carte', [])
    text = ' | '.join(carte) if isinstance(carte, list) else str(carte)
    if price is None or price < 1900 or price > 2400:
        continue
    candidates.append((it['id'], it['url'], price, text[:200]))

print('new price-filtered candidates:', len(candidates))
for c in candidates:
    print(c)
