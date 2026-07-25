import csv

path = 'annonces.csv'
with open(path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
data = rows[1:]

# Flip old NOUVEAU -> vu
for row in data:
    if row[1] == 'NOUVEAU':
        row[1] = 'vu'

today = '2026-07-25'

new_rows = [
    [
        today, 'NOUVEAU',
        "7½ rénové, 2 chambres fermées + bureau, balcon, 1200 pi² - Hochelaga (près Marché Maisonneuve/stade olympique)",
        "Hochelaga-Maisonneuve",
        "n/d (Montréal, QC H1V 2R6)",
        "2200", "1200", "2", "oui",
        "Pie-IX (à vérifier)", "verte", "8 (estimé)",
        "Kijiji",
        "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/tres-beau-7-1-2-a-louer-hochelaga-maisonneuve/1741046490",
        "9",
        "Bureau additionnel, cuisine rénovée 2026, planchers bois franc, brique apparente, balcons refaits 2022, eau incluse, animaux limités, dispo 1er sept 2026",
        ""
    ],
    [
        today, 'NOUVEAU',
        "6½ meublé, 2 chambres, balcon, 1200 pi² - Plateau, près métro Laurier",
        "Le Plateau-Mont-Royal",
        "n/d (Montréal, QC H2T 2H8)",
        "2400", "1200", "2", "oui",
        "Laurier", "verte", "7 (estimé)",
        "Kijiji",
        "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/magnifique-grand-6-entierement-meuble-plateau-mont-royal/1739233013",
        "9",
        "Entièrement meublé, climatisation, 5 puits de lumière, chauffage/électricité/câble/wifi inclus, aucun animal, prix à la limite haute du budget, dispo 1er juillet 2026",
        ""
    ],
    [
        today, 'NOUVEAU',
        "7½ rénové, 3 chambres, terrasse arrière - Village, près métros Beaudry/Papineau",
        "Ville-Marie (Village/Centre-Sud)",
        "n/d (Rue Sainte-Catherine Est, secteur Village, Montréal)",
        "2350", "n/d", "3", "oui (terrasse arrière)",
        "Beaudry ou Papineau", "verte", "5 (estimé)",
        "Marketplace",
        "https://www.facebook.com/marketplace/item/1667192434430051",
        "9",
        "Terrasse arrière, planchers bois franc, boiserie style centenaire, climatisation murale, près pont Jacques-Cartier et nombreux restos/cafés, lien exige une connexion Facebook",
        "https://scontent-yyz1-1.xx.fbcdn.net/v/t39.84726-6/692069772_26712358195041265_6975725434404613474_n.jpg?stp=c0.86.526.526a_dst-jpg_p526x395_tt6&_nc_cat=100&ccb=1-7&_nc_sid=92e707&_nc_ohc=K4QVlYLlbQQQ7kNvwE0KbUC&_nc_oc=Adrk3RVHHBi5OgoT14PLqzSx6d01I7y8L2T47es6h11qi8YHvRoE9bE1E0Q_zayt4sA&_nc_zt=14&_nc_ht=scontent-yyz1-1.xx&_nc_gid=AakSf6B1WC1yfj4w57lVGA&_nc_ss=7f2a8&oh=00_AQCYGPel-1aXi7quArIAJzfowcbz2xzXa35Ilq-Fz-dWhw&oe=6A6A7855"
    ],
    [
        today, 'NOUVEAU',
        "6½ lumineux, 2 chambres (+ 3e possible), balcon privé - Plateau, à 10 min du métro Mont-Royal",
        "Le Plateau-Mont-Royal",
        "n/d (secteur avenue Mont-Royal, Montréal)",
        "2150", "n/d", "2", "oui (grand balcon privé)",
        "Mont-Royal", "verte", "10",
        "Marketplace",
        "https://www.facebook.com/marketplace/item/973452448907992",
        "8",
        "Possibilité de 3e chambre sans fenêtre, à 3 min de l'avenue Mont-Royal et ses commerces, réfrigérateur/cuisinière/lave-vaisselle non inclus, dispo 1er juillet, lien exige une connexion Facebook",
        "https://scontent-yyz1-1.xx.fbcdn.net/v/t39.30808-6/722412619_1617305450011741_6846067607866144954_n.jpg?stp=c0.169.1537.1537a_dst-jpg_tt6&cstp=mx1537x1537&ctp=s565x565&_nc_cat=110&ccb=1-7&_nc_sid=454cf4&_nc_ohc=i88TCt10YGMQ7kNvwEnUsao&_nc_oc=AdrvLp-lCdA5ACif3RiqpRsnZSFYYbio12l9aPpcJgaEV6yKGgapKeozdS-BwYw-o4k&_nc_zt=23&_nc_ht=scontent-yyz1-1.xx&_nc_gid=fvFLeV7qKVviv4IuubP9nA&_nc_ss=7f2a8&oh=00_AQAd5veOG2wwylzp4NkrAahwV01Fgfi6q3HfSwQ0p9yT_w&oe=6A6A6CB2"
    ],
    [
        today, 'NOUVEAU',
        "4½ rénové, 2 chambres fermées, balcon - Plateau (boul. Saint-Laurent)",
        "Le Plateau-Mont-Royal",
        "4655, Boulevard Saint-Laurent, Montréal",
        "2150", "n/d", "2", "oui",
        "Mont-Royal (à vérifier)", "verte", "11 (estimé)",
        "Marketplace",
        "https://www.facebook.com/marketplace/item/1310293694593951",
        "8",
        "Cuisine rénovée avec 5 électroménagers inclus (cuisinière, réfrigérateur, lave-vaisselle, laveuse, sécheuse), proche universités et espaces verts, enquête de crédit et références requises, lien exige une connexion Facebook",
        "https://scontent-yyz1-1.xx.fbcdn.net/v/t39.30808-6/749286191_10234373342255525_9092352675603353029_n.jpg?stp=c106.0.428.428a_dst-jpg_tt6&cstp=mx428x428&ctp=s428x428&_nc_cat=108&ccb=1-7&_nc_sid=454cf4&_nc_ohc=ic73Tw0-fv0Q7kNvwFNI03n&_nc_oc=AdoRe9nP95ciefPsFjp2Cz9dDFg9ClCwxaH95PBTgjuHGcE-LLH8Zj-Pkys_8IC0dFw&_nc_zt=23&_nc_ht=scontent-yyz1-1.xx&_nc_gid=fvFLeV7qKVviv4IuubP9nA&_nc_ss=7f2a8&oh=00_AQAUDDqQ7V8ap6HixCq0L7v792rJEBP5hErOYq_FI48LzQ&oe=6A6A7D85"
    ],
    [
        today, 'NOUVEAU',
        "5½ rénové, 2 chambres + coin bureau, 1000 pi² - Villeray, à 5 min du métro Jarry",
        "Villeray",
        "n/d (Montréal, QC H2R)",
        "1900", "1000", "2", "non (porte-patio vers cour arrière)",
        "Jarry", "orange", "5",
        "Kijiji",
        "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/5-1-2-villeray-2-chambres-a-5-min-a-pied-metro-jarry/1738384606",
        "5",
        "Chambre principale + 2e chambre + coin bureau, thermopompe (chauffage/climatisation), 5 électroménagers inclus, pas d'animaux, bail 1 an, dispo 1er sept 2026",
        ""
    ],
]

data.extend(new_rows)

# Sort: NOUVEAU first, then by score desc
def sort_key(row):
    statut = row[1]
    try:
        score = int(row[14])
    except ValueError:
        score = 0
    return (0 if statut == 'NOUVEAU' else 1, -score)

data.sort(key=sort_key)

with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(header)
    writer.writerows(data)

print("done, total rows:", len(data))
