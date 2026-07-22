import json
d = json.load(open('marketplace-raw.json'))
items = d['items']
excl_city = ['Longueuil','Laval','Brossard','Candiac','Repentigny','Blainville','Napierville','Ste-Julienne','Bois-des-Filion','Delson','Montréal-Ouest','Anjou']
keywords = ['hochelaga','maisonneuve','rosemont','petite-patrie','petite italie','plateau','villeray','jean-talon','beaubien','pie-ix','preville','prefontaine','préfontaine','joliette','mont-royal','laurier','sherbrooke','jarry','castelnau','masson']
for i, it in enumerate(items):
    carte = it.get('carte', [])
    if any(e in str(carte) for e in excl_city):
        continue
    extrait = it.get('extrait','') or ''
    text = (str(carte) + ' ' + extrait).lower()
    if any(k in text for k in keywords):
        print(i, '|', carte, '|', extrait[:150], '|', it.get('url'))
