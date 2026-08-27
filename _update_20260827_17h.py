import csv

with open('annonces.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
data = rows[1:]

for row in data:
    if row[1] == 'NOUVEAU':
        row[1] = 'vu'

new_rows = [
    [
        '2026-08-27', 'NOUVEAU',
        "5½ (3 chambres fermées), 2 balcons - avenue Gascon (Hochelaga), à 10 min des métros Préfontaine/Frontenac",
        'Hochelaga-Maisonneuve',
        'n/d (avenue Gascon, Montréal, QC)',
        '2100', 'n/d', '3', 'oui',
        'Préfontaine / Frontenac', 'verte', '10',
        'Marketplace',
        'https://www.facebook.com/marketplace/item/1034425322444723',
        '7',
        "3e étage d'un immeuble de 6 logements, balcon avant et balcon arrière, électroménagers inclus (frigo, four, laveuse-sécheuse, lave-vaisselle), climatisation, stationnement gratuit dans la rue, disponible 1er juillet. Lien Facebook (connexion requise).",
        '',
    ],
    [
        '2026-08-27', 'NOUVEAU',
        "5½ meublé, Plateau-Mont-Royal (Marketplace), disponible 10 juin, bail minimum 1 an",
        'Le Plateau-Mont-Royal',
        'n/d (Montréal, QC)',
        '2100', 'n/d', '2 (estimé)', 'n/d',
        'n/d', 'n/d', 'n/d',
        'Marketplace',
        'https://www.facebook.com/marketplace/item/2129210164276639',
        '2',
        "Annonce titre seulement (meublé, deux prix affichés selon la durée du bail : 2100$ et 2500$), aucune adresse ni description détaillée disponible via le scraper. Nombre de chambres estimé à 2 selon la nomenclature standard d'un 5½, à confirmer. Lien Facebook (connexion requise) pour plus de détails.",
        '',
    ],
]

data.extend(new_rows)

def sort_key(row):
    statut = row[1]
    try:
        score = int(row[14])
    except ValueError:
        score = 0
    return (0 if statut == 'NOUVEAU' else 1, -score)

data.sort(key=sort_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(header)
    writer.writerows(data)

print('done', len(data))
