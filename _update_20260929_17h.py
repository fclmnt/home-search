#!/usr/bin/env python3
import csv

FIELDS = ["date_ajout","statut","titre","quartier","adresse","prix","superficie_pi2",
          "chambres","balcon","station_metro","ligne_metro","minutes_a_pied","site",
          "lien","score","notes","photo"]

with open("annonces.csv", newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rows = list(r)

# 1. Passer les anciennes lignes NOUVEAU a vu
for row in rows:
    if row["statut"] == "NOUVEAU":
        row["statut"] = "vu"

TODAY = "2026-09-29"

new_rows = [
    {
        "date_ajout": TODAY,
        "statut": "NOUVEAU",
        "titre": "Condo 3 chambres fermées + bureau, 1100 pi², 2 balcons - secteur Frontenac",
        "quartier": "Ville-Marie (Centre-Sud)",
        "adresse": "2553, Avenue Gascon, Montréal, QC H2K 2W5",
        "prix": "1970",
        "superficie_pi2": "1100",
        "chambres": "3",
        "balcon": "oui",
        "station_metro": "Frontenac",
        "ligne_metro": "verte",
        "minutes_a_pied": "8",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/condo-3-chambres-1100pc/1743415992",
        "score": "10",
        "notes": "3 chambres fermées + bureau/den, 2 balcons, planchers de bois, grandes fenêtres, animaux acceptés, fumée exterieure seulement, libre 1er oct. 2026, bail 1 an, pas de stationnement inclus. Distance au métro Frontenac estimée a partir de l'adresse (non précisée dans l'annonce).",
        "photo": "",
    },
    {
        "date_ajout": TODAY,
        "statut": "NOUVEAU",
        "titre": "Grand 4 1/2 lumineux, 1100 pi², balcon + rooftop privatif - Centre-Sud",
        "quartier": "Ville-Marie (Centre-Sud)",
        "adresse": "n/d (secteur avenue de Lorimier / rue Ontario, Montréal, QC H2K 3X1)",
        "prix": "2380",
        "superficie_pi2": "1100",
        "chambres": "2",
        "balcon": "oui",
        "station_metro": "Frontenac",
        "ligne_metro": "verte",
        "minutes_a_pied": "12",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-4-1-2-lumineux/1744143048",
        "score": "9",
        "notes": "Balcon + rooftop privatif, laveuse/sécheuse intégrées, lave-vaisselle et réfrigérateur inclus, eau incluse, animaux acceptés, bail 1 an. Adresse exacte non précisée dans l'annonce (seul le code postal est donné) ; station de métro et distance estimées à partir de ce secteur.",
        "photo": "",
    },
    {
        "date_ajout": TODAY,
        "statut": "NOUVEAU",
        "titre": "Grand 6 1/2 Villeray, 1400 pi², 3 chambres, 3 min du métro Crémazie",
        "quartier": "Villeray-Saint-Michel-Parc-Extension",
        "adresse": "8569, Rue Saint-Denis, Montréal, QC H2P 2H4",
        "prix": "2100",
        "superficie_pi2": "1400",
        "chambres": "3",
        "balcon": "oui",
        "station_metro": "Crémazie",
        "ligne_metro": "orange",
        "minutes_a_pied": "3",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-6-1-2-villeray-a-3-min-a-pied-du-metro-cremazie/1743291493",
        "score": "9",
        "notes": "2 salles de bain, rénové, stationnement inclus, animaux limités, libre immédiatement, bail 1 an.",
        "photo": "",
    },
    {
        "date_ajout": TODAY,
        "statut": "NOUVEAU",
        "titre": "Grand 5 1/2, 3 chambres, 1200 pi², balcon avant et arrière - secteur Parc-Jarry",
        "quartier": "Villeray-Saint-Michel-Parc-Extension (secteur Parc-Jarry)",
        "adresse": "n/d (secteur rue Marquette, Parc-Jarry, Montréal, QC H2E 2C8)",
        "prix": "2395",
        "superficie_pi2": "1200",
        "chambres": "3",
        "balcon": "oui",
        "station_metro": "Jarry",
        "ligne_metro": "orange",
        "minutes_a_pied": "10",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-5-3cac-metro-fabre-villeray-rosemont/1743217472",
        "score": "9",
        "notes": "Balcon avant et arrière, climatisation, sécurité/concierge 24h, animaux non admis sauf chats, bail 1 an. L'annonce mentionne un 'métro Fabre' qui n'existe pas : le secteur (rue Marquette, Parc-Jarry) est en réalité à distance de marche de la station Jarry (ligne orange), retenue ici en estimation.",
        "photo": "",
    },
    {
        "date_ajout": TODAY,
        "statut": "NOUVEAU",
        "titre": "Beau 5 1/2 rénové, 1000 pi², cour arrière privée - secteur Préfontaine",
        "quartier": "Rosemont-La Petite-Patrie",
        "adresse": "n/d (secteur 1re Avenue, Montréal, QC H1Y 3A1)",
        "prix": "2140",
        "superficie_pi2": "1000",
        "chambres": "3",
        "balcon": "non",
        "station_metro": "Préfontaine",
        "ligne_metro": "verte",
        "minutes_a_pied": "8",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/beau-5-1-2-renove-avec-cour-arriere-prive-dispo-immediatement/1743787356",
        "score": "7",
        "notes": "3 chambres + den, cour arrière privée et cabanon, plancher chauffant partiel, thermopompe murale, laveuse/sécheuse (branchement), pas d'animaux, libre 1er oct. 2026, bail 1 an. Distance au métro Préfontaine estimée à partir de l'adresse (non précisée dans l'annonce).",
        "photo": "",
    },
    {
        "date_ajout": TODAY,
        "statut": "NOUVEAU",
        "titre": "Grand 4 1/2 rénové près du métro Papineau, 900 pi²",
        "quartier": "Ville-Marie (Village/Centre-Sud)",
        "adresse": "1693, Rue Sainte-Catherine Est, Montréal, QC H2L 2J5",
        "prix": "1975",
        "superficie_pi2": "900",
        "chambres": "2",
        "balcon": "n/d",
        "station_metro": "Papineau",
        "ligne_metro": "verte",
        "minutes_a_pied": "6",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-4-renove-pres-du-metro-papineau/1744140657",
        "score": "6",
        "notes": "Climatisation incluse, eau comprise, électroménagers majeurs et laveuse/sécheuse inclus, bail 1 an, animaux limités, pas de stationnement. Balcon non mentionné dans l'annonce. Distance au métro Papineau estimée à partir de l'adresse (non précisée dans l'annonce).",
        "photo": "",
    },
]

rows.extend(new_rows)

# Tri : NOUVEAU d'abord, puis score decroissant (au sein de chaque groupe de statut)
rows.sort(key=lambda r: (0 if r["statut"] == "NOUVEAU" else 1, -int(r["score"])))

with open("annonces.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    for row in rows:
        w.writerow(row)

print("OK -", len(rows), "lignes,", len(new_rows), "nouvelles annonces ajoutees")
