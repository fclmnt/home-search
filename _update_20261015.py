import csv

path = "annonces.csv"
rows = list(csv.DictReader(open(path, newline='', encoding='utf-8')))
fn = list(rows[0].keys())
for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'
links = set(r['lien'] for r in rows)
B = "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/"
new = [
    dict(titre="Grand 5½ géant, 3 chambres + bureau, 1500 pi², 2 balcons - Gay Village (3 min du métro Beaudry)",
         quartier="Centre-Sud / Village", adresse="1572-1574 rue Montcalm, Montréal, QC H2L 3H4",
         prix="1950", superficie_pi2="1500", chambres="3", balcon="oui", station_metro="Beaudry",
         ligne_metro="verte", minutes_a_pied="3", site="Kijiji",
         lien=B + "ville-marie-geant-5-1-2-de-3-chambres-bureau-2-balcons/1744859322", score="10",
         notes="3e étage, rénové, eau incluse, laveuse-sécheuse, climatisation murale, animaux limités, bail 1 an, date de disponibilité affichée 1er avril 2026 (annonce active, à confirmer)"),
    dict(titre="Superbe 6½ rénové 2e étage, 4 chambres, 1500 pi², balcon arrière - Centre-Sud (5 min du métro Frontenac)",
         quartier="Centre-Sud / Ville-Marie", adresse="1737 rue Fullum, Montréal, QC H2K 3M7",
         prix="1975", superficie_pi2="1500", chambres="4", balcon="oui", station_metro="Frontenac",
         ligne_metro="verte", minutes_a_pied="5", site="Kijiji",
         lien=B + "ville-marie-superbe-6-1-2-renove-au-2e-etage-4-chambres/1744859335", score="10",
         notes="Rénové, eau incluse, lave-vaisselle, laveuse-sécheuse, climatisation murale, animaux limités, 2 chambres sans fenêtre, bail 1 an, libre maintenant (à confirmer)"),
    dict(titre="6½ rénové avec cachet, 2 chambres + bureau, 950 pi², balcon/terrasse - 5 min du métro Préfontaine",
         quartier="Hochelaga-Maisonneuve", adresse="Rue non précisée, Montréal, QC H1W 2P3",
         prix="1975", superficie_pi2="950", chambres="2", balcon="oui", station_metro="Préfontaine",
         ligne_metro="verte", minutes_a_pied="5", site="Kijiji",
         lien=B + "6-renove-avec-cachet-libre-5-min-metro-prefontaine/1742907944", score="8",
         notes="2e étage d'un triplex, planchers de bois, lave-vaisselle, raccords laveuse-sécheuse, climatisation, animaux acceptés, charges non précisées, bail 1 an, libre maintenant"),
    dict(titre="À deux pas du cinéma! 5½ rénové, 1000 pi², balcon - Rosemont (Promenade Masson)",
         quartier="Rosemont", adresse="Rue non précisée (secteur Étienne-Desmarteaux), Montréal, QC H1Y 3B9",
         prix="1932", superficie_pi2="1000", chambres="3", balcon="oui", station_metro="Beaubien",
         ligne_metro="orange", minutes_a_pied="10-12 (estimé, à vérifier)", site="Kijiji",
         lien=B + "a-deux-pas-du-cinema/1744722948", score="8",
         notes="Rénové, thermopompe neuve, 3 chambres à vérifier (description : 2 grandes chambres + den), électricité et eau chaude à la charge du locataire, animaux non acceptés, bail 1 an, libre 12 oct. 2026, station estimée d'après le code postal"),
    dict(titre="5½, 3 chambres, 900 pi², balcon, vue sur parc - secteur De Lorimier",
         quartier="Le Plateau-Mont-Royal", adresse="Rue non précisée, Montréal, QC H2H 1Y6",
         prix="1950", superficie_pi2="900", chambres="3", balcon="oui", station_metro="Laurier",
         ligne_metro="orange", minutes_a_pied="10-12 (estimé, à vérifier)", site="Kijiji",
         lien=B + "5-3-chambres-dispo-avec-vue-sur-parc-a-voir/1742915215", score="8",
         notes="Rénové, laveuse-sécheuse, lave-vaisselle, climatisation, planchers de bois, animaux limités, charges non précisées, bail 1 an, station estimée d'après le code postal"),
]
d = dict(date_ajout="2026-10-15", statut="NOUVEAU", photo="")
for n in new:
    if n['lien'] in links:
        continue
    r = dict(d)
    r.update(n)
    rows.append(r)
rows.sort(key=lambda r: (0 if r['statut'] == 'NOUVEAU' else 1, -int(r['score']) if r['score'].isdigit() else 0))
with open(path, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fn)
    w.writeheader()
    w.writerows(rows)
