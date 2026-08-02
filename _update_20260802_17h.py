import csv

PATH = 'annonces.csv'

with open(PATH, newline='', encoding='utf-8') as f:
    rows = list(csv.reader(f))

header = rows[0]
body = rows[1:]

# Pass old NOUVEAU rows to vu
for r in body:
    if r[1] == 'NOUVEAU':
        r[1] = 'vu'

new_rows = [
    [
        '2026-08-02', 'NOUVEAU',
        'Grand 3 chambres rénové, 2 balcons - Rosemont Nord',
        'Rosemont-La Petite-Patrie',
        '3227, Rue Saint-Zotique Est, Montréal',
        '2000', '960', '3', 'oui', 'Beaubien', 'orange', '6',
        'Centris',
        'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/26424558',
        '8',
        "Dernier étage d'un triplex dans Rosemont Nord, aire ouverte, cuisine avec grand îlot et comptoirs de quartz, planchers de bois, électroménagers inclus, semi-meublé, animaux acceptés sous conditions, non-fumeur, Walk Score 93, disponible 1er septembre 2026",
        '',
    ],
    [
        '2026-08-02', 'NOUVEAU',
        '4½ neuf avec balcon privé - Le Richmar, Petite Italie',
        'Villeray-Saint-Michel-Parc-Extension',
        '105, Rue Jean-Talon Ouest, app. 204, Montréal',
        '2100', 'n/d', '2', 'oui', 'De Castelnau', 'bleue', 'n/d (estimé proche)',
        'Centris',
        'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/11622239',
        '5',
        "Immeuble neuf « Le Richmar » (74 unités) en Petite Italie, location sur plan (aucune visite physique), 7 pièces au total, salle d'entraînement, terrasse sur le toit avec BBQ, garage intérieur avec bornes de recharge, animaux acceptés sous conditions, disponible 1er octobre 2026, superficie non précisée",
        '',
    ],
    [
        '2026-08-02', 'NOUVEAU',
        '3 grandes chambres, entièrement rénové - Villeray',
        'Villeray-Saint-Michel-Parc-Extension',
        '7635, Rue Saint-Hubert, Montréal',
        '2250', 'n/d', '3', 'n/d', 'Jarry', 'orange', '11',
        'Centris',
        'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/25817021',
        '4',
        "Moderne et entièrement rénové, aire ouverte et abondante lumière naturelle, animaux acceptés sous conditions, non-fumeur, stationnement en location (1-100$/mois), quartier dynamique de Villeray, balcon non mentionné dans l'annonce, disponible dès maintenant",
        '',
    ],
    [
        '2026-08-02', 'NOUVEAU',
        'Grand appartement 6½ (3 chambres), cour arrière privée - Centre-Sud (Marketplace)',
        'Centre-Sud (frontière Hochelaga/Rosemont)',
        '2469, Rue Messier, Montréal',
        '1995', 'n/d', '2', 'oui', 'Frontenac', 'verte', '12',
        'Marketplace',
        'https://www.facebook.com/marketplace/item/2137116496873918',
        '6',
        "Description mentionne 1 chambre fermée + 1 grande chambre double convertible en 2 pièces (le champ structurel Facebook indique 3 chambres) - à valider lors de la visite. Rez-de-chaussée, accès privé à la cour arrière, planchers de bois franc, hauts plafonds, walk-in, à quelques minutes du Plateau-Mont-Royal et de Rosemont. Lien exige une connexion Facebook",
        'https://scontent-yyz1-1.xx.fbcdn.net/v/t39.30808-6/743016729_10174780714605652_6368637080978275674_n.jpg?stp=c194.0.782.782a_dst-jpg_tt6&cstp=mx782x782&ctp=s565x565&_nc_cat=100&ccb=1-7&_nc_sid=454cf4&_nc_ohc=8GCeouhtuXMQ7kNvwFPa1aI&_nc_oc=AdqUBLUw7WDYM5oT-g0o0FLhHtQRi4JRIolKizscRP-SGdi2D1F7wvtXZ-4SkM9a4ao&_nc_zt=23&_nc_ht=scontent-yyz1-1.xx&_nc_gid=dd0NInQSCV1jnFTzbXfEhQ&_nc_ss=7f2a8&oh=00_AQEm7I_yKAD_jZVkj5wHeOKrC8cRKupr62oih1oM6n28hw&oe=6A751945',
    ],
]

body = new_rows + body

# tri : NOUVEAU d'abord, puis score decroissant
def sort_key(r):
    is_new = 0 if r[1] == 'NOUVEAU' else 1
    try:
        score = -int(r[14])
    except Exception:
        score = 0
    return (is_new, score)

body.sort(key=sort_key)

with open(PATH, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(body)

print('OK, total rows:', len(body))
