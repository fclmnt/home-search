import csv

FIELDS = ['date_ajout','statut','titre','quartier','adresse','prix','superficie_pi2',
          'chambres','balcon','station_metro','ligne_metro','minutes_a_pied','site',
          'lien','score','notes','photo']

with open('annonces.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'

new_rows = [
    {
        'date_ajout': '2026-08-08',
        'statut': 'NOUVEAU',
        'titre': "4½ rénové (2 chambres fermées), 900 pi² - rue Panet (Centre-Sud), à ~3 min du métro Beaudry",
        'quartier': 'Ville-Marie (Centre-Sud)',
        'adresse': '1278, Rue Panet, Montréal, QC H2L 2Y8',
        'prix': '2200',
        'superficie_pi2': '900',
        'chambres': '2',
        'balcon': 'n/d',
        'station_metro': 'Beaudry',
        'ligne_metro': 'verte',
        'minutes_a_pied': '3',
        'site': 'Marketplace',
        'lien': 'https://www.facebook.com/marketplace/item/1661806952618975',
        'score': '6',
        'notes': "Climatisation murale (mini-split), chauffage electrique, laveuse-secheuse et electromenagers inclus, salle de bain refaite (ceramique blanche, style subway), chats acceptes. Attention : la fiche affiche 2200$ mais le texte de la description mentionne 2300$/mois, a valider avant de contacter. Station Beaudry a environ 267 m (Walk Score). Lien Facebook (connexion requise).",
        'photo': 'https://scontent-yyz1-1.xx.fbcdn.net/v/t39.84726-6/741454032_1038070832060783_549839444418073514_n.jpg?stp=c135.0.540.540a_dst-jpg_p180x540_tt6&_nc_cat=111&ccb=1-7&_nc_sid=92e707&_nc_ohc=PVPFRqJoIOwQ7kNvwFDCnJn&_nc_oc=AdocfsZfD7staQgLh9OYjdqpS6aFuyxyzwKGz-l8Fy7_F--WLr9pxfmCjra-9MAQp1w&_nc_zt=14&_nc_ht=scontent-yyz1-1.xx&_nc_gid=FcVGu1aZywPT9hzyS_kBsQ&_nc_ss=7f2a8&oh=00_AQExwbSA0OhZjYoguNyQ77SsuN5K2SIvYcYSqzfZYqv8xg&oe=6A7D0436',
    },
    {
        'date_ajout': '2026-08-08',
        'statut': 'NOUVEAU',
        'titre': "5½ rénové (2 chambres fermées), 900 pi², terrasse et jardin privés - rue Parthenais (Plateau-Mont-Royal), près métro Laurier",
        'quartier': 'Le Plateau-Mont-Royal',
        'adresse': 'Rue Parthenais (entre Gilford et Saint-Joseph), Montréal, QC H2H 2H1',
        'prix': '2080',
        'superficie_pi2': '900',
        'chambres': '2',
        'balcon': 'oui',
        'station_metro': 'Laurier',
        'ligne_metro': 'orange',
        'minutes_a_pied': 'n/d (estime ~5 min)',
        'site': 'Kijiji',
        'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/5-1-2-apartment-for-rent-plateau-mont-royal/1741275574',
        'score': '7',
        'notes': "Unite au rez-de-chaussee, terrasse et jardin prives, planchers chauffants en ceramique, climatisation incluse, laveuse-secheuse et lave-vaisselle, 1 place de stationnement incluse, animaux limites, non-fumeur (a l'exterieur seulement), bail 1 an, disponible 15 septembre 2026.",
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
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    w.writerows(rows)

print('total rows:', len(rows))
print('nouveau count:', sum(1 for r in rows if r['statut'] == 'NOUVEAU'))
