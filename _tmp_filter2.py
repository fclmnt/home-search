import json
import re

d = json.load(open('marketplace-raw.json'))
items = d['items']
excl_city = ['Longueuil', 'Laval', 'Brossard', 'Candiac', 'Repentigny', 'Blainville',
             'Napierville', 'Bois-des-Filion', 'Delson', 'Montréal-Ouest', 'Ste-Marthe',
             'Ste-Sophie', 'Dollard', 'Terrebonne', 'Mascouche', 'Boucherville', 'Chambly',
             'St-Jean', 'Varennes', 'Vaudreuil', 'Rosemère', 'Boisbriand', 'Mirabel',
             'Ste-Julienne', "L'Assomption", 'Ste-Catherine', 'St-Hyacinthe', 'St-Lin',
             'St-Constant', 'Ile-Perrot', "L'Ile-Perrot", 'Pincourt', 'Beloeil', 'McMasterville',
             'St-Bruno', 'Hampstead', 'St-Roch', "St-Jérôme", 'Pointe-Claire', 'Montréal-Est',
             'Pointe-aux-Trembles', 'Anjou']

target_kw = ['Hochelaga', 'Maisonneuve', 'Rosemont', 'Petite-Patrie', 'Plateau', 'Villeray',
             'Mont-Royal', 'Ontario', 'Masson', 'Beaubien', 'Jean-Talon', 'Pie-IX', 'Pie IX',
             'Préfontaine', 'Joliette', 'Sherbrooke', 'Jarry', 'De Castelnau', 'Castelnau',
             'Laurier', 'Rachel', 'Fullum', 'Iberville', 'Cartier', 'Papineau', 'Marquette',
             "d'Iberville", 'Bourbonnière', 'Aird', 'Létourneux', 'Moreau', 'Valois', 'Nicolet',
             'Coupal', 'Adam', 'Ontario', "Ste-Catherine", 'De Lorimier', 'Chambord',
             'Boyer', 'Garnier', 'Fabre', 'De Bordeaux', 'Bordeaux', '16e', '17e', '18e', '19e',
             '1ere avenue', '2e avenue', '3e avenue', 'Marché Maisonneuve', 'Parc Lafontaine']

for i, it in enumerate(items):
    carte = it.get('carte', [])
    carte_str = str(carte)
    if any(e in carte_str for e in excl_city):
        continue
    extrait = it.get('extrait', '') or ''
    hit = [k for k in target_kw if k.lower() in extrait.lower()]
    if hit:
        prix = it.get('prix', '')
        print(f"=== {i} | {prix} | hits: {hit} | {it.get('url')}")
