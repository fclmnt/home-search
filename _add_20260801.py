# -*- coding: utf-8 -*-
import csv

PATH = 'annonces.csv'

with open(PATH, newline='', encoding='utf-8') as f:
    rows = list(csv.reader(f))

header = rows[0]
data = rows[1:]

# Mark old NOUVEAU as vu
for r in data:
    if r[1] == 'NOUVEAU':
        r[1] = 'vu'

new_row = [
    '2026-08-01', 'NOUVEAU',
    "3 chambres fermées, 1000 pi², grande cour arrière privée - rue Cuvillier (Hochelaga, 12 min métro Joliette)",
    'Hochelaga-Maisonneuve',
    'Rue Cuvillier, Montréal, QC H1W 3A8',
    '2010', '1000', '3', 'non', 'Joliette', 'verte', '12',
    'Kijiji',
    'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/3-bedroom-with-backyard-in-hochelaga/1741114311',
    '7',
    "Grande cour arrière privée (pas de balcon), animaux acceptés, laveuse/sécheuse et lave-vaisselle inclus, internet inclus, plafonds hauts, dispo 1er septembre 2026 (entrée hâtive possible dès le 21 août), bail 1 an requis",
    ''
]

data.append(new_row)

def sort_key(r):
    is_new = 0 if r[1] == 'NOUVEAU' else 1
    try:
        score = -int(r[14])
    except (ValueError, IndexError):
        score = 0
    return (is_new, score)

data.sort(key=sort_key)

with open(PATH, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(data)

print('Done. Total rows:', len(data))
print('NOUVEAU count:', sum(1 for r in data if r[1] == 'NOUVEAU'))
