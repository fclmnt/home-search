import json
d = json.load(open('marketplace-raw.json'))
items = d['items']
excl = ['Longueuil','Laval','Brossard','Candiac','Repentigny','Blainville','Napierville','Ste-Julienne','Bois-des-Filion','Delson','Montréal-Ouest','Anjou']
for i, it in enumerate(items):
    carte = it.get('carte', [])
    if any(e in str(carte) for e in excl):
        continue
    print(i, '|', carte, '|', it.get('url'))
