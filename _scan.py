import json, re

d = json.load(open('marketplace-raw.json'))
items = {it['id']: it for it in d['items']}

banlieue = ['Terrebonne','Longueuil','Laval','Mirabel','Piedmont','Salaberry-de-Valleyfield','Ste-Therese','St-Jerome','Sainte-Therese','Saint-Jerome']

keywords_quartier = ['Hochelaga','Maisonneuve','Rosemont','Petite-Patrie','Plateau','Villeray','Mile-End','Mile End','Marche Jean-Talon','Jean-Talon']
keywords_metro = ['metro','Prefontaine','Joliette','Pie-IX','Rosemont','Beaubien','Jean-Talon','Mont-Royal','Laurier','Sherbrooke','Jarry','De Castelnau','Castelnau','Papineau','Frontenac','Viau','Assomption','Cadillac','Langelier','Radisson','Honore-Beaugrand','Mercier']

import unicodedata
def norm(s):
    return unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode().lower()

results = []
for it in items.values():
    carte = it.get('carte', [])
    loc = carte[-1] if carte else ''
    if any(norm(b) in norm(loc) for b in banlieue):
        continue
    prix_str = it.get('prix','')
    m = re.search(r'[\d,]+', prix_str)
    if not m:
        continue
    prix = int(m.group().replace(',',''))
    if prix < 1900 or prix > 2400:
        continue
    extrait = it.get('extrait','')
    hay = norm(extrait + ' ' + ' '.join(carte))
    found_q = [k for k in keywords_quartier if norm(k) in hay]
    found_m = [k for k in keywords_metro if norm(k) in hay]
    if found_q or found_m:
        results.append((it['id'], prix, carte[1] if len(carte)>1 else '', found_q, found_m, it['url']))

print(len(results))
for r in results:
    print(r)
