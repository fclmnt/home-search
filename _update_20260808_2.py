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
        'date_ajout': '2026-08-08',
        'statut': 'NOUVEAU',
        'titre': "5½ (2 chambres fermées + bureau fermé), 940 pi², balcons avant/arrière - rue St-André (Villeray), à 8 min du métro Jarry",
        'quartier': 'Villeray',
        'adresse': '7647, Rue St-André, Montréal',
        'prix': '2000',
        'superficie_pi2': '940',
        'chambres': '2',
        'balcon': 'oui',
        'station_metro': 'Jarry',
        'ligne_metro': 'orange',
        'minutes_a_pied': '8 (estime, ~655 m)',
        'site': 'LogisQuebec',
        'lien': 'https://www.logisquebec.com/appartement-a-louer-villeray_saint-michel_parc-extension-l356503',
        'score': '7',
        'notes': "2e etage de duplex, 2 chambres fermees + bureau ferme, cuisine et salle de bain renovees, 5 electromenagers inclus (frigo/cuisiniere/lave-vaisselle/laveuse/secheuse), thermopompe murale, disponible immediatement. Jean-Talon aussi a ~819 m.",
        'photo': '',
    },
    {
        'date_ajout': '2026-08-08',
        'statut': 'NOUVEAU',
        'titre': "4½ renove (2 chambres), 989 pi², balcon arriere - avenue Papineau, app. 202 (Villeray), en face du metro Fabre",
        'quartier': 'Villeray',
        'adresse': '7145, Avenue Papineau, app. 202, Montreal',
        'prix': '2095',
        'superficie_pi2': '989',
        'chambres': '2',
        'balcon': 'oui',
        'station_metro': 'Fabre',
        'ligne_metro': 'bleue',
        'minutes_a_pied': '1-2',
        'site': 'Centris',
        'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/11982280',
        'score': '7',
        'notes': "Balcon arriere, ascenseur, terrasse commune sur le toit, insonorisation beton, stationnement optionnel (100$/mois), disponible 1er aout 2026. Meme immeuble qu'une autre unite (app. 209) deja repertoriee a un prix different.",
        'photo': '',
    },
    {
        'date_ajout': '2026-08-08',
        'statut': 'NOUVEAU',
        'titre': "5½ renove (2-3 chambres), secteur Marche Maisonneuve - rue Nicolet (Hochelaga), pres metro Joliette",
        'quartier': 'Hochelaga-Maisonneuve',
        'adresse': '603, Rue Nicolet, Montreal',
        'prix': '1900',
        'superficie_pi2': 'n/d',
        'chambres': '2',
        'balcon': 'n/d',
        'station_metro': 'Joliette (estime)',
        'ligne_metro': 'verte',
        'minutes_a_pied': '7 (estime, a verifier)',
        'site': 'Centris',
        'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/12296918',
        'score': '6',
        'notes': "Grande cuisine avec 5 electromenagers inclus, semi-meuble, aucun animal, proche Marche Maisonneuve/Stade Olympique/autoroute 720, Walk Score 93, disponible 15 jours apres acceptation. Superficie et balcon non precises par l'annonce ; fiche Centris indique 2 chambres mais decrit un 5½ (a valider).",
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

print('done, total rows now', len(rows))
