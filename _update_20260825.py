import csv

path = 'annonces.csv'
with open(path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
data = rows[1:]

for row in data:
    if row[1] == 'NOUVEAU':
        row[1] = 'vu'

new_rows = [
    [
        '2026-08-25', 'NOUVEAU',
        "5 1/2 RDC rénové (2 chambres, 1000 pi²), balcon et terrasse - Hochelaga-Maisonneuve, à 4 min du métro Joliette",
        'Hochelaga-Maisonneuve',
        'n/d (secteur métro Joliette, Montréal, QC H1W 3J3)',
        '1916', '1000', '2', 'oui', 'Joliette', 'verte', '4', 'Kijiji',
        'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/joli-rdc-homa-metrojoliette-5-1-2-cour-thermopompe-1916-mo/1742514974',
        '8',
        "Rez-de-chaussée, balcon avant et terrasse arrière avec accès à la cour, thermopompe (non chauffé), animaux limités acceptés, disponible 1er octobre 2026.",
        '',
    ],
    [
        '2026-08-25', 'NOUVEAU',
        "7 1/2 à rénover (2 chambres fermées + bureau, 1200 pi²), balcons refaits - Hochelaga-Maisonneuve, près du marché Maisonneuve",
        'Hochelaga-Maisonneuve',
        'n/d (près du marché Maisonneuve, Montréal, QC H1V 2R6)',
        '2200', '1200', '2', 'oui', 'Pie-IX (à vérifier, adresse exacte non précisée)', 'verte', '10 (estimé)', 'Kijiji',
        'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/7-1-2-hochelaga-maisonneuve-7-1-2-hochelaga-maisonneuve/1742386416',
        '9',
        "2e étage d'un triplex en rénovation complète, cachet d'origine (murs de brique, planchers bois franc, plafonds 9 pi), balcons refaits à neuf, électroménagers neufs, disponible 1er septembre 2026.",
        '',
    ],
    [
        '2026-08-25', 'NOUVEAU',
        "Grand 5½ (3 chambres) face au métro Pie-IX - Hochelaga-Maisonneuve",
        'Hochelaga-Maisonneuve',
        '2645, Boulevard Pie-IX, Montréal, QC H1V 2E8',
        '2095', 'n/d', '3', 'n/d', 'Pie-IX', 'verte', '1', 'Marketplace',
        'https://www.facebook.com/marketplace/item/1042462432026740',
        '5',
        "Lien Facebook Marketplace (connexion requise). Eau chaude, électroménagers et air climatisé inclus, stationnement 50$/mois en option, internet 50$/mois en option, à quelques secondes à pied du métro Pie-IX.",
        '',
    ],
]

data.extend(new_rows)

def sort_key(row):
    is_new = 0 if row[1] == 'NOUVEAU' else 1
    try:
        score = -int(row[14])
    except (ValueError, IndexError):
        score = 0
    return (is_new, score)

data.sort(key=sort_key)

with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print('Total rows:', len(data))
print('NOUVEAU count:', sum(1 for r in data if r[1] == 'NOUVEAU'))
