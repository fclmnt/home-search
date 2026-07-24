import csv

FIELDS = ['date_ajout','statut','titre','quartier','adresse','prix','superficie_pi2',
          'chambres','balcon','station_metro','ligne_metro','minutes_a_pied','site',
          'lien','score','notes','photo']

with open('annonces.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

# 1. Old NOUVEAU -> vu
for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'

new_rows = [
    {
        'date_ajout': '2026-07-24',
        'statut': 'NOUVEAU',
        'titre': "4½ rénové, terrasse et jardin privés, 900 pi² - Hochelaga-Maisonneuve, entre métro Joliette et Pie-IX",
        'quartier': 'Hochelaga-Maisonneuve',
        'adresse': '1693, Avenue Bourbonnière, Montréal, QC H1W 3N5',
        'prix': '1990',
        'superficie_pi2': '900',
        'chambres': '2',
        'balcon': 'oui',
        'station_metro': 'Joliette',
        'ligne_metro': 'verte',
        'minutes_a_pied': '8',
        'site': 'Marketplace',
        'lien': 'https://www.facebook.com/marketplace/item/1034802492591491',
        'score': '8',
        'notes': "Disponible immédiatement, rez-de-chaussée, terrasse et jardin privatifs, cuisine à aire ouverte rénovée, 2 chambres fermées (dont une sans fenêtre), quartier vivant (Promenade Ontario et Place Simon-Valois à quelques pas, épicerie Metro à 1 min, boulangerie Arhoma à 3 min), lien exige une connexion Facebook",
        'photo': '',
    },
    {
        'date_ajout': '2026-07-24',
        'statut': 'NOUVEAU',
        'titre': "4½ lumineux ~1000 pi², 2 chambres, à 2 min du métro Berri-UQAM - Ville-Marie (Village)",
        'quartier': 'Ville-Marie (Centre-Sud/Village)',
        'adresse': 'Rue St-Christophe, Montréal, QC H2L 3W5',
        'prix': '2065',
        'superficie_pi2': '1000',
        'chambres': '2',
        'balcon': 'oui',
        'station_metro': 'Berri-UQAM',
        'ligne_metro': 'verte',
        'minutes_a_pied': '2',
        'site': 'Marketplace',
        'lien': 'https://www.facebook.com/marketplace/item/1751858266169561',
        'score': '8',
        'notes': "Appartement traversant au 2e étage, climatisation murale, chauffage individuel, cuisine équipée (laveuse-sécheuse, four, lave-vaisselle inclus), terrasses, IGA (Place Dupuis) à 2 min, hydro et internet en sus, disponible 2026-07-31, lien exige une connexion Facebook",
        'photo': '',
    },
    {
        'date_ajout': '2026-07-24',
        'statut': 'NOUVEAU',
        'titre': "4½ rénové meublé tout inclus, 1099 pi², 2 chambres + bureau fermé, 2 balcons - Plateau, 10 min du métro Mont-Royal",
        'quartier': 'Le Plateau-Mont-Royal',
        'adresse': 'Coin Marie-Anne / De La Roche, Montréal, QC H2J 3J2',
        'prix': '2300',
        'superficie_pi2': '1099',
        'chambres': '2',
        'balcon': 'oui',
        'station_metro': 'Mont-Royal',
        'ligne_metro': 'orange',
        'minutes_a_pied': '10',
        'site': 'Kijiji',
        'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/1-octobre-4-1-2-renove-meuble-tout-inclut-a-louer-sur-le-plateau/1740994299',
        'score': '7',
        'notes': "Meublé, tout inclus (chauffage, hydro, eau; internet en sus), plancher chauffant à la salle de bain, climatisation, à 5 min du parc La Fontaine, aucun animal, disponible 2026-10-01",
        'photo': '',
    },
    {
        'date_ajout': '2026-07-24',
        'statut': 'NOUVEAU',
        'titre': "4½ construction récente (2021), terrasse privée, animaux acceptés, 900 pi² - Plateau, 10 min du métro Mont-Royal/Laurier",
        'quartier': 'Le Plateau-Mont-Royal',
        'adresse': '4609, Rue de la Roche, Montréal, QC H2J 3J5',
        'prix': '2265',
        'superficie_pi2': '900',
        'chambres': '2',
        'balcon': 'oui',
        'station_metro': 'Mont-Royal',
        'ligne_metro': 'orange',
        'minutes_a_pied': '10',
        'site': 'Kijiji',
        'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/4-sur-le-plateau-mont-royal-animaux-acceptes/1740915606',
        'score': '7',
        'notes': "Construction récente en béton (2021), tous électroménagers inclus (laveuse-sécheuse, lave-vaisselle, climatisation), grande terrasse privée avec accès cour, immeuble calme, gestion professionnelle, disponible 2026-08-01 (flexible)",
        'photo': '',
    },
]

existing_links = {r['lien'] for r in rows}
for nr in new_rows:
    if nr['lien'] in existing_links:
        raise SystemExit(f"DUPLICATE: {nr['lien']}")

rows.extend(new_rows)

# Sort: NOUVEAU first, then by score desc
def sort_key(r):
    is_nouveau = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        score = -int(r['score'])
    except (ValueError, TypeError):
        score = 0
    return (is_nouveau, score)

rows.sort(key=sort_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    w.writerows(rows)

print(f"Total rows: {len(rows)}, new: {len(new_rows)}")
