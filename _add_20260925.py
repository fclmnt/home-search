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
    [TODAY, "NOUVEAU", "4½ + sous-sol, cession de bail - Marie-Anne E., Plateau", "Le Plateau-Mont-Royal",
     "172, rue Marie-Anne Est, Montréal, QC H2W 1A5", "1940", "900", "2", "oui", "Mont-Royal", "orange", "8 (estimé)",
     "Kijiji", K + "4-1-2-basement-plateau-mont-royal-lease-transfer-1940/1743197854", "7",
     "Rez-de-chaussée + sous-sol (salle familiale, buanderie), électroménagers et laveuse/sécheuse, chauffage électrique aux frais du locataire, libre 1er oct., 1er mois gratuit, pas d'animaux, bail 1 an min.", ""],
    [TODAY, "NOUVEAU", "SUPERBE 6½ Plateau-Mont-Royal, 3 chambres fermées, 2 balcons - av. de l'Hôtel-de-Ville", "Le Plateau-Mont-Royal",
     "4082, avenue de l'Hôtel-de-Ville, Montréal, QC H2W 2H1", "2300", "1000", "3", "oui (2 balcons)", "Mont-Royal", "orange", "12",
     "Kijiji", K + "superbe-6-1-2-plateau-mont-royal/1743328232", "8",
     "Maison victorienne rénovée 1890, bois franc, brique, beaucoup de rangement, laveuse/sécheuse et lave-vaisselle inclus, libre 1er oct. (négociable). Chauffage non précisé. 12 min de Mont-Royal selon l'annonce.", ""],
]
links = {r[13] for r in body}
new = [n for n in new if n[13] not in links]
body = new + body
body.sort(key=lambda r: (r[1] != "NOUVEAU", -int(r[14]) if r[14].isdigit() else 0))
w = csv.writer(open(PATH, "w", encoding="utf-8", newline=""))
w.writerow(hdr)
w.writerows(body)
print(len(new), "ajouts")
