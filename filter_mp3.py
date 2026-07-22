import json, re
d = json.load(open('marketplace-raw.json'))
items = d['items']
excl_city = ['Longueuil','Laval','Brossard','Candiac','Repentigny','Blainville','Napierville','Ste-Julienne','Bois-des-Filion','Delson','Montréal-Ouest','Anjou']
keywords = ['hochelaga','maisonneuve','rosemont','petite-patrie','petite italie','villeray','plateau-mont-royal','plateau mont-royal','le plateau','préfontaine','prefontaine','joliette','pie-ix','beaubien','jean-talon','de castelnau','castelnau']
for i, it in enumerate(items):
    carte = it.get('carte', [])
    if any(e in str(carte) for e in excl_city):
        continue
    extrait = it.get('extrait','') or ''
    text = extrait.lower()
    hits = [k for k in keywords if k in text]
    if hits:
        # print address line (usually line 3)
        lines = extrait.split('\n')
        addr = lines[2] if len(lines) > 2 else ''
        print(i, '|', hits, '|', addr, '|', it.get('url'))
