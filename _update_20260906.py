import csv

rows = []
with open('annonces.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        if row['statut'] == 'NOUVEAU':
            row['statut'] = 'vu'
        rows.append(row)

new_rows = [
{
    'date_ajout': '2026-09-06',
    'statut': 'NOUVEAU',
    'titre': "6 pièces (3 chambres), 1450 pi² - Rue Cartier (Rosemont/La Petite-Patrie), à 8-9 min du métro Beaubien",
    'quartier': 'Rosemont-La Petite-Patrie',
    'adresse': '5628, Rue Cartier, Montréal',
    'prix': '1925',
    'superficie_pi2': '1450',
    'chambres': '3',
    'balcon': 'n/d',
    'station_metro': 'Beaubien',
    'ligne_metro': 'orange',
    'minutes_a_pied': '8-9 (estimé)',
    'site': 'Centris',
    'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/11586670',
    'score': '7',
    'notes': "Animaux non acceptés, fumeurs non acceptés, libre 10 jours après acceptation, Walk Score 94, année de construction inconnue",
    'photo': '',
},
{
    'date_ajout': '2026-09-06',
    'statut': 'NOUVEAU',
    'titre': "4½ rénové (2 chambres, 1000 pi²), balcon - Villeray, à quelques minutes du métro Jarry",
    'quartier': 'Villeray',
    'adresse': '7770, Avenue Casgrain, Montréal',
    'prix': '2300',
    'superficie_pi2': '1000',
    'chambres': '2',
    'balcon': 'oui',
    'station_metro': 'Jarry',
    'ligne_metro': 'orange',
    'minutes_a_pied': '5-8 (estimé)',
    'site': 'Kijiji',
    'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/4-entierement-renove-villeray-2-salles-de-bain-2-300-mois/1742993259',
    'score': '7',
    'notes': "Cuisine neuve (îlot, quartz), 2 salles de bain neuves, planchers bois franc, laveuse-sécheuse, climatisation, animaux acceptés, chauffage non inclus, libre 1er nov. 2026",
    'photo': '',
},
{
    'date_ajout': '2026-09-06',
    'statut': 'NOUVEAU',
    'titre': "4½ (2 chambres, 1000 pi²), balcon privé - Mile End/Plateau, à 10 min du métro Mont-Royal",
    'quartier': 'Le Plateau-Mont-Royal',
    'adresse': 'Secteur Mont-Royal / Saint-Laurent (adresse exacte communiquée sur demande), Montréal',
    'prix': '2160',
    'superficie_pi2': '1000',
    'chambres': '2',
    'balcon': 'oui',
    'station_metro': 'Mont-Royal',
    'ligne_metro': 'orange',
    'minutes_a_pied': '10 (estimé)',
    'site': 'Kijiji',
    'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/4-1-2-mile-end-plateau-mont-royal-for-october-1st-or-earlier/1741226751',
    'score': '7',
    'notes': "Eau incluse, animaux acceptés, garde-robes dans les 2 chambres, libre 1er sept. (flexible jusqu'à début oct.), quartier très commerçant",
    'photo': '',
},
]

rows = new_rows + rows

def sort_key(r):
    is_new = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        score = -float(r['score'])
    except (ValueError, TypeError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("done, total rows:", len(rows))
