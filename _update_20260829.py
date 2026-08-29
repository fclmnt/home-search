import csv

PATH = "annonces.csv"

with open(PATH, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)

for r in rows:
    if r["statut"] == "NOUVEAU":
        r["statut"] = "vu"

new_rows = [
    {
        "date_ajout": "2026-08-29",
        "statut": "NOUVEAU",
        "titre": "3 chambres, meuble, chauffe, eclaire, terrasse - a 3 min du metro Joliette (Hochelaga-Maisonneuve)",
        "quartier": "Hochelaga-Maisonneuve",
        "adresse": "n/d (secteur Promenade Ontario / metro Joliette, Montreal, QC H1W 1R9)",
        "prix": "2400",
        "superficie_pi2": "1152",
        "chambres": "3",
        "balcon": "oui",
        "station_metro": "Joliette",
        "ligne_metro": "verte",
        "minutes_a_pied": "3",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/3-chambres-wifi-meuble-chauffe-eclaire-metro-joliette-terrasse/1742703523",
        "score": "10",
        "notes": "entierement meuble; chauffe (foyer gaz); wifi inclus; animaux limites; terrasse 20x11 pi; disponible 29 aout 2026; Airbnb interdit",
        "photo": "",
    },
    {
        "date_ajout": "2026-08-29",
        "statut": "NOUVEAU",
        "titre": "6 1/2 spacieux, 3 chambres, grand balcon - avenue Louis-Hebert (Rosemont/La Petite-Patrie), entre metro Rosemont et Beaubien",
        "quartier": "Rosemont-La Petite-Patrie",
        "adresse": "5838, Avenue Louis-Hebert, Montreal, QC H2G 2G2",
        "prix": "2100",
        "superficie_pi2": "1000",
        "chambres": "3",
        "balcon": "oui",
        "station_metro": "Rosemont / Beaubien",
        "ligne_metro": "orange",
        "minutes_a_pied": "8",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/6-rosemont-gem-spacious-3-bedroom-fully-equipped/1742621981",
        "score": "8",
        "notes": "2 thermopompes (chauffage/climatisation inclus); electromenagers inclus; animaux limites; disponible 1er sept. 2026",
        "photo": "",
    },
    {
        "date_ajout": "2026-08-29",
        "statut": "NOUVEAU",
        "titre": "6 1/2, 2 chambres + bureau convertible, terrasse 3 saisons - secteur Parc Jarry (Villeray)",
        "quartier": "Villeray",
        "adresse": "n/d (secteur Parc Jarry, Montreal, QC H2R 2M2)",
        "prix": "2295",
        "superficie_pi2": "1240",
        "chambres": "2",
        "balcon": "oui",
        "station_metro": "Jarry",
        "ligne_metro": "bleue",
        "minutes_a_pied": "10",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/6-1-2-appartement/1738525339",
        "score": "8",
        "notes": "chauffage inclus; climatisation murale (3 unites); internet inclus; terrasse 3 saisons partagee; bureau convertible en 3e chambre; distance metro estimee (non precisee dans l'annonce); disponible 1er juin 2026",
        "photo": "",
    },
]

rows.extend(new_rows)

def sort_key(r):
    is_new = 0 if r["statut"] == "NOUVEAU" else 1
    try:
        score = -int(r["score"])
    except (ValueError, KeyError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open(PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

print(f"{len(new_rows)} nouvelles annonces ajoutees. Total: {len(rows)} lignes.")
