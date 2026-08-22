import json, re, csv

d = json.load(open('marketplace-raw.json'))
items = {it['url']: it for it in d.get('items', [])}

existing_links = set()
with open('annonces.csv', encoding='utf-8') as f:
    r = csv.DictReader(f)
    for row in r:
        existing_links.add(row['lien'].strip())

exclude_metro = ['viau','assomption','cadillac','langelier','radisson','honore-beaugrand','mercier']

def norm(s):
    return (s.replace('é','e').replace('è','e').replace('à','a').replace('û','u')
             .replace('ô','o').replace('ê','e').replace('î','i').replace('ç','c'))

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
    text = norm((' '.join(it.get('carte', [])) + ' ' + it.get('extrait', '')).lower())
    bed_m = re.search(r'(\d+)\s*bed', text)
    beds = int(bed_m.group(1)) if bed_m else None
    if beds is None or beds < 2:
        continue
    if any(k in text for k in exclude_metro):
        continue
    count += 1
    print('=' * 20, url, prix, beds)
    print(it.get('extrait', '')[:400].replace('\n', ' | '))
print('TOTAL', count)
