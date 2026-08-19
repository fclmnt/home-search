import csv

path = "annonces.csv"
with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

for row in rows:
    if row['statut'] == 'NOUVEAU':
        row['statut'] = 'vu'

new_rows = [
    {
        "date_ajout": "2026-08-19",
        "statut": "NOUVEAU",
        "titre": "Nouveau condo 4 1/2 (2 chambres), 1014 pi² - rue Sainte-Catherine Est app. 101 (Hochelaga), à 5 min du métro Préfontaine",
        "quartier": "Hochelaga-Maisonneuve",
        "adresse": "3257, Rue Sainte-Catherine Est, app. 101, Montréal, QC",
        "prix": "2350",
        "superficie_pi2": "1014",
        "chambres": "2",
        "balcon": "n/d",
        "station_metro": "Préfontaine",
        "ligne_metro": "verte",
        "minutes_a_pied": "5",
        "site": "Centris",
        "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/16060283",
        "score": "",
        "notes": "Construction neuve (2026), semi-meublé, 7 pièces au total, chambres au sous-sol, prêt en 5 jours après acceptation du bail, Walk Score 89.",
        "photo": "",
    },
    {
        "date_ajout": "2026-08-19",
        "statut": "NOUVEAU",
        "titre": "5 1/2 rénové (3 chambres), 900 pi² - rue Saint-Hubert (Villeray), à 2 min du métro Jarry",
        "quartier": "Villeray",
        "adresse": "7848, Rue Saint-Hubert, Montréal, QC",
        "prix": "1900",
        "superficie_pi2": "900",
        "chambres": "3",
        "balcon": "n/d",
        "station_metro": "Jarry",
        "ligne_metro": "orange",
        "minutes_a_pied": "2",
        "site": "Centris",
        "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/20306931",
        "score": "",
        "notes": "Récemment rénové (finitions modernes), 2e étage, à deux pas du Marché Jean-Talon et du métro Jarry, prêt en 5 jours après acceptation du bail, Walk Score 97.",
        "photo": "",
    },
    {
        "date_ajout": "2026-08-19",
        "statut": "NOUVEAU",
        "titre": "5 1/2 spacieux (3 chambres) - rue Everett (Villeray), à 2 min du métro Jean-Talon",
        "quartier": "Villeray",
        "adresse": "2709, Rue Everett, Montréal, QC",
        "prix": "1900",
        "superficie_pi2": "n/d",
        "chambres": "3",
        "balcon": "n/d",
        "station_metro": "Jean-Talon",
        "ligne_metro": "orange",
        "minutes_a_pied": "2",
        "site": "Centris",
        "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/12317886",
        "score": "",
        "notes": "Rez-de-chaussée avec sous-sol aménagé récemment rénové (2 chambres au sous-sol + bureau), 5 pièces, disponible 1er juin 2026, Walk Score 91.",
        "photo": "",
    },
    {
        "date_ajout": "2026-08-19",
        "statut": "NOUVEAU",
        "titre": "Très beau 7 1/2 (2 chambres fermées + bureau), 1200 pi², balcon - Hochelaga-Maisonneuve, à ~10 min du métro Pie-IX",
        "quartier": "Hochelaga-Maisonneuve",
        "adresse": "n/d (Montréal, QC H1V 2R6)",
        "prix": "2200",
        "superficie_pi2": "1200",
        "chambres": "2",
        "balcon": "oui",
        "station_metro": "Pie-IX",
        "ligne_metro": "verte",
        "minutes_a_pied": "10",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/tres-beau-7-1-2-a-louer-hochelaga-maisonneuve/1741046490",
        "score": "",
        "notes": "2e étage d'un triplex, cuisine/portes/salle de bain rénovées (2022-2024), plancher bois franc, mur de brique, eau incluse, animaux limités acceptés, disponible 1er sept. 2026, près marché Maisonneuve et stade olympique.",
        "photo": "",
    },
]

def score(row):
    s = 0
    sup = row['superficie_pi2']
    try:
        sup_val = int(sup)
        if sup_val >= 1100:
            s += 3
        elif sup_val >= 900:
            s += 2
    except ValueError:
        pass
    try:
        ch = int(row['chambres'])
        if ch >= 3:
            s += 2
        elif ch == 2:
            s += 1
    except ValueError:
        pass
    if row['balcon'] == 'oui':
        s += 2
    try:
        mins = int(str(row['minutes_a_pied']).split('-')[0])
        if mins <= 12:
            if row['ligne_metro'] == 'verte':
                s += 2
            else:
                s += 1
    except ValueError:
        pass
    s += 1
    return s

for row in new_rows:
    row['score'] = str(score(row))

rows.extend(new_rows)

def sort_key(row):
    is_new = 0 if row['statut'] == 'NOUVEAU' else 1
    try:
        sc = -int(row['score'])
    except (ValueError, TypeError):
        sc = 0
    return (is_new, sc)

rows.sort(key=sort_key)

with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("done", len(rows))
for r in new_rows:
    print(r['titre'], r['score'])
