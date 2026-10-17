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
    dict(titre="Superbe 7½ rénové 2e étage, 5 chambres, 1300 pi², 2 balcons privés - Hochelaga (rue Sainte-Catherine E)",
         quartier="Hochelaga-Maisonneuve", adresse="3781 Rue Sainte-Catherine E, Montréal, QC H1W 2E9",
         prix="2250", superficie_pi2="1300", chambres="5", balcon="oui", station_metro="Joliette",
         ligne_metro="verte", minutes_a_pied="10-12 (estimé, à vérifier)", site="Kijiji",
         lien=B + "hochelaga-superbe-7-1-2-renove-de-5-chambres-2e-etage/1744859317", score="10",
         notes="Rénové, électroménagers et laveuse-sécheuse inclus, bail 1 an, disponibilité affichée 7 oct. 2026 (description : dès maintenant), eau/charges contradictoires dans l'annonce, adresse à confirmer (3781 ou 3783), station estimée"),
]
d = dict(date_ajout="2026-10-17", statut="NOUVEAU", photo="")
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
