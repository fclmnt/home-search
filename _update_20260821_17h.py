import csv

with open('annonces.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
data = rows[1:]

for row in data:
    if row[1] == 'NOUVEAU':
        row[1] = 'vu'

new_rows = [
    {
        "date_ajout": "2026-08-21",
        "statut": "NOUVEAU",
        "titre": "5½ spacieux (3 chambres), 1300 pi², 2 balcons, à 1-2 min du métro Jarry",
        "quartier": "Villeray",
        "adresse": "8188, Rue Saint-Denis, Montréal, QC",
        "prix": "2155",
        "superficie_pi2": "1300",
        "chambres": "3",
        "balcon": "oui",
        "station_metro": "Jarry",
        "ligne_metro": "orange",
        "minutes_a_pied": "1-2",
        "site": "Centris",
        "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/22417154",
        "score": "9",
        "notes": "2 balcons, stationnement extérieur, lave-vaisselle. Animaux et fumeurs non acceptés. Disponible 1er juillet 2026.",
        "photo": "https://mspublic.centris.ca/media.ashx?id=ADDD250DA4F0DBCDDDDDDDDDDF&t=pi&w=640&h=480&sm=c",
    },
    {
        "date_ajout": "2026-08-21",
        "statut": "NOUVEAU",
        "titre": "4½ rez-de-chaussée rénové (2 chambres), 1103 pi², terrasse et cour privée, à 4 min du métro Beaubien",
        "quartier": "Rosemont / La Petite-Patrie",
        "adresse": "5990, 13e Avenue, Montréal, QC",
        "prix": "2190",
        "superficie_pi2": "1103",
        "chambres": "2",
        "balcon": "oui",
        "station_metro": "Beaubien",
        "ligne_metro": "orange",
        "minutes_a_pied": "4",
        "site": "Centris",
        "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/14587845",
        "score": "8",
        "notes": "Immense terrasse et grande cour à usage exclusif. Semi-meublé, chats acceptés, non-fumeurs. Stationnement disponible 120$/mois. Disponible 15 jours après acceptation de la promesse.",
        "photo": "https://mspublic.centris.ca/media.ashx?id=ADDD250DA46EDE8DDDDDDDDDDD&t=pi&w=640&h=480&sm=c",
    },
    {
        "date_ajout": "2026-08-21",
        "statut": "NOUVEAU",
        "titre": "Cession de bail - 3½ rénové (2 chambres), 900 pi², 2 balcons - rue Saint-Denis, à 5 min des métros Beaubien et Rosemont (Marketplace)",
        "quartier": "Rosemont / La Petite-Patrie",
        "adresse": "Rue Saint-Denis, Montréal, QC H2S 2R8",
        "prix": "2005",
        "superficie_pi2": "900",
        "chambres": "2",
        "balcon": "oui",
        "station_metro": "Beaubien / Rosemont",
        "ligne_metro": "orange",
        "minutes_a_pied": "5",
        "site": "Marketplace",
        "lien": "https://www.facebook.com/marketplace/item/1594430635360278",
        "score": "7",
        "notes": "Cession de bail, rénové 2023, 2 chambres séparées par portes françaises, plafonds 9 pieds, 2 balcons privés (rénovés été 2026), 3e et dernier étage. Électros inclus (cuisinière, réfrigérateur, lave-vaisselle, laveuse-sécheuse, climatisation). Chauffage électrique. Disponible 1er septembre ou 1er octobre 2026, bail existant jusqu'au 30 juin 2027 (renouvelable). Animaux acceptés. Lien Facebook (connexion requise).",
        "photo": "https://scontent-yyz1-1.xx.fbcdn.net/v/t39.30808-6/781924721_10175157656315125_2373393678656261387_n.jpg?stp=c250.0.1500.1500a_dst-jpg_tt6&cstp=mx1500x1500&ctp=s565x565&_nc_cat=109&ccb=1-7&_nc_sid=454cf4&_nc_ohc=smlTrHXjBewQ7kNvwGzuav8&_nc_oc=Adq6D0OVuBNehdV_ceGxPNpGToNi3Apwpx6zAoSi0s06IaSYwQOIiM0J32laMCvzLLM&_nc_zt=23&_nc_ht=scontent-yyz1-1.xx&_nc_gid=l1Sy-42TMfrjsVGJoPoSEw&_nc_ss=7f2a8&oh=00_AQEkqJKuWjMKR1ukvmL7ZT_JTkS0N_tMdgWJqfK0_yG0HA&oe=6A8E78BB",
    },
    {
        "date_ajout": "2026-08-21",
        "statut": "NOUVEAU",
        "titre": "4½ rénové (2 chambres), terrasse et jardin, chauffé - rue Bélanger, à 7 min du métro Fabre",
        "quartier": "Rosemont / La Petite-Patrie",
        "adresse": "1385, Rue Bélanger, Montréal, QC",
        "prix": "1945",
        "superficie_pi2": "n/d",
        "chambres": "2",
        "balcon": "oui",
        "station_metro": "Fabre",
        "ligne_metro": "bleue",
        "minutes_a_pied": "7",
        "site": "Centris",
        "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/27815565",
        "score": "5",
        "notes": "Chauffage et eau chaude inclus. Terrasse et jardin. Construit en 1936. Disponibilité selon les baux. Walk Score 93.",
        "photo": "https://mspublic.centris.ca/media.ashx?id=ADDD250DA132D2FDDDDDDDDDDE&t=pi&w=640&h=480&sm=c",
    },
]

existing_liens = set(row[header.index('lien')] for row in data)
for nr in new_rows:
    assert nr['lien'] not in existing_liens, f"Doublon: {nr['lien']}"
    data.append([nr[col] for col in header])

def sort_key(row):
    statut = row[1]
    try:
        score = int(row[header.index('score')])
    except Exception:
        score = 0
    return (0 if statut == 'NOUVEAU' else 1, -score)

data.sort(key=sort_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print("OK, total rows:", len(data))
print("NOUVEAU count:", sum(1 for r in data if r[1] == 'NOUVEAU'))
