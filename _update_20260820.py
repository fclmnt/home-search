import csv

fields = ["date_ajout","statut","titre","quartier","adresse","prix","superficie_pi2","chambres","balcon","station_metro","ligne_metro","minutes_a_pied","site","lien","score","notes","photo"]

with open('annonces.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'

new_row = {
    "date_ajout": "2026-08-20",
    "statut": "NOUVEAU",
    "titre": "5½ rénové (3 chambres fermées + salon), 1080 pi², 3 balcons - rue Cartier (Plateau-Mont-Royal, secteur Parc Laurier), près métro Laurier",
    "quartier": "Le Plateau-Mont-Royal",
    "adresse": "5483, Rue Cartier, Montréal, QC H1T 2X7",
    "prix": "2000",
    "superficie_pi2": "1080",
    "chambres": "3",
    "balcon": "oui",
    "station_metro": "Laurier",
    "ligne_metro": "orange",
    "minutes_a_pied": "n/d (estimé ~10 min)",
    "site": "Kijiji",
    "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-5-1-2-plateau-mont-royal/1742059571",
    "score": "8",
    "notes": "2e étage, aire ouverte cuisine/salon, planchers bois franc, laveuse-sécheuse incluse, climatiseur et réfrigérateur fournis, 3 balcons (avant/arrière/latéral), station BIXI à 2 min, animaux acceptés sous conditions, bail 1 an, disponible immédiatement (titre annonce sept. 2026), proche parc Laurier",
    "photo": ""
}
rows.append(new_row)

def sort_key(r):
    is_new = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        score = -float(r['score'])
    except (ValueError, TypeError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

print("done", len(rows), "rows")
