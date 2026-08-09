import json, re, csv

d = json.load(open('marketplace-raw.json'))
items = d['items']

existing_links = set()
with open('annonces.csv') as f:
    r = csv.DictReader(f)
    for row in r:
        existing_links.add(row['lien'].strip())

candidates = []
for it in items:
    url = it.get('url', '').strip()
    if url in existing_links:
        continue
    carte = it.get('carte', [])
    text = ' | '.join(carte)
    m = re.search(r'CA\$([\d,]+)', text)
    if not m:
        continue
    price = int(m.group(1).replace(',', ''))
    if price < 1900 or price > 2400:
        continue
    if 'Montréal' not in text and 'Montreal' not in text:
        continue
    if 'Apartment' not in text and 'Condo' not in text:
        continue
    candidates.append((url, price, text, it.get('extrait', ''), it.get('image', '')))

print(len(candidates))
for c in candidates:
    print('---')
    print(c[0], c[1])
    print(c[2])
