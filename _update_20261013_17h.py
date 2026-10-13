import csv

path = "annonces.csv"
with open(path, newline='', encoding='utf-8') as f:
    rd = csv.DictReader(f)
    fn = rd.fieldnames
    rows = list(rd)
for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'
links = set(r['lien'] for r in rows)

new = [
    dict(titre="Grand 5½ 3 chambres fermées + bureau, 1600 pi², 2 terrasses, stationnement - secteur Boyer/Mont-Royal (Plateau)",
         quartier="Le Plateau-Mont-Royal",
         adresse="Secteur rue Boyer / avenue du Mont-Royal, Montréal, QC H2J 3C9",
         prix="2300", superficie_pi2="1600", chambres="3", balcon="oui",
         station_metro="Mont-Royal", ligne_metro="orange",
         minutes_a_pied="10 (estimé, à vérifier)", site="Kijiji",
         lien="https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-5-1-2-le-plateau-mont-royal/1744761905",
         score="9",
         notes="Deux terrasses privées (avant et arrière), laveuse-sécheuse incluse, 1 stationnement extérieur inclus, semi-meublé, animaux acceptés, charges non incluses, libre 1er nov. 2026, bail 1 an, adresse exacte non précisée"),
    dict(titre="5½ rénové 2023, 3 chambres, 1000 pi², 2 balcons - De Lorimier (Plateau/Centre-Sud), près des métros Papineau et Frontenac",
         quartier="Le Plateau-Mont-Royal",
         adresse="2331, Avenue De Lorimier, Montréal, QC H2K 3X4",
         prix="2080", superficie_pi2="1000", chambres="3", balcon="oui",
         station_metro="Papineau", ligne_metro="verte",
         minutes_a_pied="10-12 (estimé, à vérifier)", site="Kijiji",
         lien="https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/magnifique-5-1-2-au-coeur-de-ville-marie/1744759176",
         score="9",
         notes="Rénové en 2023, thermopompe/air climatisé, lave-vaisselle et laveuse-sécheuse inclus, ~500 m du parc La Fontaine, hydro non incluse, animaux : info contradictoire (attributs « non », texte « acceptés »), une chambre sans fenêtre, DISPONIBLE SEULEMENT 1er mars 2027, bail 1 an"),
    dict(titre="Grand et lumineux 5½, 3 chambres, 1200 pi², grand balcon + terrasse - La Petite-Patrie",
         quartier="La Petite-Patrie",
         adresse="Adresse non précisée, Montréal, QC H2G 3C1 (La Petite-Patrie)",
         prix="2050", superficie_pi2="1200", chambres="3", balcon="oui",
         station_metro="Rosemont", ligne_metro="orange",
         minutes_a_pied="10-12 (estimé, à vérifier)", site="Kijiji",
         lien="https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-et-lumineux-logement-51-2/1744412382",
         score="9",
         notes="Duplex/triplex, eau incluse, lave-vaisselle, climatisation, animaux non acceptés, libre 5 oct. 2026, bail 1 an, station estimée d'après le code postal (rue non précisée), l'annonce signale que les photos peuvent provenir d'autres unités"),
]
base = dict(date_ajout="2026-10-13", statut="NOUVEAU", photo="")
n = 0
for d in new:
    if d['lien'] in links:
        continue
    row = dict(base)
    row.update(d)
    rows.append(row)
    n += 1


def key(r):
    s = r['score']
    return (0 if r['statut'] == 'NOUVEAU' else 1, -int(s) if s.isdigit() else 0)


rows.sort(key=key)
with open(path, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fn, quoting=csv.QUOTE_MINIMAL)
    w.writeheader()
    w.writerows(rows)
print("added", n, "total", len(rows))
