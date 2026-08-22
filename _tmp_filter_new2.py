import json, re, csv

d = json.load(open('marketplace-raw.json'))
items = d.get('items', [])

existing_links = set()
with open('annonces.csv', encoding='utf-8') as f:
    r = csv.DictReader(f)
    for row in r:
        existing_links.add(row['lien'].strip())

neighborhood_kw = ['hochelaga','maisonneuve','rosemont','petite-patrie','petite italie',
                    'villeray','plateau','mont-royal','mile end','mile-end','centre-sud','ville-marie']
metro_kw = ['prefontaine','joliette','pie-ix','pie ix','rosemont','beaubien','jean-talon','jean talon',
            'mont-royal','mont royal','laurier','sherbrooke','jarry','castelnau','papineau','fabre',
            'frontenac','de lorimier','lorimier']
exclude_metro = ['viau','assomption','cadillac','langelier','radisson','honore-beaugrand','mercier']

def norm(s):
    return (s.replace('é','e').replace('è','e').replace('à','a').replace('û','u')
             .replace('ô','o').replace('ê','e').replace('î','i').replace('ç','c'))

candidates = []
for it in items:
    url = it.get('url','')
    if url in existing_links:
        continue
    prix_raw = it.get('prix','')
    m = re.search(r'([\d,]+)', prix_raw)
    if not m:
        continue
    prix = int(m.group(1).replace(',',''))
    if prix < 1900 or prix > 2400:
        continue
    text = norm((' '.join(it.get('carte',[])) + ' ' + it.get('extrait','')).lower())
    bed_m = re.search(r'(\d+)\s*bed', text)
    beds = int(bed_m.group(1)) if bed_m else None
    if beds is not None and beds < 2:
        continue
    excl = [k for k in exclude_metro if k in text]
    if excl:
        continue
    nb_hits = [k for k in neighborhood_kw if norm(k) in text]
    metro_hits = [k for k in metro_kw if norm(k) in text]
    candidates.append({
        'url': url,
        'prix': prix,
        'beds': beds,
        'nb_hits': nb_hits,
        'metro_hits': metro_hits,
        'carte': it.get('carte'),
    })

print(len(candidates))
for c in candidates:
    print(c['prix'], c['beds'], c['nb_hits'], c['metro_hits'], c['url'])
