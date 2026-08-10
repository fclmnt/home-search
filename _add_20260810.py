import csv

with open('annonces.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

for row in rows:
    if row['statut'] == 'NOUVEAU':
        row['statut'] = 'vu'

new_rows = [
    {
        'date_ajout': '2026-08-10',
        'statut': 'NOUVEAU',
        'titre': "5½ (3 chambres) avec balcons avant/arrière, cour privée - avenue Jeanne-d'Arc, à 6 min du métro Joliette",
        'quartier': 'Rosemont/La Petite-Patrie',
        'adresse': "5491, Avenue Jeanne-d'Arc, app. 2, Montréal, QC",
        'prix': '2000',
        'superficie_pi2': 'n/d',
        'chambres': '3',
        'balcon': 'oui',
        'station_metro': 'Joliette',
        'ligne_metro': 'verte',
        'minutes_a_pied': '6',
        'site': 'Centris',
        'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/13330410',
        'score': '',
        'notes': "Balcons avant et arrière, cour privée, cuisine spacieuse, proche parc Maisonneuve et Jardin botanique, animaux non acceptés, libre 13 juillet 2026.",
        'photo': '',
    },
    {
        'date_ajout': '2026-08-10',
        'statut': 'NOUVEAU',
        'titre': "Grand 7½ (4 chambres, 1500 pi²) avec 2 balcons + terrasse privée - avenue Ogilvy, à 5 min du métro Parc",
        'quartier': 'Villeray',
        'adresse': '826, Avenue Ogilvy, Montréal, QC',
        'prix': '2100',
        'superficie_pi2': '1500',
        'chambres': '4',
        'balcon': 'oui',
        'station_metro': 'Parc',
        'ligne_metro': 'bleue',
        'minutes_a_pied': '5',
        'site': 'Centris',
        'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/10316417',
        'score': '',
        'notes': "3e étage, immeuble rénové, 2 balcons + grande terrasse privée arrière (~500 pi²), chauffage électrique, électroménagers inclus (frigo, cuisinière, laveuse-sécheuse), stationnement rue, libre 1er juillet 2026.",
        'photo': '',
    },
    {
        'date_ajout': '2026-08-10',
        'statut': 'NOUVEAU',
        'titre': "3+1 chambres (1200 pi²) avec sous-sol aménagé et stationnement - avenue De Lorimier, à 6 min du métro D'Iberville",
        'quartier': 'Villeray',
        'adresse': '7183, Avenue De Lorimier, Montréal, QC',
        'prix': '2350',
        'superficie_pi2': '1200',
        'chambres': '4',
        'balcon': 'n/d',
        'station_metro': "D'Iberville",
        'ligne_metro': 'bleue',
        'minutes_a_pied': '6',
        'site': 'Centris',
        'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/19997673',
        'score': '',
        'notes': "Unité au rez-de-chaussée, sous-sol entièrement aménagé (salle familiale, chambre supplémentaire, rangement, buanderie), 1 place de stationnement incluse, Walk Score 97, libre 1er juillet 2026.",
        'photo': '',
    },
    {
        'date_ajout': '2026-08-10',
        'statut': 'NOUVEAU',
        'titre': "5½ (3 chambres, 1200 pi²) avec grande terrasse privée - rue Saint-Zotique Est, à 6 min du métro Beaubien",
        'quartier': 'Rosemont/La Petite-Patrie',
        'adresse': '3240, Rue Saint-Zotique Est, Montréal, QC',
        'prix': '2350',
        'superficie_pi2': '1200',
        'chambres': '3',
        'balcon': 'oui',
        'station_metro': 'Beaubien',
        'ligne_metro': 'orange',
        'minutes_a_pied': '6',
        'site': 'Kijiji',
        'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/7-et-demi-rosemont-grande-terrasse-electros-parking/1740727544',
        'score': '',
        'notes': "Rez-de-chaussée, grande terrasse privée, 2 places de stationnement en tandem, thermopompe/climatisation, chats et petits chiens acceptés, loyer 2350$ an 1 (2450$ an 2 / 2595$ an 3 si renouvellement), libre 3 août 2026.",
        'photo': '',
    },
]

def score(row):
    s = 0
    sup = row['superficie_pi2']
    if sup != 'n/d':
        sup = int(sup)
        if sup >= 1100:
            s += 3
        elif sup >= 900:
            s += 2
    ch = int(row['chambres'])
    if ch >= 3:
        s += 2
    elif ch == 2:
        s += 1
    if row['balcon'] == 'oui':
        s += 2
    if row['minutes_a_pied'] not in ('', 'n/d'):
        mins = int(row['minutes_a_pied'])
        if mins <= 12:
            if row['ligne_metro'] == 'verte':
                s += 2
            else:
                s += 1
    s += 1
    return s

for r in new_rows:
    r['score'] = str(score(r))

rows = new_rows + rows

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("done, total rows:", len(rows))
for r in new_rows:
    print(r['score'], r['titre'][:50])
