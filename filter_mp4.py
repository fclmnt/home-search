import json
d = json.load(open('marketplace-raw.json'))
items = d['items']
excl_city = ['Longueuil','Laval','Brossard','Candiac','Repentigny','Blainville','Napierville','Ste-Julienne','Bois-des-Filion','Delson','Montréal-Ouest','Anjou']
for i, it in enumerate(items):
    carte = it.get('carte', [])
    if any(e in str(carte) for e in excl_city):
        continue
    extrait = it.get('extrait','') or ''
    lines = extrait.split('\n')
    addr = lines[2] if len(lines) > 2 else ''
    print(i, '|', addr, '|', it.get('url'))
