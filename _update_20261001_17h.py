import csv

path = "annonces.csv"
with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# 1. flip old NOUVEAU -> vu
for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'

today = "2026-10-01"

new_rows = [
{
 "date_ajout": today,
 "statut": "NOUVEAU",
 "titre": "5½ avec garage, 3 chambres fermées, 2 balcons - boulevard Pie-IX (Rosemont/Villeray), à 12 min du métro Saint-Michel",
 "quartier": "Rosemont-La Petite-Patrie",
 "adresse": "7238, Boulevard Pie-IX, Montréal, QC",
 "prix": "1925",
 "superficie_pi2": "1100",
 "chambres": "3",
 "balcon": "oui (2 balcons)",
 "station_metro": "Saint-Michel",
 "ligne_metro": "bleue",
 "minutes_a_pied": "12 (estimé, 980 m)",
 "site": "LogisQuebec",
 "lien": "https://www.logisquebec.com/appartement-a-louer-rosemont_la-petite-patrie-l363372",
 "score": "9",
 "notes": "Garage privé inclus, rez-de-chaussée bien isolé, électroménagers inclus (cuisinière, frigo, laveuse-sécheuse), disponible immédiatement. Situé entre Villeray et Petite-Patrie, près de Jean-Talon Est. Chauffage et électricité non inclus.",
 "photo": "",
},
{
 "date_ajout": today,
 "statut": "NOUVEAU",
 "titre": "Condo 4½ rénové, 2 chambres fermées, grande terrasse privée - rue Saint-Hubert (Villeray), à quelques pas du métro Jean-Talon",
 "quartier": "Villeray-Saint-Michel-Parc-Extension",
 "adresse": "7250, Rue Saint-Hubert, app. 305, Montréal, QC",
 "prix": "2400",
 "superficie_pi2": "1003",
 "chambres": "2",
 "balcon": "oui",
 "station_metro": "Jean-Talon",
 "ligne_metro": "orange/bleue",
 "minutes_a_pied": "7 (estimé)",
 "site": "Centris",
 "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/21269608",
 "score": "7",
 "notes": "2 salles de bain complètes, 1 place de stationnement garage, rangement inclus, cuisine moderne aire ouverte, Walk Score 99, libre 1er déc. 2026. Métro Jean-Talon (lignes orange et bleue) à quelques pas selon l'annonce.",
 "photo": "",
},
{
 "date_ajout": today,
 "statut": "NOUVEAU",
 "titre": "5½ lumineux rénové, 3 chambres fermées, balcon et thermopompe - secteur Saint-Michel, à 9 min du métro Saint-Michel",
 "quartier": "Villeray-Saint-Michel-Parc-Extension",
 "adresse": "Montréal, QC H2A 2P9 (secteur Saint-Michel, près du parc St-Bernadette)",
 "prix": "2150",
 "superficie_pi2": "980",
 "chambres": "3",
 "balcon": "oui",
 "station_metro": "Saint-Michel",
 "ligne_metro": "bleue",
 "minutes_a_pied": "9 (estimé)",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/logement-5-1-2-lumineux-a-louer/1744132273",
 "score": "8",
 "notes": "Thermopompe murale haute performance, douche italienne, aspirateur central, laveuse-sécheuse, chauffage inclus. Pas d'animaux, non-fumeur, bail 1 an, aucun Airbnb/sous-location permis, libre 30 sept. 2026. Accès également à la nouvelle station Pie-IX (ligne bleue). Adresse exacte non précisée par l'annonceur.",
 "photo": "",
},
{
 "date_ajout": today,
 "statut": "NOUVEAU",
 "titre": "Condo 4½ rénové, 2 chambres fermées, terrasse privée - rue Sherbrooke Est (Plateau-Mont-Royal), proche du métro Papineau",
 "quartier": "Le Plateau-Mont-Royal",
 "adresse": "2121, Rue Sherbrooke Est, app. 102, Montréal, QC H2K 1C2",
 "prix": "2300",
 "superficie_pi2": "1012",
 "chambres": "2",
 "balcon": "oui",
 "station_metro": "Papineau",
 "ligne_metro": "verte",
 "minutes_a_pied": "8 (estimé)",
 "site": "Centris",
 "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-le-plateau-mont-royal/26877857",
 "score": "8",
 "notes": "Planchers de bois franc, cuisine à aire ouverte, semi-meublé, 1 salle de bain, libre 1er déc. 2026, Walk Score 97. Distance au métro Papineau (ligne verte) estimée à partir de l'intersection Sherbrooke/Papineau (annonce ne précise pas la station exacte).",
 "photo": "",
},
]

rows = new_rows + rows

def sort_key(r):
    status_rank = 0 if r['statut'] == 'NOUVEAU' else 1
    return (status_rank, -int(r['score']))

rows.sort(key=sort_key)

with open(path, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    writer.writerows(rows)

print("done, total rows:", len(rows))
