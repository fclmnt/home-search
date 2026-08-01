import csv

path = 'annonces.csv'
with open(path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
data = rows[1:]

# flip old NOUVEAU to vu
for row in data:
    if row[1] == 'NOUVEAU':
        row[1] = 'vu'

new_rows = [
    [
        '2026-08-01', 'NOUVEAU',
        '4½ avec jardin privatif, 2 chambres, balcon et terrasse - rue Bourbonnière (Hochelaga, 5 min métro Joliette/Pie-IX)',
        'Hochelaga-Maisonneuve',
        '1693 Avenue Bourbonnière, Montréal, QC H1W 3N5',
        '1990', '900', '2', 'oui', 'Joliette', 'verte', '5', 'Kijiji',
        'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/4-1-2-avec-jardin-privatif-disponible-maintenant/1741230362',
        '8',
        "Rez-de-chaussée avec jardin privé exclusif, 1 stationnement inclus, laveuse-sécheuse, bain tourbillon et plancher chauffant à la salle de bain, électroménagers neufs, thermopompe murale, non-fumeur, aucun animal, bail 1 an, dispo 1er août 2026, à quelques minutes des métros Joliette et Pie-IX",
        ''
    ],
    [
        '2026-08-01', 'NOUVEAU',
        'Grand 6½ rénové, 3 chambres, 2 balcons - Villeray (métro Jarry, 3 min à pied)',
        'Villeray',
        'Montréal, QC H2R 2E8',
        '2400', '1250', '3', 'oui', 'Jarry', 'orange', '3', 'Kijiji',
        'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-6-1-2-villeray-metro-jarry/1741363911',
        '9',
        "2e étage d'un triplex tranquille, double salon/salle à manger, cuisine avec îlot central, laveuse-sécheuse incluse, électroménagers inclus (locataire paie électricité/chauffage/internet), stationnement rue avec vignette possible, petit animal calme accepté sous conditions, non-fumeur, proche marché Jean-Talon et parc Jarry, dispo 1er août 2026",
        ''
    ],
    [
        '2026-08-01', 'NOUVEAU',
        '3 chambres fermées, 1030 pi² - rue Joliette (Hochelaga-Maisonneuve, proche métro Joliette)',
        'Hochelaga-Maisonneuve',
        '1679 Rue Joliette, Montréal, QC',
        '2200', '1030', '3', 'n/d', 'Joliette', 'verte', '8', 'Centris',
        'https://www.centris.ca/en/condos-apartments~for-rent~montreal-mercier-hochelaga-maisonneuve/19180102',
        '7',
        "Construit en 1935, Walk Score 98, proximité métro, parc, piste cyclable, garderie et école secondaire, animaux acceptés sous conditions, non-fumeur, dispo 1er août 2026, balcon non mentionné dans la fiche, station de métro estimée à partir du nom de la rue",
        ''
    ],
]

data.extend(new_rows)

with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print('done, total rows:', len(data))
