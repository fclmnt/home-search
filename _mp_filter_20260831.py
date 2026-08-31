import json, re

with open('marketplace-raw.json') as f:
    data = json.load(f)
items = data['items']

keywords = ['Hochelaga','Maisonneuve','Rosemont','Petite-Patrie','Petite Patrie','Plateau','Villeray',
            'Préfontaine','Prefontaine','Joliette','Pie-IX','Pie IX','Beaubien','Jean-Talon','Jean Talon',
            'Mont-Royal','Mont Royal','Laurier','Sherbrooke','Jarry','Castelnau','Frontenac','Papineau',
            'Masson','Ontario','H1V','H1W','H1X','H1Y','H1Z','H2H','H2G','H2J','H2K','H2L','H2S','H2T','H2R']

hits = []
for it in items:
    carte = it.get('carte') or []
    extrait = it.get('extrait') or ''
    full = ' '.join(carte) + ' ' + extrait
    for kw in keywords:
        if kw in full:
            hits.append((it.get('url'), kw, carte, extrait[:400]))
            break

print(len(hits))
for h in hits:
    print(h[0])
    print('kw:', h[1])
    print('carte:', h[2])
    print('extrait:', h[3])
    print('---')
