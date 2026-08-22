import csv

path = 'annonces.csv'
with open(path, encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
data = rows[1:]

for row in data:
    if row[1] == 'NOUVEAU':
        row[1] = 'vu'

new_rows = [
    [
        '2026-08-22', 'NOUVEAU',
        '5½ meublé, 3 chambres fermées, 1200 pi², terrasse arrière - rue Saint-Dominique (Mile-End/Plateau), à 10 min du métro Rosemont',
        'Le Plateau-Mont-Royal (Mile-End)',
        '5561, Rue Saint-Dominique, Montréal',
        '2000', '1200', '3', 'oui', 'Rosemont', 'orange', '10 (estimé)',
        'DuProprio',
        'https://duproprio.com/fr/location/montreal/le-plateau-mont-royal/5-1-2-a-louer/hab-5561-rue-saint-dominique-1139770',
        '9',
        "Entièrement meublé et équipé (peut être loué non meublé), rez-de-chaussée, belle salle de bain avec laveuse-sécheuse, grand espace ouvert salon/salle à manger avec mur de brique, petite terrasse arrière, WiFi inclus, situé entre Mile-End et Plateau, disponible immédiatement",
        ''
    ],
    [
        '2026-08-22', 'NOUVEAU',
        '5½, 3 chambres fermées, 1100 pi², accès terrasse - rue Saint-Dominique (Mile-End/Plateau), à 10 min du métro Rosemont',
        'Le Plateau-Mont-Royal (Mile-End)',
        '5571, Rue Saint-Dominique, Montréal',
        '2000', '1100', '3', 'oui', 'Rosemont', 'orange', '10 (estimé)',
        'DuProprio',
        'https://duproprio.com/fr/location/montreal/le-plateau-mont-royal/5-1-2-a-louer/hab-5571-rue-saint-dominique-1139764',
        '9',
        "Rez-de-chaussée, 3 chambres lumineuses avec rangement, accès à une petite terrasse pour BBQ + rangement, à quelques pas du boulevard Saint-Laurent, coeur du Mile-End, tous électros inclus, disponible immédiatement",
        ''
    ],
]

data.extend(new_rows)

def sort_key(row):
    is_new = 0 if row[1] == 'NOUVEAU' else 1
    try:
        score = -float(row[14])
    except ValueError:
        score = 0
    return (is_new, score)

data.sort(key=sort_key)

with open(path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(header)
    writer.writerows(data)

print("Done. Total rows:", len(data))
print("NOUVEAU count:", sum(1 for r in data if r[1] == 'NOUVEAU'))
