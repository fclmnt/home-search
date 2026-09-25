import csv
PATH = "annonces.csv"
TODAY = "2026-09-25"
rows = list(csv.reader(open(PATH, encoding="utf-8")))
hdr, body = rows[0], rows[1:]
for r in body:
    if r[1] == "NOUVEAU":
        r[1] = "vu"
K = "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/"
new = [
    [TODAY, "NOUVEAU", "Très grand 6½ rénové, 2e étage, 2 balcons - boul. Rosemont", "Rosemont / La Petite-Patrie",
     "2039, boulevard Rosemont (angle De Lorimier), Montréal, QC H2G 1T2", "1950", "1250", "3", "oui (2 balcons)", "Rosemont", "orange", "10 (estimé)",
     "Kijiji", K + "tres-grand-logement-6-1-2-2eme-etage-renove-libre-immediatement/1743064869", "9",
     "3 chambres fermées + bureau, laveuse/sécheuse incluse, chauffage non précisé, pas d'animaux, libre 7 sept.", ""],
    [TODAY, "NOUVEAU", "5½ 3 CAC Plateau, Parc Lafontaine - libre", "Le Plateau-Mont-Royal",
     "Secteur Parc Lafontaine / De Lorimier, Montréal, QC H2K 4G1 (adresse exacte non indiquée)", "1950", "1000", "3", "oui", "Papineau", "verte", "12 (estimé)",
     "Kijiji", K + "5-1-2-3-cac-sur-le-plateau-parc-lafontaine-libre-1950/1743756670", "9",
     "Rénové, branchements laveuse/sécheuse et lave-vaisselle, chats et petits chiens acceptés, bail 1 an, libre depuis le 20 sept. Station estimée d'après le code postal, à confirmer.", ""],
    [TODAY, "NOUVEAU", "Cession de bail 5½ Plateau (De Lorimier), 2 balcons", "Le Plateau-Mont-Royal",
     "Secteur Mont-Royal / Messier, Montréal, QC H2H 2H8 (adresse exacte non indiquée)", "2279", "1000", "3", "oui (avant et arrière)", "Mont-Royal", "orange", "12 (estimé)",
     "Kijiji", K + "cession-de-bail-5-au-plateau-de-lorimier/1743826982", "8",
     "Cession de bail, laveuse/sécheuse et électroménagers inox neufs, chats acceptés (pas de chiens), immeuble non-fumeur, libre 1er nov. (flexible), bail renouvelable 1er juill. 2027.", ""],
]
links = {r[13] for r in body}
new = [n for n in new if n[13] not in links]
body = new + body
body.sort(key=lambda r: (r[1] != "NOUVEAU", -int(r[14]) if r[14].isdigit() else 0))
w = csv.writer(open(PATH, "w", encoding="utf-8", newline=""))
w.writerow(hdr)
w.writerows(body)
print(len(new), "ajouts")
