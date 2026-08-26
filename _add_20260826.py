import csv

with open('annonces.csv', newline='', encoding='utf-8') as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)

for row in rows:
    if row['statut'] == 'NOUVEAU':
        row['statut'] = 'vu'

new_rows = [
    {
        'date_ajout': '2026-08-26',
        'statut': 'NOUVEAU',
        'titre': '5½ rénové avec balcon, cuisine rénovée - près métro Joliette',
        'quartier': 'Rosemont-La Petite-Patrie',
        'adresse': '4332, Rue Joliette, Montréal',
        'prix': '1900',
        'superficie_pi2': '915',
        'chambres': '2',
        'balcon': 'oui',
        'station_metro': 'Joliette',
        'ligne_metro': 'verte',
        'minutes_a_pied': '3',
        'site': 'Centris',
        'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/11830297',
        'score': '8',
        'notes': 'Semi-meublé, 2e étage, cuisine rénovée, chats acceptés, non-fumeurs, stationnement garage disponible (+200$/mois), libre 1er sept.',
        'photo': '',
    },
    {
        'date_ajout': '2026-08-26',
        'statut': 'NOUVEAU',
        'titre': '3½ chambres à louer, Plateau-Mont-Royal',
        'quartier': 'Le Plateau-Mont-Royal',
        'adresse': '3910, Avenue Henri-Julien, apt. 1, Montréal',
        'prix': '1900',
        'superficie_pi2': 'n/d',
        'chambres': '3',
        'balcon': 'n/d',
        'station_metro': 'Sherbrooke',
        'ligne_metro': 'orange',
        'minutes_a_pied': '8',
        'site': 'Centris',
        'lien': 'https://www.centris.ca/en/condos-apartments~for-rent~montreal-le-plateau-mont-royal/19149920',
        'score': '4',
        'notes': "Courtier immobilier (L'Expert Immobilier P.M.), libre 1er août, pas d'info chauffage/animaux/balcon dans l'annonce.",
        'photo': '',
    },
    {
        'date_ajout': '2026-08-26',
        'statut': 'NOUVEAU',
        'titre': 'Super Condo 4½ tout inclus, meublé',
        'quartier': 'Villeray-Saint-Michel-Parc-Extension',
        'adresse': '7026, Rue Saint-André, Montréal',
        'prix': '2250',
        'superficie_pi2': '950',
        'chambres': '2',
        'balcon': 'n/d',
        'station_metro': 'Jean-Talon',
        'ligne_metro': 'orange',
        'minutes_a_pied': '2',
        'site': 'Logis Québec',
        'lien': 'https://www.logisquebec.com/appartement-a-louer-villeray_saint-michel_parc-extension-l357980',
        'score': '5',
        'notes': 'Entièrement meublé, hydro + wifi + toutes charges incluses, plafonds 12 pi, insonorisé, disponible immédiatement.',
        'photo': '',
    },
    {
        'date_ajout': '2026-08-26',
        'statut': 'NOUVEAU',
        'titre': 'Grand 5½ au niveau de la rue (en rénovation) - Villeray',
        'quartier': 'Villeray',
        'adresse': '8329, Rue St-Denis, Montréal',
        'prix': '2125',
        'superficie_pi2': 'n/d',
        'chambres': '3',
        'balcon': 'n/d',
        'station_metro': 'Jarry',
        'ligne_metro': 'orange',
        'minutes_a_pied': '3',
        'site': 'Marketplace',
        'lien': 'https://www.facebook.com/marketplace/item/1045734174887528',
        'score': '4',
        'notes': "Logement actuellement en rénovation (livré rafraîchi), chauffage inclus, entrée indépendante. Lien Facebook (connexion requise).",
        'photo': 'https://scontent-yyz1-1.xx.fbcdn.net/v/t39.84726-6/777851665_1392285162836899_2586773633785074076_n.jpg?stp=c135.0.540.540a_dst-jpg_p180x540_tt6&_nc_cat=107&ccb=1-7&_nc_sid=92e707&_nc_ohc=bbqkjXEOooUQ7kNvwGCLjF3&_nc_oc=AdqcFQl6IK4Vq6ghSY5Gwq2lHYbKp-DdU9d1587_dNK-lvUnNr1YatumMq7j0GnExkY&_nc_zt=14&_nc_ht=scontent-yyz1-1.xx&_nc_gid=xz3GAY07JF78DVneStR9iQ&_nc_ss=7f2a8&oh=00_AQGYpPqDbvxzZHJaxQpQuKilNWHE6U_FE7M9qHH5BdSoTw&oe=6A949B24',
    },
]

rows.extend(new_rows)

def sort_key(row):
    is_new = 0 if row['statut'] == 'NOUVEAU' else 1
    try:
        score = -int(row['score'])
    except (ValueError, KeyError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)

print('done, total rows:', len(rows))
print('new rows added:', len(new_rows))
