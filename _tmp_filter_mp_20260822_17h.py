import json, csv, re

with open('marketplace-raw.json') as f:
    data = json.load(f)
items = data.get('items', [])

existing_links = set()
with open('annonces.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        existing_links.add(row['lien'])

neighborhood_kw = ['hochelaga','maisonneuve','rosemont','petite-patrie','petite patrie','plateau','villeray','mile-end','mile end','saint-michel','st-michel']
exclude_kw = ['mercier-est','mercier est',' viau','assomption','cadillac','langelier','radisson','honore-beaugrand','honoré-beaugrand','westmount','carignan','griffintown','ville-marie','verdun','lasalle','lachine','longueuil','laval','brossard','ndg','notre-dame-de-grace','pointe-claire','saint-leonard','st-leonard','anjou','montreal-nord','ahuntsic','outremont','cote-des-neiges','côte-des-neiges','dorval','kirkland','ile-des-soeurs','nuns island','beaconsfield']

candidates = []
for it in items:
    text = (' '.join(it.get('carte',[])) + ' ' + it.get('extrait','')).lower()
    if it['url'] in existing_links:
        continue
    if any(k in text for k in exclude_kw):
        continue
    if any(k in text for k in neighborhood_kw):
        candidates.append(it)

print('total items:', len(items))
print('candidates after filter:', len(candidates))
for c in candidates:
    print('---')
    print(c['url'])
    print(c.get('carte'))
    print(c.get('extrait','')[:500])
