import csv

CSV_PATH = "annonces.csv"

with open(CSV_PATH, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)

for r in rows:
    if r["statut"] == "NOUVEAU":
        r["statut"] = "vu"

new_row = {
    "date_ajout": "2026-08-09",
    "statut": "NOUVEAU",
    "titre": "Condo 2 chambres avec balcon (ELYA), quartier Centre-Sud - à 5 min du métro Frontenac",
    "quartier": "Ville-Marie (Centre-Sud)",
    "adresse": "n/d (secteur Frontenac / de Rouen, Montréal)",
    "prix": "2400",
    "superficie_pi2": "944",
    "chambres": "2",
    "balcon": "oui",
    "station_metro": "Frontenac",
    "ligne_metro": "verte",
    "minutes_a_pied": "5",
    "site": "Marketplace",
    "lien": "https://www.facebook.com/marketplace/item/970016458942788",
    "score": "8",
    "notes": "Condos ELYA (projet de 3 étages), partiellement meublé (mobilier chambre principale, 2e chambre et salon inclus), électroménagers inclus (frigo, cuisinière, lave-vaisselle, laveuse-sécheuse), assurance et internet exclus, Walk Score 97 / Transit Score 75 / Bike Score 98, quartier Centre-Sud adjacent à Hochelaga-Maisonneuve, disponible maintenant. Lien Facebook (connexion requise).",
    "photo": "https://scontent-ord5-2.xx.fbcdn.net/v/t39.84726-6/680726095_813975818030704_4628638014475424705_n.jpg?stp=c134.0.540.540a_dst-jpg_p180x540_tt6&_nc_cat=103&ccb=1-7&_nc_sid=92e707&_nc_ohc=DaakHU1OaocQ7kNvwEMEtaO&_nc_oc=AdrsUr5TAVFF_e9NxaxSw-e62G_ASx45bZgZ3AKzGUiGAv7Y6AituyAR4PJfd2d07IM&_nc_zt=14&_nc_ht=scontent-ord5-2.xx&_nc_gid=sttELMekqIl1QrHVrbiaqg&_nc_ss=7f2a8&oh=00_AQFHyumaRS4RXVFvesKyc1d5apqNp6RyNfym_4lCPOPaaQ&oe=6A7EC616",
}

rows.append(new_row)

def sort_key(r):
    is_new = 0 if r["statut"] == "NOUVEAU" else 1
    try:
        score = -int(r["score"])
    except (ValueError, KeyError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

print(f"Total rows: {len(rows)}")
print(f"NOUVEAU count: {sum(1 for r in rows if r['statut'] == 'NOUVEAU')}")
