import csv

path = 'annonces.csv'
with open(path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
data = rows[1:]

for r in data:
    if r[1] == 'NOUVEAU':
        r[1] = 'vu'

new_rows = [
    [
        '2026-08-14', 'NOUVEAU',
        'Villeray 5 1/2 + coin bureau, rénové - à 5 min du métro Jarry',
        'Villeray',
        'n/d (secteur Villeray, Montréal, QC H2R)',
        '1900', '1000', '2', 'non', 'Jarry', 'orange', '5',
        'Kijiji',
        'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/villeray-5-1-2-coin-bureau-5-min-du-metro-jarry/1741938769',
        '5',
        "Renovation recente (planchers, cuisine avec ilot), chambre principale avec walk-in, 2e chambre fermee avec grand rangement, coin bureau distinct, porte-patio vers cour arriere (pas de balcon), thermopompe, 5 electromenagers inclus, non meuble, aucun animal, disponible 1er sept. 2026, bail 1 an",
        '',
    ],
    [
        '2026-08-14', 'NOUVEAU',
        '6 1/2 avec cachet ancien, rue Mont-Royal - à 2 min à pied du métro Mont-Royal',
        'Le Plateau-Mont-Royal',
        'n/d (rue Mont-Royal, Montréal, QC H2J 1X1)',
        '2300', '1300', '3', 'n/d', 'Mont-Royal', 'orange', '2',
        'Kijiji',
        'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/plateau-mont-royal-6-a-louer-a-2-minutes-a-pied-du-metro-mont/1741701265',
        '7',
        "6 1/2 avec cachet ancien, double salon (salle a manger) pouvant servir de bureau ou 2e espace fermable, buanderie et rangement inclus, animaux acceptes, non meuble, fumeur exterieur seulement, disponible 1er sept. 2026, Walk/Transit/Bike Score 10/10/10",
        '',
    ],
    [
        '2026-08-14', 'NOUVEAU',
        '5 1/2 en plein cœur de Ville-Marie/Centre-Sud, près du métro Papineau (Marketplace)',
        'Centre-Sud (limitrophe Hochelaga, arrondissement Ville-Marie)',
        'n/d (secteur Ontario/Papineau, Montréal, QC)',
        '1920', 'n/d', '2', 'oui', 'Papineau (estimé)', 'verte', '10 (estimé)',
        'Marketplace',
        'https://www.facebook.com/marketplace/item/4460325497556044',
        '6',
        "Grande chambre principale + petite chambre fermee + espace bureau (porte francaise, non ferme), grande cuisine et grande terrasse, thermopompe, animaux non acceptes, non-fumeur, secteur tres bien note (Walk Score 99), a proximite des commerces de la rue Ontario/Papineau. Lien Facebook (connexion requise) pour plus de details.",
        'https://scontent-yyz1-1.xx.fbcdn.net/v/t39.30808-6/774099767_4498890010437618_4371530889131076939_n.jpg?stp=c0.169.1537.1537a_dst-jpg_tt6&cstp=mx1537x1537&ctp=s565x565&_nc_cat=108&ccb=1-7&_nc_sid=454cf4&_nc_ohc=XAIM3pOBL0oQ7kNvwFUx3E6&_nc_oc=Adpu3TSlDU1QiYfl5sq84OBwkul8LEwGj9KK2o-QufiCUX1RxADzZkeWk8qowJ_6DnQ&_nc_zt=23&_nc_ht=scontent-yyz1-1.xx&_nc_gid=M0wLFCq9_PHDdapIdcxiPw&_nc_ss=7f2a8&oh=00_AQFBHin6QjLt_2gCXpq9cl3H_ncdyJbaP6NmXM7EVAWmow&oe=6A853B95',
    ],
]

data.extend(new_rows)

def sort_key(r):
    statut_rank = 0 if r[1] == 'NOUVEAU' else 1
    try:
        score = -int(r[14])
    except (ValueError, IndexError):
        score = 0
    return (statut_rank, score)

data.sort(key=sort_key)

with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(header)
    writer.writerows(data)

print('done', len(data), 'rows')
