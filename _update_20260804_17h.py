import csv

path = 'annonces.csv'
with open(path, encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
data = rows[1:]

for r in data:
    if r[1] == 'NOUVEAU':
        r[1] = 'vu'

new_rows = [
    ['2026-08-04', 'NOUVEAU',
     '4½ rénové, 2 chambres, balcon privé, 1000 pi² - boulevard Rosemont',
     'Rosemont-La Petite-Patrie',
     '2041, Boulevard Rosemont, Montréal',
     '2000', '1000', '2', 'oui', 'Rosemont (estimé)', 'orange', '8 (estimé)',
     'DuProprio',
     'https://duproprio.com/fr/location/montreal/rosemont-la-petite-patrie/4-1-2-a-louer/hab-2041-boulevard-rosemont-1123132',
     '7',
     "2e étage, cuisine à aire ouverte rénovée, climatisation murale, électroménagers en option (frais additionnels), aucun animal accepté, quartier dynamique et convivial (épiceries/restos/bars/parcs à pied), disponible immédiatement, distance métro Rosemont estimée (non confirmée par l'annonce)",
     ''],
    ['2026-08-04', 'NOUVEAU',
     '5½ rénové climatisé, 3 chambres, 930 pi² - Promenade Masson',
     'Rosemont-La Petite-Patrie',
     'n/d (secteur Promenade Masson, Montréal, QC H1Y 1W9)',
     '1950', '930', '3', 'n/d', 'Beaubien (estimé)', 'orange', '10 (estimé)',
     'Kijiji',
     'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/5-1-2-renove-rosemont-petite-patrie/1736299730',
     '6',
     "Entièrement rénové, climatisation incluse, bail 1 an, animaux limités, situé sur/près Promenade Masson (commerces, cafés, boulangeries à pied), proche parcs Beaubien et Baldwin, balcon non précisé dans l'annonce, distance métro estimée (adresse exacte non indiquée)",
     ''],
]

data.extend(new_rows)

def sort_key(r):
    status_rank = 0 if r[1] == 'NOUVEAU' else 1
    try:
        score = -int(r[14])
    except ValueError:
        score = 0
    return (status_rank, score)

data.sort(key=sort_key)

with open(path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(header)
    writer.writerows(data)

print('done, total rows:', len(data))
