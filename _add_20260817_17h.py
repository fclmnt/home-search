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
        'date_ajout': '2026-08-17',
        'statut': 'NOUVEAU',
        'titre': "5½ rénové (3 chambres), 1000 pi², balcon arrière - rue Saint-Dominique (Plateau-Mont-Royal), à 10 min du métro Sherbrooke",
        'quartier': 'Le Plateau-Mont-Royal',
        'adresse': '3477, Rue Saint-Dominique, Montréal, QC',
        'prix': '2100',
        'superficie_pi2': '1000',
        'chambres': '3',
        'balcon': 'oui',
        'station_metro': 'Sherbrooke',
        'ligne_metro': 'verte',
        'minutes_a_pied': '10',
        'site': 'DuProprio',
        'lien': 'https://duproprio.com/fr/location/montreal/le-plateau-mont-royal/5-1-2-a-louer/hab-3477-rue-saint-dominique-1130024',
        'score': '9',
        'notes': "2e étage, électroménagers inclus (four, frigo, laveuse-sécheuse), à distance de marche du boul. Saint-Laurent, bars/restaurants/parcs, disponible 19 août 2026, politique animaux non précisée.",
        'photo': '',
    },
    {
        'date_ajout': '2026-08-17',
        'statut': 'NOUVEAU',
        'titre': "Grand 5½ (2 chambres + bureau), 2 balcons, cession de bail - rue De Bordeaux (Plateau, près parc Lafontaine)",
        'quartier': 'Le Plateau-Mont-Royal',
        'adresse': 'n/d (secteur Rue De Bordeaux près du parc Lafontaine, Montréal, QC)',
        'prix': '1985',
        'superficie_pi2': 'n/d',
        'chambres': '2',
        'balcon': 'oui (2 balcons)',
        'station_metro': 'Papineau (estimé)',
        'ligne_metro': 'verte',
        'minutes_a_pied': '10-12 (estimé)',
        'site': 'Marketplace',
        'lien': 'https://www.facebook.com/marketplace/item/1983962432308889',
        'score': '6',
        'notes': "Cession de bail au loyer actuel de 1985$ jusqu'en juin 2027, bureau fermé additionnel, frigo/cuisinière/laveuse-sécheuse inclus, animaux non acceptés, chauffage/électricité non inclus, disponible 1er octobre 2026, à 2-3 min du parc Lafontaine. Distance au métro estimée (non confirmée par l'annonce). Lien Facebook (connexion requise).",
        'photo': 'https://scontent-ord5-1.xx.fbcdn.net/v/t39.84726-6/774018503_1823419532347863_7577712837293895190_n.jpg?stp=c90.0.540.540a_dst-jpg_p180x540_tt6&_nc_cat=109&ccb=1-7&_nc_sid=92e707&_nc_ohc=xMe3HP-O0YwQ7kNvwEazl2d&_nc_oc=AdoqZRQvUiZLh6qN-vLQZ5vcK7urX1Q7IGKAFpXk2l3IvLTKN2wj_rJNETw86Udb27M&_nc_zt=14&_nc_ht=scontent-ord5-1.xx&_nc_gid=jEymNZoMaE4FjQWd5vXvqQ&_nc_ss=7f2a8&oh=00_AQGsaACExKt5xcVIA_fjCmOf63bZN-eD9wDMAt1mYL2esQ&oe=6A895D5E',
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

with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print('total rows:', len(rows))
print('nouveau rows:', sum(1 for r in rows if r['statut'] == 'NOUVEAU'))
