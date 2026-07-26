import csv

NEW_ROWS = [
    {
        "date_ajout": "2026-07-26",
        "statut": "NOUVEAU",
        "titre": "Grand logement de 4 chambres fermées, terrasse ~1100 pi² - rue Ontario Est (Hochelaga-Maisonneuve, entre métro Pie-IX et Joliette)",
        "quartier": "Hochelaga-Maisonneuve",
        "adresse": "3889, rue Ontario Est, Montréal",
        "prix": "1950",
        "superficie_pi2": "n/d",
        "chambres": "4",
        "balcon": "oui",
        "station_metro": "Joliette",
        "ligne_metro": "verte",
        "minutes_a_pied": "8 (estimé)",
        "site": "Marketplace",
        "lien": "https://www.facebook.com/marketplace/item/3191099554424215",
        "score": "7",
        "notes": "4 chambres fermées, situé au 2e étage, aucun locataire en dessous, grande terrasse ~1100 pi² (superficie intérieure non précisée), dispo 1er juillet 2026. Walk Score 98/Transit 72. Lien Facebook (connexion requise).",
        "photo": "https://scontent-yyz1-1.xx.fbcdn.net/v/t39.30808-6/734367592_37516698021250688_9048995181085965231_n.jpg?stp=c0.273.1206.1206a_dst-jpg_tt6&cstp=mx1206x1206&ctp=s565x565&_nc_cat=100&ccb=1-7&_nc_sid=454cf4&_nc_ohc=nR4bexDdA7kQ7kNvwETwXRu&_nc_oc=Adr8b_ZPIzcfgyLtbIjdkZ5tD3NsD-JGZbJKl6RPXDVY72qwup6OtDttajaoVBxtwXs&_nc_zt=23&_nc_ht=scontent-yyz1-1.xx&_nc_gid=DKAPrnNgmI9udtZ3TamYHQ&_nc_ss=7f2a8&oh=00_AQB-a9NpI4qTkrXbihGbIld6aXJDIH_w-iC6HuVrESJzYg&oe=6A6BCFE1",
    },
    {
        "date_ajout": "2026-07-26",
        "statut": "NOUVEAU",
        "titre": "2+1 chambres, 1286 pi², balcon privé - avenue Somerled (NDG, près métro Villa-Maria)",
        "quartier": "Notre-Dame-de-Grâce",
        "adresse": "5622, Avenue Somerled, Montréal",
        "prix": "2225",
        "superficie_pi2": "1286",
        "chambres": "2",
        "balcon": "oui",
        "station_metro": "Villa-Maria",
        "ligne_metro": "orange",
        "minutes_a_pied": "11 (estimé)",
        "site": "Marketplace",
        "lien": "https://www.facebook.com/marketplace/item/1754611555548011",
        "score": "8",
        "notes": "2 chambres + bureau polyvalent à l'étage, planchers de bois franc, cuisine rénovée, laveuse-sécheuse, climatiseur mural, balcon privé, à quelques pas du Village Monkland (commerces/cafés). Hors des quartiers prioritaires (NDG), ligne orange (pas verte). Preuve d'assurance et de revenu exigées, animaux non permis. Lien Facebook (connexion requise).",
        "photo": "https://scontent-yyz1-1.xx.fbcdn.net/v/t39.84726-6/741906764_999333282900431_4323348310788966668_n.jpg?stp=c135.0.540.540a_dst-jpg_p180x540_tt6&_nc_cat=101&ccb=1-7&_nc_sid=92e707&_nc_ohc=e7mVA1XcBRIQ7kNvwFL7uZt&_nc_oc=AdqnFzyRZtxb7ka1eYUWiztJMyEoOnHjXRXo5ojOmyif9_CGvypBkMyBQytmKVgrTEA&_nc_zt=14&_nc_ht=scontent-yyz1-1.xx&_nc_gid=DKAPrnNgmI9udtZ3TamYHQ&_nc_ss=7f2a8&oh=00_AQAGyvXY24_iW0FUCA37EJ_3WuUlTOiALImCM8ETmYcvEw&oe=6A6BCCAC",
    },
    {
        "date_ajout": "2026-07-26",
        "statut": "NOUVEAU",
        "titre": "5½ meublé, 3 chambres, 980 pi², 2 balcons - rue Fabre (Rosemont, près métro Beaubien)",
        "quartier": "Rosemont-La Petite-Patrie",
        "adresse": "6334, Rue Fabre, Montréal",
        "prix": "2200",
        "superficie_pi2": "980",
        "chambres": "3",
        "balcon": "oui",
        "station_metro": "Beaubien",
        "ligne_metro": "orange",
        "minutes_a_pied": "7 (estimé)",
        "site": "DuProprio",
        "lien": "https://duproprio.com/fr/location/montreal/rosemont-la-petite-patrie/5-1-2-a-louer/hab-6334-rue-fabre-796253",
        "score": "8",
        "notes": "Semi-meublé, chauffage et électroménagers inclus, dernier étage, deux petits balcons, animaux acceptés, disponible immédiatement. Distance exacte au métro Beaubien non confirmée par l'annonce (estimée à partir de l'adresse).",
        "photo": "",
    },
    {
        "date_ajout": "2026-07-26",
        "statut": "NOUVEAU",
        "titre": "4½ rénové, 950 pi², balcon avant + terrasse arrière privée - rue St-Joseph Est (Plateau, près parc Laurier)",
        "quartier": "Le Plateau-Mont-Royal",
        "adresse": "1570, rue St-Joseph Est, Montréal",
        "prix": "2000",
        "superficie_pi2": "950",
        "chambres": "2",
        "balcon": "oui",
        "station_metro": "Laurier",
        "ligne_metro": "orange",
        "minutes_a_pied": "12 (estimé, incertain)",
        "site": "DuProprio",
        "lien": "https://duproprio.com/fr/location/montreal/le-plateau-mont-royal/4-1-2-a-louer/hab-1570-stjoseph-est-1119590",
        "score": "7",
        "notes": "Planchers de bois franc, comptoirs de granit, cuisine à îlot, disponible maintenant. Distance réelle au métro Laurier non confirmée par l'annonce, possiblement proche de la limite de 12 min - à vérifier avant de contacter.",
        "photo": "",
    },
    {
        "date_ajout": "2026-07-26",
        "statut": "NOUVEAU",
        "titre": "Appartement rénové (semi sous-sol), 3 chambres - avenue De Gaspé (Villeray/Petite Italie, près métro De Castelnau)",
        "quartier": "Villeray",
        "adresse": "6695, Avenue De Gaspé, app. 1, Montréal",
        "prix": "1900",
        "superficie_pi2": "n/d",
        "chambres": "3",
        "balcon": "n/d",
        "station_metro": "De Castelnau",
        "ligne_metro": "bleue",
        "minutes_a_pied": "9 (estimé, incertain)",
        "site": "Centris",
        "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/15505756",
        "score": "4",
        "notes": "Unité en semi sous-sol (moins de lumière naturelle), coin Saint-Zotique/De Gaspé, cuisine équipée, laveuse-sécheuse incluses, non-fumeurs, disponible immédiatement ou 5 jours après acceptation. Walk Score 99. Superficie et balcon non précisés, distance métro estimée non confirmée.",
        "photo": "",
    },
]

with open("/Users/fclement/home-search/annonces.csv", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
existing_links = {r[header.index("lien")] for r in rows[1:]}

added = 0
for nr in NEW_ROWS:
    if nr["lien"] in existing_links:
        print("SKIP (already present):", nr["lien"])
        continue
    rows.append([nr[h] for h in header])
    added += 1

with open("/Users/fclement/home-search/annonces.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerows(rows)

print(f"Added {added} new rows.")
