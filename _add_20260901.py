import csv

PATH = "annonces.csv"
TODAY = "2026-09-01"

FIELDS = ["date_ajout","statut","titre","quartier","adresse","prix","superficie_pi2",
          "chambres","balcon","station_metro","ligne_metro","minutes_a_pied","site",
          "lien","score","notes","photo"]

new_rows = [
    {
        "date_ajout": TODAY, "statut": "NOUVEAU",
        "titre": "8½, 5 chambres, à 3 min du métro Sherbrooke (Marketplace)",
        "quartier": "Le Plateau-Mont-Royal",
        "adresse": "n/d (secteur Saint-Denis / Sherbrooke, Montréal)",
        "prix": "2295", "superficie_pi2": "n/d", "chambres": "5", "balcon": "n/d",
        "station_metro": "Sherbrooke", "ligne_metro": "orange", "minutes_a_pied": "3",
        "site": "Marketplace",
        "lien": "https://www.facebook.com/marketplace/item/1295097232428646",
        "score": "4",
        "notes": "Disponible dès maintenant. Cuisine, salon, salle de bain, laveuse/sécheuse et poêle/frigo inclus. Walk Score 100. Superficie non précisée. Lien Facebook (connexion requise).",
        "photo": "",
    },
    {
        "date_ajout": TODAY, "statut": "NOUVEAU",
        "titre": "4½ rénové, 2 chambres, balcon privé, près du parc Lafontaine (Marketplace)",
        "quartier": "Ville-Marie (Village, bordure Plateau-Mont-Royal)",
        "adresse": "n/d (Montréal, QC)",
        "prix": "1945", "superficie_pi2": "n/d", "chambres": "2", "balcon": "oui",
        "station_metro": "n/d", "ligne_metro": "n/d", "minutes_a_pied": "n/d",
        "site": "Marketplace",
        "lien": "https://www.facebook.com/marketplace/item/1500903075380300",
        "score": "4",
        "notes": "Disponible maintenant. Électros inclus (frigo, four, lave-vaisselle), laveuse/sécheuse dans la salle de bain, balcon privé. À distance de marche du parc Lafontaine, rue Sainte-Catherine, Village, Plateau et Vieux-Port ; proche de 3 stations de métro (non nommées) et du REM. Stationnement extérieur optionnel 155$/mois. Lien Facebook (connexion requise).",
        "photo": "",
    },
    {
        "date_ajout": TODAY, "statut": "NOUVEAU",
        "titre": "5½ au Plateau-Mont-Royal (Marketplace)",
        "quartier": "Le Plateau-Mont-Royal",
        "adresse": "n/d (Montréal, QC)",
        "prix": "1975", "superficie_pi2": "n/d", "chambres": "2", "balcon": "n/d",
        "station_metro": "n/d", "ligne_metro": "n/d", "minutes_a_pied": "n/d",
        "site": "Marketplace",
        "lien": "https://www.facebook.com/marketplace/item/2124372061520309",
        "score": "2",
        "notes": "Annonce titre seulement, description non disponible via le scraper. Nombre de chambres estimé à 2 selon la nomenclature standard d'un 5½. Lien Facebook (connexion requise) pour plus de détails.",
        "photo": "",
    },
    {
        "date_ajout": TODAY, "statut": "NOUVEAU",
        "titre": "6 pièces (3 chambres), 1208 pi² — 9e Avenue (Rosemont), près Promenades Masson, à distance du métro Beaubien",
        "quartier": "Rosemont-La Petite-Patrie",
        "adresse": "5172, 9e Avenue, Montréal",
        "prix": "1950", "superficie_pi2": "1208", "chambres": "3", "balcon": "n/d",
        "station_metro": "Beaubien", "ligne_metro": "orange", "minutes_a_pied": "10-13 (estimé, à vérifier)",
        "site": "Centris",
        "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/23528752",
        "score": "7",
        "notes": "Proche des Promenades Masson, Walk Score 97, disponible 1er septembre 2026. Distance au métro Beaubien estimée entre 10 et 13 minutes à pied selon la source — à confirmer sur place.",
        "photo": "",
    },
    {
        "date_ajout": TODAY, "statut": "NOUVEAU",
        "titre": "6 pièces (2 chambres dont sous-sol), 941 pi² — rue Saint-Zotique Ouest, à 8 min du métro Jean-Talon",
        "quartier": "Rosemont-La Petite-Patrie",
        "adresse": "251, Rue Saint-Zotique Ouest, Montréal",
        "prix": "2300", "superficie_pi2": "941", "chambres": "2", "balcon": "n/d",
        "station_metro": "Jean-Talon", "ligne_metro": "orange", "minutes_a_pied": "8",
        "site": "Centris",
        "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/16217167",
        "score": "5",
        "notes": "Animaux acceptés sous conditions, climatisation murale, disponible 5 jours après promesse de location. Une des 2 chambres est au sous-sol.",
        "photo": "",
    },
    {
        "date_ajout": TODAY, "statut": "NOUVEAU",
        "titre": "5½ (3 chambres), ~1076 pi² — boulevard Saint-Joseph Est (Plateau), à 10 min du métro Laurier",
        "quartier": "Le Plateau-Mont-Royal",
        "adresse": "1260A, Boulevard Saint-Joseph Est, Montréal",
        "prix": "1950", "superficie_pi2": "1076", "chambres": "3", "balcon": "n/d",
        "station_metro": "Laurier", "ligne_metro": "orange", "minutes_a_pied": "10",
        "site": "Centris",
        "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-le-plateau-mont-royal/12989624",
        "score": "6",
        "notes": "Environ 100 m² (~1076 pi²), électroménagers inclus, animaux acceptés, disponible 1er septembre 2026, Walk Score 99.",
        "photo": "",
    },
    {
        "date_ajout": TODAY, "statut": "NOUVEAU",
        "titre": "3 chambres dans un 6½, meublé, 1000 pi² — rue Saint-Denis, à deux pas du métro Laurier",
        "quartier": "Le Plateau-Mont-Royal",
        "adresse": "5061, Rue Saint-Denis, Montréal",
        "prix": "2000", "superficie_pi2": "1000", "chambres": "3", "balcon": "oui",
        "station_metro": "Laurier", "ligne_metro": "orange", "minutes_a_pied": "3 (estimé)",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/3-chambres-dans-6-1-2-metro-laurier/1742718585",
        "score": "8",
        "notes": "Meublé, eau incluse, chauffage électrique non inclus, laveuse/sécheuse dans l'immeuble, animaux limités, disponible 28 août 2026, bail 1 an.",
        "photo": "",
    },
    {
        "date_ajout": TODAY, "statut": "NOUVEAU",
        "titre": "Grand 4½ (900 pi²), terrasse privée — rue Drolet (Plateau-Mont-Royal), à 6 min du métro Laurier",
        "quartier": "Le Plateau-Mont-Royal",
        "adresse": "Rue Drolet, Montréal, QC H2T 2H5",
        "prix": "2150", "superficie_pi2": "900", "chambres": "2", "balcon": "oui",
        "station_metro": "Laurier", "ligne_metro": "orange", "minutes_a_pied": "6",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-4-900-pi-plateau-mt-royal-metro-laurier-terrasse/1742151006",
        "score": "7",
        "notes": "Condo rez-de-chaussée rénové, foyer au gaz, laveuse/sécheuse, lave-vaisselle, climatiseur portatif, chauffage/électricité à la charge du locataire (~110$/mois Hydro + ~25$/mois Énergir), animaux non acceptés, disponible 17 août 2026, bail 1 an.",
        "photo": "",
    },
]

with open(PATH, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

existing_links = set(r["lien"] for r in rows)
for r in new_rows:
    if r["lien"] in existing_links:
        raise SystemExit(f"DUPLICATE lien already present: {r['lien']}")

for r in rows:
    if r["statut"] == "NOUVEAU":
        r["statut"] = "vu"

rows = new_rows + rows

def sort_key(r):
    is_new = 0 if r["statut"] == "NOUVEAU" else 1
    try:
        score = -float(r["score"])
    except (ValueError, TypeError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open(PATH, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    for r in rows:
        w.writerow(r)

print("Added", len(new_rows), "rows. Total rows now:", len(rows))
