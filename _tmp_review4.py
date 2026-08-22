import json, re, csv

d = json.load(open('marketplace-raw.json'))
items = {it['url']: it for it in d.get('items', [])}

existing_links = set()
with open('annonces.csv', encoding='utf-8') as f:
    r = csv.DictReader(f)
    for row in r:
        existing_links.add(row['lien'].strip())

count = 0
for url, it in items.items():
    if url in existing_links:
        continue
    prix_raw = it.get('prix', '')
    m = re.search(r'([\d,]+)', prix_raw)
    if not m:
        continue
    prix = int(m.group(1).replace(',', ''))
    if prix < 1900 or prix > 2400:
        continue
    extrait = it.get('extrait', '')
    if extrait.strip():
        continue
    carte = it.get('carte', [])
    # print carte items that look like an address (contain digits) or a city name
    addr_like = [c for c in carte if re.search(r'\d', c) or ',' in c]
    count += 1
    print(prix, carte)
print('TOTAL blank-extrait candidates:', count)
