import csv

path = 'annonces.csv'
with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'

new_rows = [
{
 'date_ajout': '2026-07-23', 'statut': 'NOUVEAU',
 'titre': 'Grand 5½ de 1240 pi² avec 2 balcons privés - rue de la Visitation (Centre-Sud), à 2 min du métro Beaudry',
 'quartier': 'Centre-Sud',
 'adresse': '1433, Rue de la Visitation, Montréal',
 'prix': '2000', 'superficie_pi2': '1240', 'chambres': '2', 'balcon': 'oui',
 'station_metro': 'Beaudry', 'ligne_metro': 'verte', 'minutes_a_pied': '2',
 'site': 'Marketplace', 'lien': 'https://www.facebook.com/marketplace/item/1675910780361896',
 'score': '9',
 'notes': "2 chambres fermées + 1 chambre ouverte, grande cuisine moderne avec îlot central, salle de bain rénovée avec espace laveuse/sécheuse, lien exige une connexion Facebook",
 'photo': 'https://scontent-yyz1-1.xx.fbcdn.net/v/t39.30808-6/747978141_10167419432889256_7838070296744630358_n.jpg?stp=c273.0.652.652a_dst-jpg_tt6&cstp=mx652x652&ctp=s565x565&_nc_cat=102&ccb=1-7&_nc_sid=454cf4&_nc_ohc=1BHIBLZMut0Q7kNvwGcjJKY&_nc_oc=AdqL6QD8fVTD7q3J4l5WBnexTjWzHzx5_JFODaqPJQYjJbX5CNPnTI7QmCUqQifrkxQ&_nc_zt=23&_nc_ht=scontent-yyz1-1.xx&_nc_gid=I01Huqn8cRYQWCF5daV0fw&_nc_ss=7f2a8&oh=00_AQCmBZgaUJOgbf9TtDkOp05R878cvx5VZPmstj6q8E25Kg&oe=6A686D2B'
},
{
 'date_ajout': '2026-07-23', 'statut': 'NOUVEAU',
 'titre': '4½ meublé avec balcon refait à neuf - entre les métros Jarry et Jean-Talon (Villeray)',
 'quartier': 'Villeray',
 'adresse': 'Secteur Villeray, entre métro Jarry et Jean-Talon, Montréal',
 'prix': '2000', 'superficie_pi2': 'n/d', 'chambres': '2', 'balcon': 'oui',
 'station_metro': 'Jarry ou Jean-Talon (à vérifier)', 'ligne_metro': 'orange', 'minutes_a_pied': '8 (estimé)',
 'site': 'Marketplace', 'lien': 'https://www.facebook.com/marketplace/item/1200370795499483',
 'score': '5',
 'notes': "Appartement meublé (2 lits queen, meubles inclus), balcon refait à neuf à l'arrière, à 5 min à pied du parc Jarry et 10 min du marché Jean-Talon, 2e étage d'un duplex, lien exige une connexion Facebook",
 'photo': 'https://scontent-yyz1-1.xx.fbcdn.net/v/t39.84726-6/719951504_1525424678988571_3029279822230004988_n.jpg?stp=c0.87.526.526a_dst-jpg_p526x395_tt6&_nc_cat=108&ccb=1-7&_nc_sid=92e707&_nc_ohc=1GvmU2MuoZYQ7kNvwGQoY7P&_nc_oc=AdoTdsiH2zz9uO5Fd_ygBkJLJi0OpX-UJyx11ydhdL0cY2WAinKXNKxj7G3DpqNMvvc&_nc_zt=14&_nc_ht=scontent-yyz1-1.xx&_nc_gid=I01Huqn8cRYQWCF5daV0fw&_nc_ss=7f2a8&oh=00_AQDrBcwEvZHdYqd9spbMH4nzFS0cAnJtwO-FuyEAgUC8XQ&oe=6A683EFF'
},
]

# dedupe check against existing links (safety)
existing_links = {r['lien'] for r in rows}
added = 0
for nr in new_rows:
    if nr['lien'] not in existing_links:
        rows.append(nr)
        added += 1

def sort_key(r):
    is_new = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        score = -int(r['score'])
    except:
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Added {added} new rows. Total rows now: {len(rows)}")
