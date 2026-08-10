import csv

CSV_PATH = "annonces.csv"

with open(CSV_PATH, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)

for r in rows:
    if r["statut"] == "NOUVEAU":
        r["statut"] = "vu"

new_rows = [
    {
        "date_ajout": "2026-08-10",
        "statut": "NOUVEAU",
        "titre": "5½ (3 chambres, 975 pi²) semi-meublé rénové - rue Rachel Est, à 6 min du métro Frontenac (Marketplace)",
        "quartier": "Le Plateau-Mont-Royal",
        "adresse": "2473, Rue Rachel Est, Montréal, QC H2H 1R9",
        "prix": "2195",
        "superficie_pi2": "975",
        "chambres": "3",
        "balcon": "n/d",
        "station_metro": "Frontenac",
        "ligne_metro": "verte",
        "minutes_a_pied": "6 (estimé)",
        "site": "Marketplace",
        "lien": "https://www.facebook.com/marketplace/item/28384964421192516",
        "score": "7",
        "notes": "Entièrement rénové, semi-meublé (électros inclus, meubles optionnels), wifi inclus, thermopompe (chauffage/climatisation), stationnement possible, à quelques pas du parc Baldwin, disponible janvier 2027 (rabais 100$/mois). Balcon non précisé. Lien Facebook (connexion requise).",
        "photo": "https://scontent-ord5-2.xx.fbcdn.net/v/t39.84726-6/729747145_1529652128704746_2446908512688911381_n.jpg?stp=c135.0.540.540a_dst-jpg_p180x540_tt6&_nc_cat=100&ccb=1-7&_nc_sid=92e707&_nc_ohc=LA6jZZEZ45oQ7kNvwGRnS2t&_nc_oc=AdrZCuORhD3hALxRgmd10RoTq9JuIZXSg4214VZdOTXsMiakR8xw5tTQbhhgra0l8kY&_nc_zt=14&_nc_ht=scontent-ord5-2.xx&_nc_gid=U_RbhiGiDK3yu5vaRrkfHQ&_nc_ss=7f2a8&oh=00_AQHfBalX_kK8XzlY20u-FNZWV6MBFMNC2Lw_LG6TZMElxQ&oe=6A7FFF35",
    },
    {
        "date_ajout": "2026-08-10",
        "statut": "NOUVEAU",
        "titre": "Grand 6½ (3 chambres) sur 2 étages avec balcon - rue Joliette, à 1 min du métro Joliette (Marketplace)",
        "quartier": "Hochelaga-Maisonneuve",
        "adresse": "2160, Rue Joliette, app. 2160, Montréal, QC H1W 3G6",
        "prix": "2100",
        "superficie_pi2": "n/d",
        "chambres": "3",
        "balcon": "oui",
        "station_metro": "Joliette",
        "ligne_metro": "verte",
        "minutes_a_pied": "1",
        "site": "Marketplace",
        "lien": "https://www.facebook.com/marketplace/item/27448354598105803",
        "score": "7",
        "notes": "Logement sur 2 niveaux (2e et 3e étage), belle séparation des espaces, cuisinière et frigo inclus, laveuse-sécheuse, chats acceptés, non-fumeur, disponible 1er juillet 2026. Superficie non précisée. Lien Facebook (connexion requise).",
        "photo": "https://scontent-ord5-1.xx.fbcdn.net/v/t39.84726-6/706781388_2020210695546568_6789588270194734204_n.jpg?stp=c135.0.540.540a_dst-jpg_p180x540_tt6&_nc_cat=109&ccb=1-7&_nc_sid=92e707&_nc_ohc=7ZaeWa83n9gQ7kNvwErJKHr&_nc_oc=AdqbRAE3vD-VxtsbWYHfC1EasYImUqf4qjOfiZ5xzMSizKYWZQB0dLKm9V8hbEm00EU&_nc_zt=14&_nc_ht=scontent-ord5-1.xx&_nc_gid=hcfDg9CFnn2YrDyR7gvmZg&_nc_ss=7f2a8&oh=00_AQFDb0E3oqQXPs7J5-w19gSbrxjOK-TdHCbGe3cJWADFxw&oe=6A8014A6",
    },
    {
        "date_ajout": "2026-08-10",
        "statut": "NOUVEAU",
        "titre": "Terrasse privée sur le toit, 2 chambres + mezzanine (911 pi²) - rue Nicolet, à 12 min du métro Joliette",
        "quartier": "Hochelaga-Maisonneuve",
        "adresse": "578, Rue Nicolet, app. 401, Montréal, QC",
        "prix": "2400",
        "superficie_pi2": "911",
        "chambres": "2",
        "balcon": "oui",
        "station_metro": "Joliette",
        "ligne_metro": "verte",
        "minutes_a_pied": "12 (estimé)",
        "site": "Centris",
        "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/24329498",
        "score": "8",
        "notes": "Construction neuve (2023), meublé, mezzanine polyvalente (bureau ou 3e chambre, non fermée) menant à la terrasse privée sur le toit, 1 stationnement + 1 rangement inclus, proche Marché Maisonneuve, non-fumeur, disponible 15 mars 2026.",
        "photo": "",
    },
    {
        "date_ajout": "2026-08-10",
        "statut": "NOUVEAU",
        "titre": "3 chambres avec balcon privé (1060 pi²) sur 2 niveaux - rue De La Roche, à 7-8 min du métro Mont-Royal",
        "quartier": "Le Plateau-Mont-Royal",
        "adresse": "4406, Rue De La Roche, Montréal, QC H2J 3J1",
        "prix": "2400",
        "superficie_pi2": "1060",
        "chambres": "2",
        "balcon": "oui",
        "station_metro": "Mont-Royal",
        "ligne_metro": "orange",
        "minutes_a_pied": "7-8",
        "site": "Centris",
        "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-le-plateau-mont-royal/12242524",
        "score": "7",
        "notes": "Unité sur 2 étages (salon au rez-de-chaussée, chambres au sous-sol), balcon privé côté soleil, semi-meublé, stationnement arrière, chats acceptés, Walk Score 99, disponible 17 août 2026.",
        "photo": "",
    },
    {
        "date_ajout": "2026-08-10",
        "statut": "NOUVEAU",
        "titre": "2 chambres rénové avec jardinet avant (1000 pi²) - avenue de l'Esplanade (Mile End), à 12 min du métro Rosemont",
        "quartier": "Le Plateau-Mont-Royal",
        "adresse": "5873, Avenue de l'Esplanade, Montréal, QC H2V 3A2",
        "prix": "2050",
        "superficie_pi2": "1000",
        "chambres": "2",
        "balcon": "n/d",
        "station_metro": "Rosemont",
        "ligne_metro": "orange",
        "minutes_a_pied": "12 (estimé)",
        "site": "Centris",
        "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-le-plateau-mont-royal/18715596",
        "score": "5",
        "notes": "Rez-de-chaussée, planchers de bois franc, cuisine et salle de bain récemment rénovées, jardinet avant (pas de balcon confirmé), secteur Mile End, Walk Score 98, disponible 1er septembre 2026.",
        "photo": "",
    },
    {
        "date_ajout": "2026-08-10",
        "statut": "NOUVEAU",
        "titre": "Très grand 6½ (3 chambres, 1250 pi²) avec 2 balcons - Villeray, à 3 min du métro Jarry",
        "quartier": "Villeray",
        "adresse": "Secteur métro Jarry, Montréal, QC H2R 2E8",
        "prix": "2400",
        "superficie_pi2": "1250",
        "chambres": "3",
        "balcon": "oui",
        "station_metro": "Jarry",
        "ligne_metro": "orange",
        "minutes_a_pied": "3",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/tres-grand-6-1-2-villeray-metro-jarry/1741589226",
        "score": "9",
        "notes": "Étage intermédiaire d'un triplex, 2 balcons (avant et grand balcon arrière), îlot de cuisine, laveuse-sécheuse dans l'unité, petit chien ou chat accepté sous conditions, disponible 1er août 2026. Adresse exacte non précisée dans l'annonce.",
        "photo": "",
    },
    {
        "date_ajout": "2026-08-10",
        "statut": "NOUVEAU",
        "titre": "3 chambres, 2 salles de bain - avenue Bourbonnière, à 7 min du métro Pie-IX",
        "quartier": "Hochelaga-Maisonneuve",
        "adresse": "1419, Avenue Bourbonnière, Montréal, QC",
        "prix": "2108",
        "superficie_pi2": "n/d",
        "chambres": "3",
        "balcon": "n/d",
        "station_metro": "Pie-IX",
        "ligne_metro": "verte",
        "minutes_a_pied": "7",
        "site": "Centris",
        "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/24971226",
        "score": "5",
        "notes": "Prix promotionnel 2108$/mois pour bail 12 mois (régulier 2300$/mois), semi-meublé, entièrement rénové, électroménagers haut de gamme, proche Super C et Marché Métro, Walk Score 94, disponible 3 jours après acceptation.",
        "photo": "",
    },
]

fields_out = fields if "photo" in fields else fields + ["photo"]
rows_out = rows + new_rows

def sort_key(r):
    is_new = 0 if r["statut"] == "NOUVEAU" else 1
    try:
        score = -int(r["score"])
    except (ValueError, TypeError):
        score = 0
    return (is_new, score)

rows_out.sort(key=sort_key)

with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields_out)
    w.writeheader()
    w.writerows(rows_out)

print(f"{len(new_rows)} nouvelles annonces ajoutées. Total: {len(rows_out)} lignes.")
