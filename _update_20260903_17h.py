import csv

path = "annonces.csv"
with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'

new_rows = [
{
 "date_ajout": "2026-09-03",
 "statut": "NOUVEAU",
 "titre": "4 1/2 meublé, 2 chambres, 2 salles de bain, terrasse - rue Nicolet (Hochelaga), à 6 min du métro Joliette",
 "quartier": "Hochelaga-Maisonneuve",
 "adresse": "2113, Rue Nicolet, Montréal, QC H1W 3L3",
 "prix": "2100",
 "superficie_pi2": "n/d",
 "chambres": "2",
 "balcon": "oui",
 "station_metro": "Joliette",
 "ligne_metro": "verte",
 "minutes_a_pied": "6",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/appartement-2-chambres-et-2-salles-de-bain/1742905541",
 "score": "6",
 "notes": "Totalement meuble, tous electromenagers et mobilier inclus, climatisation, internet inclus, 1 stationnement, animaux limites, disponible 1er octobre 2026, bail jusqu'au 30 sept 2027, electricite en sus (~100$/mois).",
 "photo": "",
},
{
 "date_ajout": "2026-09-03",
 "statut": "NOUVEAU",
 "titre": "4 1/2 meublé de luxe, 2 chambres, 1050 pi² - rue Saint-Denis (Plateau), à ~8 min du métro Mont-Royal",
 "quartier": "Le Plateau-Mont-Royal",
 "adresse": "4055, Rue Saint-Denis, Montréal, QC",
 "prix": "2200",
 "superficie_pi2": "1050",
 "chambres": "2",
 "balcon": "n/d",
 "station_metro": "Mont-Royal",
 "ligne_metro": "verte",
 "minutes_a_pied": "8 (estimé)",
 "site": "logisquebec",
 "lien": "https://www.logisquebec.com/appartement-a-louer-le-plateau-mont-royal-l348152",
 "score": "6",
 "notes": "Condo meuble de prestige, coin de rue avec vues sur Saint-Denis, 2 salles de bain completes, plafonds 12 pi, internet fibre 1 Gbps, climatisation, chauffage et electricite inclus, stationnement prive, animaux acceptes, disponible immediatement.",
 "photo": "",
},
{
 "date_ajout": "2026-09-03",
 "statut": "NOUVEAU",
 "titre": "5 1/2 rénové, 2 chambres, 2 balcons - coin Drolet/Castelnau (Villeray), à ~5 min du métro Jean-Talon/De Castelnau",
 "quartier": "Villeray",
 "adresse": "Rue Drolet et Castelnau, Montréal, QC H2V 1W1",
 "prix": "2095",
 "superficie_pi2": "n/d",
 "chambres": "2",
 "balcon": "oui",
 "station_metro": "Jean-Talon",
 "ligne_metro": "orange",
 "minutes_a_pied": "5 (estimé)",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/5-1-2-appartement-a-louer/1742933661",
 "score": "5",
 "notes": "2 balcons (avant et arriere), bureau et espace de rangement, planchers de bois franc, plafonds hauts, laveuse/secheuse/frigo/cuisiniere inclus, eau incluse, chats acceptes, disponible 1er octobre 2026, bail 1 an.",
 "photo": "",
},
]

existing_links = set(r['lien'] for r in rows)
for nr in new_rows:
    assert nr['lien'] not in existing_links, "Duplicate: " + nr['lien']

rows = new_rows + rows

def sort_key(r):
    is_new = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        score = -int(r['score'])
    except Exception:
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open(path, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Total rows:", len(rows))
print("NOUVEAU count:", sum(1 for r in rows if r['statut'] == 'NOUVEAU'))
