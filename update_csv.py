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
 'date_ajout': '2026-07-22', 'statut': 'NOUVEAU',
 'titre': 'Grand 4½ (900 pi²) avec balcon, électros et climatisation inclus - Hochelaga-Maisonneuve',
 'quartier': 'Hochelaga-Maisonneuve',
 'adresse': 'n/d (Montréal, QC H1W 3N5)',
 'prix': '1900', 'superficie_pi2': '900', 'chambres': '2', 'balcon': 'oui',
 'station_metro': 'Joliette ou Pie-IX (à vérifier)', 'ligne_metro': 'verte', 'minutes_a_pied': '10 (estimé)',
 'site': 'Kijiji', 'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-4-1-2-avec-balcon-electros-ac-inclus/1740573339',
 'score': '8',
 'notes': "Grand balcon arrière avec vue sur jardin, thermopompe (chauffage/climatisation) incluse, tous électros et internet inclus, non-fumeur, aucun animal, vérification de crédit requise, disponible 1er août 2026",
 'photo': ''
},
{
 'date_ajout': '2026-07-22', 'statut': 'NOUVEAU',
 'titre': 'Grand 4½ (3 chambres) - avenue Bourbonnière (Hochelaga-Maisonneuve)',
 'quartier': 'Hochelaga-Maisonneuve',
 'adresse': '1419, Avenue Bourbonnière, Montréal',
 'prix': '2200', 'superficie_pi2': 'n/d', 'chambres': '3', 'balcon': 'n/d',
 'station_metro': 'Joliette (estimé)', 'ligne_metro': 'verte', 'minutes_a_pied': '10 (estimé)',
 'site': 'Centris', 'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/14219826',
 'score': '5',
 'notes': "Prix promotionnel 2200$ pour bail 12 mois (régulier 2400$), disponible 3 jours après acceptation, à 5 min en bus (métro estimé à pied) du métro Pie-IX, près Super C et Marché Métro",
 'photo': ''
},
{
 'date_ajout': '2026-07-22', 'statut': 'NOUVEAU',
 'titre': 'Grand 3 chambres - Place Victor-Bourgeau (Rosemont), à 7 min du métro Pie-IX',
 'quartier': 'Rosemont-La Petite-Patrie',
 'adresse': '3827, Place Victor-Bourgeau, app. 2e étage, Montréal',
 'prix': '1950', 'superficie_pi2': 'n/d', 'chambres': '3', 'balcon': 'n/d',
 'station_metro': 'Pie-IX', 'ligne_metro': 'verte', 'minutes_a_pied': '7',
 'site': 'Centris', 'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/10515269',
 'score': '5',
 'notes': "Walk Score 92, quartier calme et verdoyant, immeuble de 1950, disponible 1er juin 2026",
 'photo': ''
},
{
 'date_ajout': '2026-07-22', 'statut': 'NOUVEAU',
 'titre': '4 pièces, 2 chambres avec balcon privé - rue Drolet (Plateau/Mile-End)',
 'quartier': 'Le Plateau-Mont-Royal',
 'adresse': '4868, Rue Drolet, Montréal',
 'prix': '2095', 'superficie_pi2': 'n/d', 'chambres': '2', 'balcon': 'oui',
 'station_metro': 'Laurier (estimé)', 'ligne_metro': 'orange', 'minutes_a_pied': '6 (estimé)',
 'site': 'Centris', 'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-le-plateau-mont-royal/12638852',
 'score': '5',
 'notes': "Semi-meublé, non-fumeurs, Walk Score 100, 2e étage, disponible 1er août 2026, superficie non précisée",
 'photo': ''
},
{
 'date_ajout': '2026-07-22', 'statut': 'NOUVEAU',
 'titre': '2 chambres (1080 pi²), sous-sol rénové - rue Marie-Anne Est (Plateau)',
 'quartier': 'Le Plateau-Mont-Royal',
 'adresse': '2484, Rue Marie-Anne Est, app. 1, Montréal',
 'prix': '2075', 'superficie_pi2': '1080', 'chambres': '2', 'balcon': 'n/d',
 'station_metro': 'Mont-Royal ou Frontenac (à vérifier)', 'ligne_metro': 'orange', 'minutes_a_pied': '8 (estimé)',
 'site': 'Centris', 'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-le-plateau-mont-royal/14193012',
 'score': '5',
 'notes': "Unité en sous-sol (condo sur 2 niveaux), animaux non acceptés, Walk Score 97, disponible 1er sept 2026",
 'photo': ''
},
{
 'date_ajout': '2026-07-22', 'statut': 'NOUVEAU',
 'titre': 'Condo 2 chambres, finitions haut de gamme - rue Durocher (Plateau), à 9 min du métro Place-des-Arts',
 'quartier': 'Le Plateau-Mont-Royal',
 'adresse': '3518, Rue Durocher, app. 303, Montréal',
 'prix': '2150', 'superficie_pi2': 'n/d', 'chambres': '2', 'balcon': 'n/d',
 'station_metro': 'Place-des-Arts', 'ligne_metro': 'verte', 'minutes_a_pied': '9',
 'site': 'Centris', 'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-le-plateau-mont-royal/28667761',
 'score': '4',
 'notes': "Finitions italiennes haut de gamme, entrée privée, vue sur parc, immeuble sécurisé (interphone/caméras), Walk Score 99, disponible 1 jour après acceptation, secteur Milton-Parc/McGill",
 'photo': ''
},
{
 'date_ajout': '2026-07-22', 'statut': 'NOUVEAU',
 'titre': '2 chambres avec terrasse privée - rue Boyer (Villeray), à 5 min du métro Jean-Talon',
 'quartier': 'Villeray',
 'adresse': '7236, Rue Boyer, Montréal',
 'prix': '2300', 'superficie_pi2': 'n/d', 'chambres': '2', 'balcon': 'oui',
 'station_metro': 'Jean-Talon', 'ligne_metro': 'orange/bleue', 'minutes_a_pied': '5',
 'site': 'Centris', 'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/25783192',
 'score': '5',
 'notes': "Terrasse privée spacieuse, exposition sud-ouest, 2e étage, salle de bain rénovée, animaux non acceptés, semi-meublé, disponible 1er juillet 2026",
 'photo': ''
},
{
 'date_ajout': '2026-07-22', 'statut': 'NOUVEAU',
 'titre': 'Spacieux 4½ rénové, 2 chambres - avenue Henri-Julien (Plateau), à 2 min du métro Laurier',
 'quartier': 'Le Plateau-Mont-Royal',
 'adresse': '5010, Avenue Henri-Julien, Montréal',
 'prix': '2000', 'superficie_pi2': 'n/d', 'chambres': '2', 'balcon': 'n/d',
 'station_metro': 'Laurier', 'ligne_metro': 'orange', 'minutes_a_pied': '2',
 'site': 'Centris', 'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-le-plateau-mont-royal/13104221',
 'score': '3',
 'notes': "Cuisine et salle de bain rénovées, hauts plafonds, immeuble de 1910, chats acceptés, disponible 7 jours après acceptation, Walk Score 99",
 'photo': ''
},
{
 'date_ajout': '2026-07-22', 'statut': 'NOUVEAU',
 'titre': '4½ avec cour arrière privée - rue Rivard (Plateau), à quelques pas du métro Mont-Royal',
 'quartier': 'Le Plateau-Mont-Royal',
 'adresse': '4452, Rue Rivard, Montréal',
 'prix': '2000', 'superficie_pi2': 'n/d', 'chambres': '2', 'balcon': 'non',
 'station_metro': 'Mont-Royal', 'ligne_metro': 'orange', 'minutes_a_pied': '3 (estimé)',
 'site': 'Centris', 'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-le-plateau-mont-royal/14560801',
 'score': '3',
 'notes': "Cour arrière privée, lumineux et bien entretenu, Walk Score 100, animaux acceptés sous conditions, disponible 1er août 2026",
 'photo': ''
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
