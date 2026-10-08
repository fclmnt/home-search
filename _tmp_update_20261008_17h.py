import csv

PATH = "annonces.csv"

with open(PATH, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# 1. Passer les anciens NOUVEAU à vu
for row in rows:
    if row['statut'] == 'NOUVEAU':
        row['statut'] = 'vu'

new_rows = [
{
 "date_ajout": "2026-10-08",
 "statut": "NOUVEAU",
 "titre": "1600 pi², 3 chambres + bureau, balcon avant/arrière - secteur Rosemont (Angus), entre métros St-Michel et Pie-IX",
 "quartier": "Rosemont",
 "adresse": "n/d (Montréal, QC H1T 1A6, secteur Rosemont/Angus)",
 "prix": "2100",
 "superficie_pi2": "1600",
 "chambres": "3",
 "balcon": "oui",
 "station_metro": "n/d",
 "ligne_metro": "n/d",
 "minutes_a_pied": "n/d",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/1600-sq-ft-3-bedroom-2-bathroom-apartment-for-rent-in-rosemont/1716389968",
 "score": "8",
 "notes": "500 pi2 additionnels au sous-sol, 2 salles de bain, porche avant + deck arriere, laveuse-secheuse avec raccordements, animaux non acceptes, disponible depuis le 15 aout 2026, desservi par autobus vers metros St-Michel et Pie-IX (distance de marche non precisee)",
 "photo": "",
},
{
 "date_ajout": "2026-10-08",
 "statut": "NOUVEAU",
 "titre": "Rénové avec parking garage privé, 3 chambres, 1100 pi², 2 balcons - 7234 Boul. Pie-IX, Rosemont",
 "quartier": "Rosemont",
 "adresse": "7234, Boulevard Pie-IX, Montréal",
 "prix": "1900",
 "superficie_pi2": "1100",
 "chambres": "3",
 "balcon": "oui",
 "station_metro": "n/d",
 "ligne_metro": "n/d",
 "minutes_a_pied": "n/d",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/rosemont-5-1-2-renove-avec-parking-garage-prive/1744243391",
 "score": "8",
 "notes": "Secteur entre Villeray et Petite-Patrie, rez-de-chaussee bien isole, parking garage prive inclus, laveuse-secheuse + lave-vaisselle inclus, climatisation, animaux limites, eau incluse, disponible fin oct./1er nov. 2026, station de metro la plus proche non confirmee par l'annonce",
 "photo": "",
},
{
 "date_ajout": "2026-10-08",
 "statut": "NOUVEAU",
 "titre": "Grand 5½ avec solarium, 3 chambres, superficie annoncée 3000 pi² (à vérifier) - secteur Rosemont",
 "quartier": "Rosemont",
 "adresse": "n/d (Montréal, QC H1T 3S4, Rosemont)",
 "prix": "2200",
 "superficie_pi2": "3000",
 "chambres": "3",
 "balcon": "oui",
 "station_metro": "n/d",
 "ligne_metro": "n/d",
 "minutes_a_pied": "n/d",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-5-a-louer-rosemont-montreal/1744376633",
 "score": "8",
 "notes": "Superficie de 3000 pi2 annoncee, possiblement surestimee/erreur de l'annonceur - a verifier avant visite; solarium avec rideau automatique, cour arriere, chauffage et electricite inclus, garage interieur + stationnement exterieur, animaux non acceptes, disponible 1er nov. 2026, metro a proximite (non precise)",
 "photo": "",
},
{
 "date_ajout": "2026-10-08",
 "statut": "NOUVEAU",
 "titre": "5½ complètement rénové, 3 chambres, 930 pi² - sur la Promenade Masson, Vieux-Rosemont",
 "quartier": "Rosemont / La Petite-Patrie",
 "adresse": "n/d (Montréal, QC H1Y 1W9, Promenade Masson)",
 "prix": "1950",
 "superficie_pi2": "930",
 "chambres": "3",
 "balcon": "n/d",
 "station_metro": "n/d",
 "ligne_metro": "n/d",
 "minutes_a_pied": "n/d",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/5-1-2-renove-rosemont-petite-patrie/1736299730",
 "score": "5",
 "notes": "Sur la Promenade Masson (quartier commercant: cafes, epicerie, boulangerie a pied), climatise, animaux limites, non meuble, disponible 20 avril 2026 (date lointaine, a confirmer), balcon non mentionne dans l'annonce, station de metro non precisee",
 "photo": "",
},
{
 "date_ajout": "2026-10-08",
 "statut": "NOUVEAU",
 "titre": "3 chambres (5½), 1005 pi², 2 balcons - secteur Rosemont-Petite-Patrie",
 "quartier": "Rosemont / La Petite-Patrie",
 "adresse": "n/d (Montréal, QC H1T 1H8, Rosemont-Petite-Patrie)",
 "prix": "1950",
 "superficie_pi2": "1005",
 "chambres": "3",
 "balcon": "oui",
 "station_metro": "n/d",
 "ligne_metro": "n/d",
 "minutes_a_pied": "n/d",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/appartement-3-chambres-5-5-a-louer-dans-rosemont-petite-patrie/1744531044",
 "score": "7",
 "notes": "Cuisine et salle de bain neuves, planchers sables/vernis, laveuse-secheuse in-unit, petit animal tranquille possiblement tolere, disponible 15 oct. 2026, station de metro non precisee par l'annonce",
 "photo": "",
},
{
 "date_ajout": "2026-10-08",
 "statut": "NOUVEAU",
 "titre": "5½ rez-de-chaussée rénové, 2 chambres fermées, 1000 pi², balcon + cour privée - Vieux-Rosemont près Promenade Masson",
 "quartier": "Rosemont / La Petite-Patrie",
 "adresse": "n/d (Montréal, QC H1Y 1S9, Vieux-Rosemont)",
 "prix": "1995",
 "superficie_pi2": "1000",
 "chambres": "2",
 "balcon": "oui",
 "station_metro": "n/d",
 "ligne_metro": "n/d",
 "minutes_a_pied": "n/d",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/rez-de-chaussee-vieux-rosemont-5-electromenagers-1er-dec/1742946182",
 "score": "6",
 "notes": "A un coin de rue de la Promenade Masson (quartier commercant), thermopompe incluse, electricite en sus (~150$/mois), accepte un chat, non-fumeur, grand sous-sol non fini, disponible 1er dec. 2026, nombre de chambres fermees decrit comme '1 ou 2' par l'annonce - compte conservateur de 2, station de metro non precisee",
 "photo": "",
},
{
 "date_ajout": "2026-10-08",
 "statut": "NOUVEAU",
 "titre": "5½ meublé, 3 chambres, 1100 pi², jardin/terrasse/cour arrière - aux Promenades Masson",
 "quartier": "Rosemont / La Petite-Patrie",
 "adresse": "n/d (Montréal, QC H1Y 2N3, Promenades Masson)",
 "prix": "2100",
 "superficie_pi2": "1100",
 "chambres": "3",
 "balcon": "oui",
 "station_metro": "n/d",
 "ligne_metro": "n/d",
 "minutes_a_pied": "n/d",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/magnifique-5-1-2-aux-promenades-masson/1744395250",
 "score": "8",
 "notes": "Meuble, rez-de-chaussee, climatisation/chauffage/electricite/eau inclus, 1 stationnement inclus, animaux acceptes, disponible 1er nov. 2026, pres de la Promenade Masson (quartier commercant), station de metro non precisee",
 "photo": "",
},
{
 "date_ajout": "2026-10-08",
 "statut": "NOUVEAU",
 "titre": "5½ rénové, 3 grandes chambres, 1000 pi², thermopompe - Rosemont/La Petite-Patrie (Jeanne-d'Arc et Masson)",
 "quartier": "Rosemont / La Petite-Patrie",
 "adresse": "n/d (Montréal, QC H1X 2E8, intersection Jeanne-d'Arc et Masson)",
 "prix": "2250",
 "superficie_pi2": "1000",
 "chambres": "3",
 "balcon": "n/d",
 "station_metro": "Pie-IX",
 "ligne_metro": "verte",
 "minutes_a_pied": "n/d (non précisé, distance semble importante)",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/magnifique-5-renove-beautiful-renovated-3-bedroom-apartment/1743912100",
 "score": "5",
 "notes": "Cuisine comptoirs quartz, salle de bain renovee, thermopompe haute efficacite, stationnement prive pre-file pour borne electrique, animaux a discuter, disponible sept./maintenant selon l'annonce, pres de la Promenade Masson; l'annonce cite le metro Pie-IX comme le plus proche mais la distance de marche reelle n'est pas confirmee (probablement superieure a 12 min), balcon non mentionne",
 "photo": "",
},
{
 "date_ajout": "2026-10-08",
 "statut": "NOUVEAU",
 "titre": "7½ (4 chambres), 1500-1600 pi², 2 balcons, internet et stationnement inclus - 6635 20e avenue, Rosemont (près parc Étienne-Desmarteau)",
 "quartier": "Rosemont",
 "adresse": "6635, 20e Avenue, Montréal",
 "prix": "2150",
 "superficie_pi2": "1550",
 "chambres": "4",
 "balcon": "oui",
 "station_metro": "Pie-IX",
 "ligne_metro": "verte",
 "minutes_a_pied": "n/d (non précisé)",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/7-et-demi-rosemont-internet-parking-inclus-dispo-mtn/1744109211",
 "score": "8",
 "notes": "4 chambres fermees malgre le titre '7 et demi', pres du parc Etienne-Desmarteau, stationnement exterieur + internet inclus, 1 chat accepte (pas de chien), disponible depuis le 28 sept. 2026, l'annonce mentionne le metro Pie-IX comme acces transport mais la distance de marche exacte n'est pas confirmee",
 "photo": "",
},
{
 "date_ajout": "2026-10-08",
 "statut": "NOUVEAU",
 "titre": "3 grandes chambres, 1500 pi², balcon, thermopompe neuve - secteur Plateau/Mile End",
 "quartier": "Le Plateau-Mont-Royal",
 "adresse": "n/d (Montréal, QC H2V 4H4, secteur Mile End/Plateau)",
 "prix": "2200",
 "superficie_pi2": "1500",
 "chambres": "3",
 "balcon": "oui",
 "station_metro": "n/d",
 "ligne_metro": "n/d",
 "minutes_a_pied": "n/d",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/3-beds-1-bath-apartment-in-plateau/1743229407",
 "score": "8",
 "notes": "Thermopompe neuve (chauffage/climatisation/filtration), laveuse-secheuse incluses, 1 stationnement inclus, pas de frigo inclus, animaux limites, disponible 1er oct. 2026, 2e etage, hydro non inclus, station de metro non precisee par l'annonce",
 "photo": "",
},
]

# Dedup check (lien exact)
existing_links = set(r['lien'] for r in rows)
added = 0
for nr in new_rows:
    if nr['lien'] in existing_links:
        print("SKIP (déjà présent):", nr['lien'])
        continue
    rows.append(nr)
    added += 1

print(f"{added} nouvelles lignes ajoutées sur {len(new_rows)} candidates.")

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

print("Fichier annonces.csv mis à jour. Total lignes (hors en-tête):", len(rows))
