import csv

with open('annonces.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'

new_rows = [
{
 'date_ajout': '2026-07-27',
 'statut': 'NOUVEAU',
 'titre': 'Grand 6½ rénové, 3 chambres fermées, 2 balcons, 1250 pi² - Villeray (à 3 min du métro Jarry)',
 'quartier': 'Villeray',
 'adresse': "n/d (Montréal, QC H2R 2E8)",
 'prix': '2400',
 'superficie_pi2': '1250',
 'chambres': '3',
 'balcon': 'oui',
 'station_metro': 'Jarry',
 'ligne_metro': 'orange',
 'minutes_a_pied': '3',
 'site': 'Kijiji',
 'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-6-1-2-villeray-metro-jarry/1741040354',
 'score': '9',
 'notes': "2 balcons (avant et grand balcon arriere), tres proche du metro Jarry, bon rapport superficie/prix. Date de disponibilite et politique animaux non precisees par l'annonce.",
 'photo': '',
},
{
 'date_ajout': '2026-07-27',
 'statut': 'NOUVEAU',
 'titre': '4½ rénové, 2 chambres fermées, balcon, 950 pi² - Mile-End (Plateau), à ~10 min du métro Outremont',
 'quartier': 'Le Plateau-Mont-Royal',
 'adresse': "5970, Avenue du Parc, app. 7, Montréal",
 'prix': '2300',
 'superficie_pi2': '950',
 'chambres': '2',
 'balcon': 'oui',
 'station_metro': 'Outremont',
 'ligne_metro': 'bleue',
 'minutes_a_pied': "10 (estime, non precise par l'annonce)",
 'site': 'DuProprio',
 'lien': 'https://duproprio.com/en/rental/montreal/le-plateau-mont-royal/4-1-2-for-rent/hab-7-5970-ave-du-parc-1138366',
 'score': '7',
 'notes': "Dernier etage (3e), semi-meuble, stationnement exterieur inclus, disponible 1er septembre 2026. Secteur Mile-End (bordure Plateau/Outremont), distance au metro estimee.",
 'photo': '',
},
{
 'date_ajout': '2026-07-27',
 'statut': 'NOUVEAU',
 'titre': 'Grand condo 4 chambres fermées - rue Jean-Talon Ouest (Villeray), à ~5 min du métro Acadie',
 'quartier': 'Villeray',
 'adresse': "816, Rue Jean-Talon Ouest, Montréal",
 'prix': '2300',
 'superficie_pi2': 'n/d',
 'chambres': '4',
 'balcon': 'n/d',
 'station_metro': 'Acadie',
 'ligne_metro': 'bleue',
 'minutes_a_pied': '5-6 (estime)',
 'site': 'Centris',
 'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/25680514',
 'score': '4',
 'notes': "7 pieces / 4 chambres fermees, 2 salles de bain, animaux acceptes sous conditions, disponible 1er juillet 2026, visite virtuelle 3D. Superficie non precisee par la fiche ; balcon non mentionne.",
 'photo': '',
},
]

rows.extend(new_rows)

def sort_key(r):
    try:
        score = int(r['score'])
    except (ValueError, TypeError):
        score = 0
    return (0 if r['statut'] == 'NOUVEAU' else 1, -score)

rows.sort(key=sort_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("done", len(rows))
