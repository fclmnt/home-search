import csv

FIELDS = ["date_ajout","statut","titre","quartier","adresse","prix","superficie_pi2",
          "chambres","balcon","station_metro","ligne_metro","minutes_a_pied","site",
          "lien","score","notes","photo"]

with open('annonces.csv', newline='', encoding='utf-8') as f:
    r = csv.DictReader(f)
    rows = list(r)

for row in rows:
    if row['statut'] == 'NOUVEAU':
        row['statut'] = 'vu'

new_row = {
    "date_ajout": "2026-08-19",
    "statut": "NOUVEAU",
    "titre": "5½ rénové (2 chambres), garde-robes walk-in - secteur Villeray, à 5 min du métro Jarry",
    "quartier": "Villeray",
    "adresse": "n/d (Montréal, QC H2R 2P3)",
    "prix": "1900",
    "superficie_pi2": "n/d",
    "chambres": "2",
    "balcon": "non",
    "station_metro": "Jarry",
    "ligne_metro": "orange",
    "minutes_a_pied": "5",
    "site": "Marketplace",
    "lien": "https://www.facebook.com/marketplace/item/1318066247058264",
    "score": "3",
    "notes": "Entièrement rénové (cuisine avec îlot, planchers refaits), chambre principale avec walk-in, 2e chambre avec grand garde-robe, thermopompe, porte-patio vers cour arrière (pas de balcon), à distance de marche du métro Jarry et du marché Jean-Talon, références demandées, aucun animal, disponible 1er oct. 2026, bail 1 an. Lien Facebook (connexion requise).",
    "photo": "",
}
rows.append(new_row)

def sort_key(row):
    is_new = 0 if row['statut'] == 'NOUVEAU' else 1
    try:
        score = -int(row['score'])
    except (ValueError, KeyError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    for row in rows:
        w.writerow(row)

print("Total rows:", len(rows))
print("NOUVEAU:", sum(1 for r in rows if r['statut'] == 'NOUVEAU'))
