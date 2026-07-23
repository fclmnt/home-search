import json

d = json.load(open('marketplace-raw.json'))
items = d['items']
excl_city = ['Longueuil', 'Laval', 'Brossard', 'Candiac', 'Repentigny', 'Blainville',
             'Napierville', 'Bois-des-Filion', 'Delson', 'Montréal-Ouest', 'Ste-Marthe',
             'Ste-Sophie', 'Dollard', 'Terrebonne', 'Mascouche', 'Boucherville', 'Chambly',
             'St-Jean', 'Varennes', 'Vaudreuil', 'Rosemère', 'Boisbriand', 'Mirabel',
             'Ste-Julienne', "L'Assomption", 'Ste-Catherine', 'St-Hyacinthe', 'St-Lin',
             'St-Constant', 'Ile-Perrot', "L'Ile-Perrot", 'Pincourt', 'Beloeil', 'McMasterville',
             'St-Bruno', 'Mercier ']

count = 0
for i, it in enumerate(items):
    carte = it.get('carte', [])
    carte_str = str(carte)
    if any(e in carte_str for e in excl_city):
        continue
    prix = it.get('prix', '')
    loc = carte[2] if len(carte) > 2 else ''
    titre = carte[1] if len(carte) > 1 else ''
    print(f"{i} | {prix} | {titre} | {loc}")
    count += 1
print('TOTAL candidates (non-excluded cities):', count)
