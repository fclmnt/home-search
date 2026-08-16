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
        'date_ajout': '2026-08-16',
        'statut': 'NOUVEAU',
        'titre': '5½ meublé (3 chambres), 2 balcons - 13e Avenue (Villeray), à 2 min du métro Saint-Michel',
        'quartier': 'Villeray-Saint-Michel-Parc-Extension',
        'adresse': 'n/d (13e Avenue, Montréal, QC)',
        'prix': '2250',
        'superficie_pi2': 'n/d',
        'chambres': '3',
        'balcon': 'oui (2 balcons)',
        'station_metro': 'Saint-Michel',
        'ligne_metro': 'bleue',
        'minutes_a_pied': '2',
        'site': 'Logis Québec',
        'lien': 'https://www.logisquebec.com/appartement-a-louer-villeray_saint-michel_parc-extension-l357748',
        'score': '6',
        'notes': "Meuble, cuisine avec quartz, laveuse-secheuse incluse, bureau de travail dans chaque chambre, non-fumeur, aucun animal, disponible immediatement jusqu'au 30 juin 2027, verification de credit et references exigees.",
        'photo': '',
    },
    {
        'date_ajout': '2026-08-16',
        'statut': 'NOUVEAU',
        'titre': '6½ meublé (3 chambres), balcon - rue Saint-Denis (Plateau), à deux pas du métro Laurier',
        'quartier': 'Le Plateau-Mont-Royal',
        'adresse': '5061, Rue Saint-Denis, Montréal, QC',
        'prix': '2000',
        'superficie_pi2': '1000',
        'chambres': '3',
        'balcon': 'oui',
        'station_metro': 'Laurier',
        'ligne_metro': 'orange',
        'minutes_a_pied': '5-7 (estime, annonce indique a deux pas)',
        'site': 'Kijiji',
        'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/6-1-2-meuble-3-cac-metro-laurier/1742053461',
        'score': '8',
        'notes': "Meuble, climatisation, eau incluse, chauffage electrique en sus, buanderie dans l'immeuble, animaux limites, bail 1 an, disponible 15 aout 2026.",
        'photo': '',
    },
    {
        'date_ajout': '2026-08-16',
        'statut': 'NOUVEAU',
        'titre': '4½ (2 chambres), 1060 pi², balcon - secteur Saint-Laurent/Villeneuve, Plateau-Mont-Royal',
        'quartier': 'Le Plateau-Mont-Royal',
        'adresse': 'n/d (secteur boul. Saint-Laurent / rue Villeneuve / av. Mont-Royal, Montréal, QC H2T 1R2)',
        'prix': '2000',
        'superficie_pi2': '1060',
        'chambres': '2',
        'balcon': 'oui',
        'station_metro': 'Mont-Royal',
        'ligne_metro': 'orange',
        'minutes_a_pied': '10 (estime)',
        'site': 'Kijiji',
        'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/4-5-a-louer-for-rent-a-montreal/1742024029',
        'score': '7',
        'notes': "Cuisine et salle de bain renovees, laveuse-secheuse et lave-vaisselle inclus, Walk Score 10, aucun animal, bail 1 an, disponible 1er septembre 2026, adresse exacte non fournie par l'annonceur.",
        'photo': '',
    },
]

rows.extend(new_rows)

def sort_key(r):
    is_new = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        score = -int(r['score'])
    except (ValueError, TypeError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Total rows:", len(rows))
print("NOUVEAU:", sum(1 for r in rows if r['statut'] == 'NOUVEAU'))
