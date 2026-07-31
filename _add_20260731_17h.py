import csv

CSV_PATH = "annonces.csv"

with open(CSV_PATH, newline='', encoding='utf-8') as f:
    r = csv.reader(f)
    rows = list(r)
header = rows[0]
data = rows[1:]

# Flip old NOUVEAU -> vu
for row in data:
    if row[1] == "NOUVEAU":
        row[1] = "vu"

new_rows = [
    ["2026-07-31", "NOUVEAU",
     "5½ haut de gamme rénové, 2 chambres, balcon - à 2 pas du métro D'Iberville (Rosemont-La Petite-Patrie)",
     "Rosemont-La Petite-Patrie", "n/d (Montréal, QC H1X)", "1950", "950", "2", "oui",
     "D'Iberville", "bleue", "1", "Kijiji",
     "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/5-haut-de-gamme-renove-a-2-pas-du-metro-iberville/1741173311",
     "7",
     "Rénové au complet au printemps 2024, grand balcon arrière couvert, plancher chauffant salle de bain, climatisation, laveuse-sécheuse inclus, Walk Score 94, aucun animal, non-fumeur, enquête de crédit exigée, bail 1 an, disponible 1er juillet 2026",
     ""],
    ["2026-07-31", "NOUVEAU",
     "Grand 7½ (5 chambres), 1400 pi², balcon - rue Chapleau près métro Frontenac/Préfontaine (Centre-Sud, bordure Plateau)",
     "Ville-Marie (Centre-Sud)", "Rue Chapleau, Montréal, QC H2K 3H7", "2350", "1400", "5", "oui",
     "Frontenac", "verte", "10", "Kijiji",
     "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/7-et-demi-sur-le-plateau-mont-royal/1738856823",
     "10",
     "Annonce présentée comme Plateau-Mont-Royal mais secteur réel Centre-Sud/Sainte-Marie, 2e étage de quadruplex, 5 chambres (5e utilisable en bureau), accès balcon arrière depuis la cuisine, chauffage/eau chaude/électroménagers inclus, près métro Frontenac et Préfontaine (ligne verte), proche parcs Baldwin et Lafontaine, animaux limités, non-fumeur, enquête de crédit, disponible 1er juillet 2026",
     ""],
]

all_data = data + new_rows

def sort_key(row):
    statut = row[1]
    try:
        score = int(row[14])
    except (ValueError, IndexError):
        score = 0
    return (0 if statut == "NOUVEAU" else 1, -score)

all_data.sort(key=sort_key)

with open(CSV_PATH, "w", newline='', encoding='utf-8') as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow(header)
    w.writerows(all_data)

print("done, total rows:", len(all_data))
print("NOUVEAU count:", sum(1 for r in all_data if r[1] == "NOUVEAU"))
