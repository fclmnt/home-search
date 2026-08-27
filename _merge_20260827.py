import csv

with open('annonces.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'

new_rows = [
    {
        "date_ajout": "2026-08-27",
        "statut": "NOUVEAU",
        "titre": "Plateau-Mont-Royal - Superbe 5 1/2 sur 2 Etages - 3 Chambres",
        "quartier": "Le Plateau-Mont-Royal",
        "adresse": "106, Rue Napoleon, Montreal, H2W 1K6",
        "prix": "2400",
        "superficie_pi2": "1100",
        "chambres": "3",
        "balcon": "oui",
        "station_metro": "Sherbrooke",
        "ligne_metro": "orange",
        "minutes_a_pied": "6",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/plateau-mont-royal-superbe-5-1-2-sur-2-etages-3-chambres/1742098393",
        "score": "9",
        "notes": "5 1/2 sur deux etages, 1100 pi2, 2 grandes chambres fermees plus une petite piece fermee, 2 balcons. Proche des parcs Lafontaine et Jeanne-Mance, rue Saint-Denis et avenue du Mont-Royal (commerces, cafes, restaurants). Disponible le 15 aout 2026. Environ 6 min a pied de la station Sherbrooke (ligne orange).",
        "photo": "",
    },
    {
        "date_ajout": "2026-08-27",
        "statut": "NOUVEAU",
        "titre": "Villeray - Superbe Condo 4 1/2 Renove - Animaux Permis",
        "quartier": "Villeray",
        "adresse": "8325, Avenue Christophe-Colomb, Montreal, H2P 0C3",
        "prix": "1950",
        "superficie_pi2": "970",
        "chambres": "2",
        "balcon": "oui",
        "station_metro": "Jarry",
        "ligne_metro": "orange",
        "minutes_a_pied": "8",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/villeray-superbe-condo-4-1-2-renove-animaux-permis/1742098364",
        "score": "7",
        "notes": "4 1/2 renove de 970 pi2, 2 chambres fermees, grand salon avec balcon prive, gym et terrasse dans l'immeuble. Proche du parc Villeray, du parc Jarry et de la rue Saint-Hubert (restaurants et commerces).",
        "photo": "",
    },
    {
        "date_ajout": "2026-08-27",
        "statut": "NOUVEAU",
        "titre": "4½ renove, 2 chambres fermees - Rue Boyer",
        "quartier": "Rosemont/La Petite-Patrie",
        "adresse": "6552, rue Boyer, app. 103, Montreal",
        "prix": "2200",
        "superficie_pi2": "1050",
        "chambres": "2",
        "balcon": "n/d",
        "station_metro": "Beaubien",
        "ligne_metro": "orange",
        "minutes_a_pied": "5",
        "site": "DuProprio",
        "lien": "https://duproprio.com/fr/location/montreal/rosemont-la-petite-patrie/4-1-2-a-louer/hab-103-6552-boyer-1140701",
        "score": "5",
        "notes": "Quartier tres dynamique (Walk Score 96, Bike Score 100), a moins de 5 min a pied du metro Beaubien, proche Place Boyer. Animaux interdits sauf un chat sous conditions. Chauffage/electricite negociables (~150$/mois d'electricite en sus). Libre le 1er septembre 2026.",
        "photo": "",
    },
    {
        "date_ajout": "2026-08-27",
        "statut": "NOUVEAU",
        "titre": "Condo / Appartement a louer - 4355, Rue Marquette",
        "quartier": "Le Plateau-Mont-Royal",
        "adresse": "4355, Rue Marquette, Montreal (Le Plateau-Mont-Royal)",
        "prix": "2350",
        "superficie_pi2": "995",
        "chambres": "2",
        "balcon": "n/d",
        "station_metro": "Mont-Royal",
        "ligne_metro": "orange",
        "minutes_a_pied": "12",
        "site": "Centris",
        "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-le-plateau-mont-royal/28692748",
        "score": "4",
        "notes": "Disponible le 1er septembre 2026. Superficie 995 pi2, 2 chambres. Aucune mention de balcon dans la description. Distance approximative de 12 min a pied de la station Mont-Royal (ligne orange).",
        "photo": "",
    },
]

rows.extend(new_rows)

def sort_key(r):
    is_new = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        score = -float(r['score'])
    except (ValueError, TypeError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Done. Total rows:", len(rows))
print("NOUVEAU count:", sum(1 for r in rows if r['statut'] == 'NOUVEAU'))
