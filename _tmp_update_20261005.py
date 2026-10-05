import csv

PATH = "annonces.csv"

with open(PATH, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# 1. Pass old NOUVEAU to vu
for r in rows:
    if r["statut"] == "NOUVEAU":
        r["statut"] = "vu"

# 2. Add new row
new_row = {
    "date_ajout": "2026-10-05",
    "statut": "NOUVEAU",
    "titre": "5½ rénové (3 chambres), 1425 pi² - rue La Fontaine, Hochelaga-Maisonneuve",
    "quartier": "Hochelaga-Maisonneuve",
    "adresse": "3527, Rue La Fontaine, Montréal, QC",
    "prix": "2100",
    "superficie_pi2": "1425",
    "chambres": "3",
    "balcon": "n/d",
    "station_metro": "Joliette",
    "ligne_metro": "verte",
    "minutes_a_pied": "10 (estimé, 850m)",
    "site": "Centris",
    "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/16826763",
    "score": "8",
    "notes": "Portes-fenetres cuisine/salon, 2 chambres avec fenetre sur 3, Walk Score 98, a 850m (environ 10 min a pied) du metro Joliette (ligne verte), pres de la Promenade Ontario (commerces, restaurants). Disponible immediatement ou 10 jours apres acceptation de la promesse de location. Balcon non precise par l'annonce. Visite libre annoncee le lundi 5 octobre 18h-19h.",
    "photo": "",
}
rows.append(new_row)

# 3. Sort: NOUVEAU first, then score descending
def sort_key(r):
    is_nouveau = 0 if r["statut"] == "NOUVEAU" else 1
    try:
        score = -int(r["score"])
    except (ValueError, TypeError):
        score = 0
    return (is_nouveau, score)

rows.sort(key=sort_key)

with open(PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Done. Total rows:", len(rows))
print("NOUVEAU count:", sum(1 for r in rows if r["statut"] == "NOUVEAU"))
