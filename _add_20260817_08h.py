import csv

fieldnames = ["date_ajout","statut","titre","quartier","adresse","prix","superficie_pi2","chambres","balcon","station_metro","ligne_metro","minutes_a_pied","site","lien","score","notes","photo"]

new_rows = [
    {
        "date_ajout": "2026-08-17", "statut": "NOUVEAU",
        "titre": "5½ meublé (2 chambres), 1200 pi², sans balcon mais grande cour arrière/jardin - rue Saint-Dominique (Petite-Italie/Villeray), à 5 min des métros De Castelnau/Beaubien",
        "quartier": "Villeray (Petite-Italie)",
        "adresse": "6723, Rue Saint-Dominique, Montréal, QC",
        "prix": "2200", "superficie_pi2": "1200", "chambres": "2", "balcon": "non",
        "station_metro": "De Castelnau / Beaubien", "ligne_metro": "bleue/orange", "minutes_a_pied": "5",
        "site": "DuProprio",
        "lien": "https://duproprio.com/fr/location/montreal/villeray-st-michel-parc-extension/5-1-2-a-louer/hab-6723-rue-saint-dominique-1114557",
        "score": "6",
        "notes": "Tout meublé, hydro inclus, grande cour arrière privée + jardin (pas de balcon), bail court terme non renouvelable de 9 mois (fin 30 juin 2027), disponible 1er novembre 2026.",
        "photo": ""
    },
    {
        "date_ajout": "2026-08-17", "statut": "NOUVEAU",
        "titre": "Super grand 5½ lumineux (2 chambres), 1200 pi², balcon avant + terrasse arrière - rue de Lanaudière (Petite-Patrie), à 10 min du métro Beaubien",
        "quartier": "Rosemont-La Petite-Patrie",
        "adresse": "n/d (Rue de Lanaudière, Montréal, QC H2G 1G5)",
        "prix": "2050", "superficie_pi2": "1200", "chambres": "2", "balcon": "oui (balcon avant + terrasse arrière)",
        "station_metro": "Beaubien", "ligne_metro": "orange", "minutes_a_pied": "10",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/super-grand-et-lumineux-logement-petite-patrie/1741918558",
        "score": "8",
        "notes": "Non meublé, animaux interdits, thermopompe, plancher de bois, 3e étage, disponible 1er octobre 2026.",
        "photo": ""
    },
    {
        "date_ajout": "2026-08-17", "statut": "NOUVEAU",
        "titre": "5½ semi-meublé (3 chambres) - rue Saint-Hubert (Rosemont), à 5 min du métro Rosemont",
        "quartier": "Rosemont-La Petite-Patrie",
        "adresse": "5912, Rue Saint-Hubert, Montréal, QC",
        "prix": "2300", "superficie_pi2": "n/d", "chambres": "3", "balcon": "n/d",
        "station_metro": "Rosemont", "ligne_metro": "orange", "minutes_a_pied": "5 (estimé)",
        "site": "Centris",
        "lien": "https://www.centris.ca/en/condos-apartments~for-rent~montreal-rosemont-la-petite-patrie/25204133",
        "score": "4",
        "notes": "Semi-meublé, immeuble de 1989, 1 salle de bain + salle d'eau, animaux non acceptés, disponible 3 jours après acceptation de la promesse de location, Walk Score 97. Superficie non précisée mais 10 pièces au total (spacieux).",
        "photo": ""
    },
    {
        "date_ajout": "2026-08-17", "statut": "NOUVEAU",
        "titre": "5½ (3 chambres) - rue Bélanger (Rosemont/Villeray), à 5 min du métro D'Iberville",
        "quartier": "Rosemont-La Petite-Patrie",
        "adresse": "2468, Rue Bélanger, Montréal, QC",
        "prix": "1995", "superficie_pi2": "n/d", "chambres": "3", "balcon": "n/d",
        "station_metro": "D'Iberville", "ligne_metro": "bleue", "minutes_a_pied": "5 (estimé)",
        "site": "Centris",
        "lien": "https://www.centris.ca/en/condos-apartments~for-rent~montreal-rosemont-la-petite-patrie/12923755",
        "score": "4",
        "notes": "Animaux non acceptés, disponible 10 jours après acceptation de la promesse de location, courtier RE/MAX, Walk Score 96. Superficie non précisée mais 6 pièces/3 chambres (spacieux).",
        "photo": ""
    },
    {
        "date_ajout": "2026-08-17", "statut": "NOUVEAU",
        "titre": "Grand 6½ (jusqu'à 4 chambres), balcon - rue Rivard (Plateau), près du parc Lafontaine, à 5 min du métro Sherbrooke",
        "quartier": "Le Plateau-Mont-Royal",
        "adresse": "4075, Rue Rivard, Montréal, QC H2L 4J1",
        "prix": "2100", "superficie_pi2": "n/d", "chambres": "4", "balcon": "oui",
        "station_metro": "Sherbrooke", "ligne_metro": "orange", "minutes_a_pied": "5",
        "site": "Zumper",
        "lien": "https://www.zumper.com/apartment-buildings/p531166/appartement-6-1-2-a-louer-plateau-mont-royal-2100-mois-1er-juillet-parc-la-fontaine-montreal-qc",
        "score": "6",
        "notes": "Non meublé (meubles disponibles sur demande), animaux non permis, disponible 1er juillet 2026, proche parc Lafontaine, visites sur rendez-vous. Nombre exact de chambres fermées à confirmer (jusqu'à 4 selon l'annonce).",
        "photo": ""
    },
    {
        "date_ajout": "2026-08-17", "statut": "NOUVEAU",
        "titre": "Grand 4½ (2 chambres), 900 pi², terrasse privée au rez-de-jardin - rue Drolet (Plateau), à 6 min du métro Laurier",
        "quartier": "Le Plateau-Mont-Royal",
        "adresse": "n/d (Rue Drolet, Montréal, QC H2T 2H5)",
        "prix": "2200", "superficie_pi2": "900", "chambres": "2", "balcon": "oui (terrasse privée au rez-de-jardin)",
        "station_metro": "Laurier", "ligne_metro": "orange", "minutes_a_pied": "6",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-4-900-pi-plateau-mt-royal-metro-laurier-terrasse/1741538599",
        "score": "7",
        "notes": "Animaux non acceptés, non meublé, foyer au gaz, chauffage+électricité ~110$/mois + gaz ~25$/mois en sus, disponible 1er septembre 2026, laveuse-sécheuse/lave-vaisselle/frigo/cuisinière inclus.",
        "photo": ""
    },
    {
        "date_ajout": "2026-08-17", "statut": "NOUVEAU",
        "titre": "5½ de luxe rénové (3 chambres) - rue Davidson (Hochelaga-Maisonneuve), à 3-4 min du métro Joliette",
        "quartier": "Hochelaga-Maisonneuve",
        "adresse": "2591, Rue Davidson, app. 102, Montréal, QC H1W 2Z3",
        "prix": "2095", "superficie_pi2": "n/d", "chambres": "3", "balcon": "n/d",
        "station_metro": "Joliette", "ligne_metro": "verte", "minutes_a_pied": "3-4",
        "site": "Logis Québec",
        "lien": "https://www.logisquebec.com/appartement-a-louer-mercier_hochelaga-maisonneuve-l357001",
        "score": "5",
        "notes": "Disponible immédiatement, petits animaux acceptés, concierge sur place, électroménagers inclus (laveuse/sécheuse/lave-vaisselle). Une 2e unité identique (302) aussi disponible au même prix.",
        "photo": ""
    },
]

rows = list(csv.DictReader(open('annonces.csv', encoding='utf-8')))
rows.extend(new_rows)

def sort_key(r):
    is_new = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        score = -int(r['score'])
    except (ValueError, TypeError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open('annonces.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)

print("total rows:", len(rows))
print("NOUVEAU:", sum(1 for r in rows if r['statut']=='NOUVEAU'))
