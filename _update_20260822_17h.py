import csv

PATH = "annonces.csv"

with open(PATH, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'

new_rows = [
{
    "date_ajout": "2026-08-22",
    "statut": "NOUVEAU",
    "titre": "5½ semi-meublé (3 chambres), immeuble Cogir - rue Jarry Est (Villeray), à quelques pas du métro Jarry",
    "quartier": "Villeray",
    "adresse": "2660, Rue Jarry Est, Montréal, QC",
    "prix": "2305",
    "superficie_pi2": "n/d",
    "chambres": "3",
    "balcon": "n/d",
    "station_metro": "Jarry",
    "ligne_metro": "orange",
    "minutes_a_pied": "8 (estimé)",
    "site": "DuProprio",
    "lien": "https://duproprio.com/fr/location/montreal/villeray-st-michel-parc-extension/5-1-2-a-louer/hab-2660-rue-jarry-e-1129566",
    "score": "4",
    "notes": "Immeuble Cogir (69 unités), semi-meublé, 5 électroménagers inclus, chauffage/eau chaude/internet inclus, climatisation murale, stationnement intérieur en option, promotion 1 mois gratuit sous conditions, superficie non précisée.",
    "photo": "",
},
{
    "date_ajout": "2026-08-22",
    "statut": "NOUVEAU",
    "titre": "6½ lumineux (3 chambres fermées), 1000 pi², grand balcon - avenue Louis-Hébert (Rosemont), à ~9 min des métros Rosemont/Beaubien",
    "quartier": "Rosemont-La Petite-Patrie",
    "adresse": "5838, Avenue Louis-Hébert, Montréal, QC H2G 2G2",
    "prix": "2100",
    "superficie_pi2": "1000",
    "chambres": "3",
    "balcon": "oui",
    "station_metro": "Rosemont",
    "ligne_metro": "orange",
    "minutes_a_pied": "9 (estimé)",
    "site": "Kijiji",
    "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/6-lumineux-3-ch-fermees-renove-equipe-rosemont/1740407731",
    "score": "8",
    "notes": "Sous-location 1 an (jusqu'au 31 juillet 2027), laveuse-sécheuse et four neufs, frigo XL, 2 thermopompes neuves (chauffage/clim), lave-vaisselle, internet/câble et eau inclus, animaux limités, disponible 11 juillet 2026.",
    "photo": "https://media.kijiji.ca/api/v1/ca-prod-fsbo-ads/images/55/5508505f-2676-403c-a0ef-0ff508313938?rule=kijijica-640-webp",
},
{
    "date_ajout": "2026-08-22",
    "statut": "NOUVEAU",
    "titre": "Grand 5½ ensoleillé (3 chambres), balcon - coin Saint-André/Bellechasse (Petite-Patrie), à 6 min du métro Beaubien",
    "quartier": "Rosemont-La Petite-Patrie",
    "adresse": "n/d (coin Saint-André et Bellechasse, Montréal, QC H2S 2K4)",
    "prix": "2200",
    "superficie_pi2": "n/d",
    "chambres": "3",
    "balcon": "oui",
    "station_metro": "Beaubien",
    "ligne_metro": "orange",
    "minutes_a_pied": "6",
    "site": "Kijiji",
    "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-appartement-5-ensoleille-rosemont-petite-patrie/1742222174",
    "score": "6",
    "notes": "Balcon accessible depuis une chambre, four/cuisinière/lave-vaisselle/frigo/laveuse-sécheuse inclus, électricité et wifi non inclus (~100$/50$ estimés), animaux acceptés, disponible 1er oct. 2026 (dates négociables), aussi à 8 min du métro Rosemont.",
    "photo": "https://media.kijiji.ca/api/v1/ca-prod-fsbo-ads/images/c9/c94ec64e-8bbe-4c89-a24b-db48bcd3657c?rule=kijijica-640-webp",
},
{
    "date_ajout": "2026-08-22",
    "statut": "NOUVEAU",
    "titre": "5½ rénové (2 chambres), 900 pi², grand balcon arrière + toit - rue d'Iberville (Villeray), à 11 min du métro Jarry",
    "quartier": "Villeray",
    "adresse": "7186, Rue d'Iberville, Montréal, QC",
    "prix": "1950",
    "superficie_pi2": "900",
    "chambres": "2",
    "balcon": "oui",
    "station_metro": "Jarry",
    "ligne_metro": "orange",
    "minutes_a_pied": "11",
    "site": "DuProprio",
    "lien": "https://duproprio.com/fr/location/montreal/villeray-st-michel-parc-extension/5-1-2-a-louer/hab-7186-rue-diberville-1078665",
    "score": "7",
    "notes": "2e étage d'un duplex, cuisine et salle de bain rénovées (printemps 2024), climatisation centrale, branchement laveuse-sécheuse, lave-vaisselle, ruelle verte, non-fumeur, aucun animal, disponible immédiatement, Walk Score 94.",
    "photo": "",
},
{
    "date_ajout": "2026-08-22",
    "statut": "NOUVEAU",
    "titre": "5½ rénové (2 chambres), 1160 pi², 2 terrasses, stationnement inclus - rue Bossuet (Hochelaga), à ~10-12 min des métros Préfontaine/Joliette",
    "quartier": "Hochelaga-Maisonneuve",
    "adresse": "2502, Rue Bossuet, app. 305, Montréal, QC",
    "prix": "1990",
    "superficie_pi2": "1160",
    "chambres": "2",
    "balcon": "oui (2 terrasses)",
    "station_metro": "Préfontaine ou Joliette (à confirmer)",
    "ligne_metro": "verte",
    "minutes_a_pied": "10-12 (estimé)",
    "site": "Centris",
    "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/22273952",
    "score": "9",
    "notes": "Dernier étage (construction 2004), meublé et équipé, 1 place de stationnement garage incluse, animaux non acceptés, non-fumeur, Walk Score 84, disponible 5 jours après acceptation du bail, jusqu'en mai 2027.",
    "photo": "https://mspublic.centris.ca/media.ashx?id=ADDD250DA1D8268DDDDDDDDDDF&t=pi&w=640&h=480&sm=c",
},
{
    "date_ajout": "2026-08-22",
    "statut": "NOUVEAU",
    "titre": "5½ tout meublé (2 grandes chambres), 1200 pi² - rue Saint-Dominique (Villeray/Petite Italie), à 5 min des métros Castelnau/Beaubien — bail 9 mois non renouvelable",
    "quartier": "Villeray",
    "adresse": "6723, Rue Saint-Dominique, Montréal, QC",
    "prix": "2200",
    "superficie_pi2": "1200",
    "chambres": "2",
    "balcon": "n/d",
    "station_metro": "Castelnau ou Beaubien",
    "ligne_metro": "orange",
    "minutes_a_pied": "5",
    "site": "DuProprio",
    "lien": "https://duproprio.com/fr/location/montreal/villeray-st-michel-parc-extension/5-1-2-a-louer/hab-6723-rue-saint-dominique-1114557",
    "score": "6",
    "notes": "ATTENTION: bail de 9 mois non renouvelable (1er oct. 2026 au 30 juin 2027), tout meublé, électricité incluse, grande cour arrière privée avec jardin, sous-sol avec laveuse-sécheuse et rangement, rez-de-chaussée d'un triplex dans la Petite Italie.",
    "photo": "",
},
{
    "date_ajout": "2026-08-22",
    "statut": "NOUVEAU",
    "titre": "Appartement 5½ (Hochelaga) - infos limitées, à vérifier via Facebook Marketplace",
    "quartier": "Hochelaga-Maisonneuve",
    "adresse": "n/d (Montréal, QC)",
    "prix": "1995",
    "superficie_pi2": "n/d",
    "chambres": "3",
    "balcon": "n/d",
    "station_metro": "n/d (secteur Hochelaga)",
    "ligne_metro": "verte",
    "minutes_a_pied": "n/d",
    "site": "Marketplace",
    "lien": "https://www.facebook.com/marketplace/item/1020807880801669",
    "score": "3",
    "notes": "Fiche Marketplace très peu détaillée (titre et prix seulement, pas de description ni superficie). Chambres estimées à 3 d'après le type 5½. Le lien exige une connexion Facebook pour voir les détails complets.",
    "photo": "https://scontent-yyz1-1.xx.fbcdn.net/v/t39.84726-6/740733947_28734879242768603_2405899251014488449_n.jpg?stp=c0.87.526.526a_dst-jpg_p526x395_tt6&_nc_cat=105&ccb=1-7&_nc_sid=92e707&_nc_ohc=Q9ViAyeDpUAQ7kNvwFF85BL&_nc_oc=Adr4Bry90yP1945bAQ7iQ52U9LuxXUfcltCcAJNNZMjNUaTJQ7tsFLsd_jtuJfl42Ps&_nc_zt=14&_nc_ht=scontent-yyz1-1.xx&_nc_gid=rTvNKBKykO1Kn418ORNEfA&_nc_ss=7f2a8&oh=00_AQHwScRvAsPs8uZWD-UEV1uK_8325MQziNdaYa1h63-U7A&oe=6A8FDC27",
},
]

rows.extend(new_rows)

def sort_key(r):
    is_new = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        score = -int(r['score'])
    except (ValueError, KeyError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open(PATH, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    writer.writerows(rows)

print("Total rows:", len(rows))
print("New rows added:", len(new_rows))
