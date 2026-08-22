import json, re, csv

d = json.load(open('marketplace-raw.json'))
items = {it['url']: it for it in d.get('items', [])}

existing_links = set()
with open('annonces.csv', encoding='utf-8') as f:
    r = csv.DictReader(f)
    for row in r:
        existing_links.add(row['lien'].strip())

exclude_metro = ['viau','assomption','cadillac','langelier','radisson','honore-beaugrand','mercier']
target_kw = ['hochelaga','maisonneuve','rosemont','petite-patrie','petite italie','petite-italie',
             'villeray','plateau','mile end','mile-end','centre-sud',
             'prefontaine','joliette','pie-ix','pie ix','beaubien','jean-talon','jean talon',
             'mont-royal','mont royal','laurier','sherbrooke','jarry','castelnau']

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
    extrait = it.get('extrait', '')
    if not extrait.strip():
        continue
    text = norm((' '.join(it.get('carte', [])) + ' ' + extrait).lower())
    if any(k in text for k in exclude_metro):
        continue
    if not any(norm(k) in text for k in target_kw):
        continue
    count += 1
    print('=' * 20, url, prix)
    print(extrait[:600].replace('\n', ' | '))
    print()
print('TOTAL', count)
