import csv

CSV_PATH = "annonces.csv"

with open(CSV_PATH, newline='', encoding='utf-8') as f:
    r = csv.reader(f)
    rows = list(r)
header = rows[0]
data = rows[1:]

new_rows = [
    ["2026-07-30", "NOUVEAU",
     "Grand 4½ meublé, 2 chambres, terrasse privée, 1347 pi² - rue Ontario Est (Hochelaga, à 10 min du métro Pie-IX)",
     "Hochelaga-Maisonneuve", "3928, Rue Ontario Est, app. 35, Montréal", "2250", "1347", "2", "oui",
     "Pie-IX", "verte", "10", "Centris",
     "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/17092786",
     "9",
     "Meublé, cuisine moderne avec électroménagers haut de gamme, terrasse privée, chats acceptés, près du Marché Maisonneuve et du parc Maisonneuve, Walk Score 99, disponible 1er août 2026",
     ""],
    ["2026-07-30", "NOUVEAU",
     "Grand 7½ (3 chambres + bureau), 1550 pi² - RDC près métro Beaubien (Rosemont/La Petite-Patrie)",
     "Rosemont-La Petite-Patrie", "n/d (Montréal, QC H2G 3C1)", "2325", "1550", "3", "n/d",
     "Beaubien", "orange", "7", "Kijiji",
     "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/metro-beaubien-7-5-rdc-pour-octobre/1741279367",
     "7",
     "Rez-de-chaussée, planchers de bois franc et boiseries d'origine, cour, animaux limités, bail 1 an, disponible 1er octobre 2026",
     ""],
    ["2026-07-30", "NOUVEAU",
     "4½ rénové, 2 chambres, 950 pi², accès cour arrière - juste à côté du métro Beaubien (La Petite-Patrie)",
     "Rosemont-La Petite-Patrie", "6368, Avenue De Chateaubriand, Montréal, QC H2S 2N4", "1950", "950", "2", "n/d",
     "Beaubien", "orange", "1", "Kijiji",
     "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/4-5-in-petite-patrie-next-to-metro-beaubien/1738727392",
     "5",
     "À moins d'une minute de marche du métro Beaubien, électroménagers inclus (frigo/cuisinière/laveuse-sécheuse), accès à la cour arrière, petits animaux acceptés, enquête de crédit exigée, hydro en sus, pas de stationnement, disponible juin 2026",
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
