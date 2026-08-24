import csv

path = 'annonces.csv'
with open(path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
data = rows[1:]

for row in data:
    if row[1] == 'NOUVEAU':
        row[1] = 'vu'

new_rows = [
    ["2026-08-24", "NOUVEAU",
     "Grand 6½ (3 chambres), 1400 pi², cour arrière privée avec patio - Hochelaga-Maisonneuve, à quelques pas du métro Pie-IX",
     "Hochelaga-Maisonneuve", "1629, Avenue William-David, Montréal, QC H1V 2R9",
     "2300", "1400", "3", "non", "Pie-IX", "verte", "8 (estimé)",
     "Kijiji", "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-6-a-louer-hochelaga-maisonneuve-2-500-mois/1742166450",
     "8", "Rez-de-chaussée, grande cour arrière privée avec patio et espace de rangement, salle à manger séparée, animaux limités acceptés, disponible 1er septembre 2026, bail 1 an, immeuble calme et bien entretenu.",
     ""],
    ["2026-08-24", "NOUVEAU",
     "3 chambres, 1000 pi², grand balcon arrière - rue de Brébeuf (Plateau), à 12 min du métro Laurier",
     "Le Plateau-Mont-Royal", "4690, Rue de Brébeuf, Montréal, QC H2J 3L3",
     "2082", "1000", "3", "oui", "Laurier", "orange", "12",
     "Marketplace", "https://www.facebook.com/marketplace/item/1744638296867110",
     "8", "Rue tranquille près de la piste cyclable, 2 chambres doubles + 1 chambre simple séparées par des portes, grand balcon arrière avec 2 espaces de rangement, chats acceptés, locataires tranquilles seulement (références et vérification de crédit requises), disponible 1er oct. 2026, à 15 min à pied du métro Mont-Royal également. Lien Facebook (connexion requise).",
     ""],
    ["2026-08-24", "NOUVEAU",
     "4½ rénové (2 chambres), semi-meublé - Plaza St-Hubert (Rosemont), près du métro Beaubien",
     "Rosemont-La Petite-Patrie", "6617, Rue Saint-Hubert, app. 201, Montréal",
     "2175", "n/d", "2", "n/d", "Beaubien", "orange", "5 (estimé)",
     "Centris", "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/26894928",
     "3", "Entièrement rénové (finitions contemporaines), semi-meublé, climatisation et internet inclus, animaux acceptés sous conditions, disponible 2 jours après acceptation, en plein Plaza St-Hubert, proche marché Jean-Talon et Petite Italie, Walk Score 97. Balcon et superficie non précisés.",
     ""],
    ["2026-08-24", "NOUVEAU",
     "4½ (2 chambres) - secteur résidentiel calme, 23e Avenue (Rosemont)",
     "Rosemont-La Petite-Patrie", "6001, 23e Avenue, app. 3, Montréal",
     "2000", "n/d", "2", "n/d", "Beaubien ou Rosemont (estimé)", "orange", "9 (estimé)",
     "Centris", "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/22497736",
     "3", "Bien aménagé, lumineux, finitions soignées, secteur résidentiel paisible près parcs/commerces/écoles, disponible 5 jours après acceptation, Walk Score 85. Balcon, animaux et chauffage non précisés dans l'annonce.",
     ""],
    ["2026-08-24", "NOUVEAU",
     "4½ (2 chambres) - rue De La Roche (Plateau)",
     "Le Plateau-Mont-Royal", "4417, Rue De La Roche, app. 4, Montréal",
     "2350", "n/d", "2", "n/d", "Mont-Royal (estimé)", "orange", "10 (estimé)",
     "Centris", "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-le-plateau-mont-royal/14734354",
     "3", "Peu de détails dans l'annonce (balcon, superficie, animaux et chauffage non précisés), disponible 24 août 2026, Walk Score 99, secteur à confirmer avant de contacter.",
     ""],
    ["2026-08-24", "NOUVEAU",
     "4½ rénové (2 chambres), 1044 pi², chauffage inclus - avenue Christophe-Colomb (Villeray)",
     "Villeray", "7386, Avenue Christophe-Colomb, Montréal",
     "2400", "1044", "2", "n/d", "Fabre ou De Castelnau (estimé)", "bleue", "10-12 (estimé)",
     "Centris", "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/26203087",
     "5", "Rez-de-chaussée d'un triplex complètement rénové, chauffage inclus, semi-meublé, laveuse-sécheuse et lave-vaisselle inclus, stationnement optionnel (75$/mois) et rangement (50$/mois), disponible 1er juillet 2026, Walk Score 99. Balcon et station de métro exacte non précisés.",
     ""],
]

data.extend(new_rows)


def score_key(row):
    is_new = row[1] == 'NOUVEAU'
    try:
        score = int(row[14])
    except (ValueError, IndexError):
        score = 0
    return (0 if is_new else 1, -score)


data.sort(key=score_key)

with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print("done, total rows:", len(data))
