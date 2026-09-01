import json, csv

d = json.load(open('marketplace-raw.json'))
items = d['items']

with open('annonces.csv') as f:
    rows = list(csv.DictReader(f))
existing_links = set(r['lien'] for r in rows)

keywords = ['hochelaga','maisonneuve','prefontaine','préfontaine','joliette','pie-ix','pie ix',
            'rosemont','petite-patrie','petite patrie','beaubien','jean-talon','jean talon',
            'plateau','mont-royal','mont royal','laurier','sherbrooke',
            'villeray','jarry','castelnau']

candidates = []
for it in items:
    if it['url'] in existing_links:
        continue
    text = (' '.join(it.get('carte', [])) + ' ' + it.get('extrait', '')).lower()
    if any(k in text for k in keywords):
        candidates.append(it)

print('new candidates in target areas:', len(candidates))
for it in candidates:
    print('---')
    print(it['url'], it['prix'])
    print(it['carte'])
