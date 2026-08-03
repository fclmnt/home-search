import csv

path = 'annonces.csv'
with open(path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

idx = {name: i for i, name in enumerate(header)}

# 1. flip old NOUVEAU -> vu
for r in rows:
    if r[idx['statut']] == 'NOUVEAU':
        r[idx['statut']] = 'vu'

new_rows = [
    [
        '2026-08-03', 'NOUVEAU',
        "5½ rénové, grand balcon-terrasse - rue Joliette (Rosemont/Hochelaga, métro Joliette)",
        'Rosemont-La Petite-Patrie (frontière Hochelaga-Maisonneuve)',
        '4349, Rue Joliette, Montréal',
        '2100', '919', '2', 'oui', 'Joliette', 'verte', '8',
        'Centris', 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/28184451',
        '8',
        "Semi-meublé, cuisine et plancher récemment rénovés, beaucoup de rangement, douche séparée, chats acceptés (pas de chiens), non-fumeurs, disponible 1er septembre 2026.",
        ''
    ],
    [
        '2026-08-03', 'NOUVEAU',
        "Spacieux 5½ (3 chambres, 2 salles de bain), garage - 20e Avenue (Rosemont, secteur Saint-Michel)",
        'Rosemont-La Petite-Patrie (secteur Saint-Michel)',
        '6940, 20e Avenue, app. 201, Montréal',
        '2300', '1186', '3', 'oui', 'Saint-Michel', 'bleue', '5',
        'Centris', 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/17444358',
        '9',
        "Construit en 2016, cuisine ouverte équipée, garage intérieur + casier (150$/mois en sus), aucun animal ni fumeur accepté, disponible 10 jours après acceptation de la promesse de location.",
        ''
    ],
    [
        '2026-08-03', 'NOUVEAU',
        "Grand appartement 3 chambres (8 pièces) - rue Cuvillier (Hochelaga-Maisonneuve, près métro Joliette)",
        'Hochelaga-Maisonneuve',
        '2650, Rue Cuvillier, Montréal',
        '2000', 'n/d', '3', 'n/d', 'Joliette', 'verte', '12',
        'Centris', 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/11424915',
        '5',
        "Immeuble de 1931, unité de 8 pièces / 3 chambres, aire de vie ouverte et lumineuse, superficie exacte et présence d'un balcon non précisées dans l'annonce, disponible 1er juillet 2026, distance au métro à la limite maximale acceptée (12 min).",
        ''
    ],
    [
        '2026-08-03', 'NOUVEAU',
        "Grand 7½ (3 chambres), balcon - rue Chambord, cœur du Plateau-Mont-Royal (près métro Mont-Royal)",
        'Le Plateau-Mont-Royal',
        'n/d (rue Chambord, secteur Plateau-Mont-Royal, Montréal, QC H2J)',
        '2150', '1100', '3', 'oui', 'Mont-Royal', 'orange', '9',
        'Kijiji', 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-appartement-7-1-2-en-plein-coeur-du-plateau-mont-royal/1741462514',
        '9',
        "2e étage, hangar de rangement, donne sur ruelle verte, proche parc Lafontaine et avenue du Mont-Royal (commerces/cafés), animaux non acceptés, bail 1 an et vérification de crédit requis, disponible 1er août 2026.",
        ''
    ],
]

rows.extend(new_rows)

def sort_key(r):
    is_new = 0 if r[idx['statut']] == 'NOUVEAU' else 1
    try:
        score = -float(r[idx['score']])
    except ValueError:
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(header)
    writer.writerows(rows)

print('total rows:', len(rows))
print('NOUVEAU count:', sum(1 for r in rows if r[idx['statut']] == 'NOUVEAU'))
