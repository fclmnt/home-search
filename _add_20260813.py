#!/usr/bin/env python3
import csv

CSV_PATH = "annonces.csv"
TODAY = "2026-08-13"

new_rows = [
    {
        "date_ajout": TODAY,
        "statut": "NOUVEAU",
        "titre": "4½ (2 chambres), 900 pi², 2 balcons - rue Saint-Hubert (Plateau-Mont-Royal), à 5 min du métro Laurier",
        "quartier": "Le Plateau-Mont-Royal",
        "adresse": "Rue Saint-Hubert, Montréal, QC H2J 2Y2",
        "prix": "1935",
        "superficie_pi2": "900",
        "chambres": "2",
        "balcon": "oui",
        "station_metro": "Laurier",
        "ligne_metro": "verte",
        "minutes_a_pied": "5",
        "site": "kijiji.ca",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/4-1-2-apartment/1739925295",
        "score": "8",
        "notes": "Salon et cuisine séparés, 2 balcons (avant et arrière), chats acceptés, cession de bail possible, disponible 1er septembre 2026 (flexible)",
        "photo": "",
    },
    {
        "date_ajout": TODAY,
        "statut": "NOUVEAU",
        "titre": "5½ meublé (3 chambres), 2 balcons - 13e Avenue (Villeray/Saint-Michel), à 2 min du métro Saint-Michel",
        "quartier": "Villeray",
        "adresse": "13e Avenue, Montréal (adresse exacte non affichée)",
        "prix": "2250",
        "superficie_pi2": "n/d",
        "chambres": "3",
        "balcon": "oui",
        "station_metro": "Saint-Michel",
        "ligne_metro": "bleue",
        "minutes_a_pied": "2",
        "site": "logisquebec.com",
        "lien": "https://www.logisquebec.com/appartement-a-louer-villeray_saint-michel_parc-extension-l357396",
        "score": "6",
        "notes": "Meublé, bail jusqu'au 30 juin 2027, animaux non acceptés, superficie non indiquée",
        "photo": "",
    },
    {
        "date_ajout": TODAY,
        "statut": "NOUVEAU",
        "titre": "4½ (2 chambres), 904 pi², grand balcon 151 pi² - chemin de la Côte-Sainte-Catherine (Outremont), à 11 min du métro Édouard-Montpetit",
        "quartier": "Outremont",
        "adresse": "55, Chemin de la Côte-Sainte-Catherine, Montréal, QC H2V 2A5",
        "prix": "2055",
        "superficie_pi2": "904",
        "chambres": "2",
        "balcon": "oui",
        "station_metro": "Édouard-Montpetit",
        "ligne_metro": "bleue",
        "minutes_a_pied": "11",
        "site": "Marketplace",
        "lien": "https://www.facebook.com/marketplace/item/1026611543438786",
        "score": "7",
        "notes": "Hors des 4 quartiers prioritaires (secteur Outremont, près du parc Jeanne-Mance); 11e étage, piscine et sauna, disponible 31 août 2026; lien Facebook (connexion requise)",
        "photo": "https://scontent-yyz1-1.xx.fbcdn.net/v/t39.84726-6/763028717_27778713158453060_4923090953497169148_n.jpg?stp=c0.87.526.526a_dst-jpg_p526x395_tt6&_nc_cat=105&ccb=1-7&_nc_sid=92e707&_nc_ohc=z0pKkaHg84YQ7kNvwFCceqW&_nc_oc=AdpeHA8VPvRCR6fziDXUGtwMZ8_I_boPNhjs1mrLk5oJJaTF5isgwjGWNcUMINs1on0&_nc_zt=14&_nc_ht=scontent-yyz1-1.xx&_nc_gid=QUWVCKgQSZEZTuxprRp-TA&_nc_ss=7f2a8&oh=00_AQHsXcZQXfk8XVMHlEBzdbAuaZU41Ct_0WaCDW8d_EtZfw&oe=6A839BE8",
    },
    {
        "date_ajout": TODAY,
        "statut": "NOUVEAU",
        "titre": "4½ (2 chambres) - rue de Castelnau Ouest (Villeray), à 2 min du métro De Castelnau",
        "quartier": "Villeray",
        "adresse": "75, Rue de Castelnau Ouest, Montréal",
        "prix": "2295",
        "superficie_pi2": "n/d",
        "chambres": "2",
        "balcon": "n/d",
        "station_metro": "De Castelnau",
        "ligne_metro": "bleue",
        "minutes_a_pied": "2",
        "site": "logisquebec.com",
        "lien": "https://www.logisquebec.com/appartement-a-louer-villeray_saint-michel_parc-extension-l356226",
        "score": "3",
        "notes": "4½ (2 chambres), disponible sept. 2026, animaux non autorisés, superficie non indiquée",
        "photo": "",
    },
    {
        "date_ajout": TODAY,
        "statut": "NOUVEAU",
        "titre": "4½ (2 chambres), 932 pi² - avenue Louis-Hébert (Villeray), à 5 min du métro Fabre",
        "quartier": "Villeray",
        "adresse": "7175, Avenue Louis-Hébert, Montréal",
        "prix": "1900",
        "superficie_pi2": "932",
        "chambres": "2",
        "balcon": "n/d",
        "station_metro": "Fabre",
        "ligne_metro": "bleue",
        "minutes_a_pied": "5",
        "site": "centris.ca",
        "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/18922144",
        "score": "5",
        "notes": "Chambres au sous-sol (unité à paliers, pas un sous-sol complet), disponible 1er juillet 2026, animaux non précisés",
        "photo": "",
    },
]

with open(CSV_PATH, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)

existing_links = {r["lien"] for r in rows}
for nr in new_rows:
    if nr["lien"] in existing_links:
        raise SystemExit(f"DUPLICATE lien détecté, arrêt: {nr['lien']}")

# Passer les anciennes lignes NOUVEAU -> vu
for r in rows:
    if r["statut"] == "NOUVEAU":
        r["statut"] = "vu"

rows.extend(new_rows)

def sort_key(r):
    is_new = 0 if r["statut"] == "NOUVEAU" else 1
    try:
        score = -int(r["score"])
    except (ValueError, KeyError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

print(f"{len(new_rows)} nouvelles annonces ajoutées. Total: {len(rows)} lignes.")
