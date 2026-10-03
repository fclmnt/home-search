#!/usr/bin/env python3
import csv

FIELDS = ["date_ajout","statut","titre","quartier","adresse","prix","superficie_pi2",
          "chambres","balcon","station_metro","ligne_metro","minutes_a_pied","site",
          "lien","score","notes","photo"]

with open('annonces.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

# Passer les anciens NOUVEAU à vu
for row in rows:
    if row['statut'] == 'NOUVEAU':
        row['statut'] = 'vu'

today = '2026-10-03'

new_rows = [
{
 "date_ajout": today, "statut": "NOUVEAU",
 "titre": "Grand 5½ rénové (2 chambres), 1000 pi², jardin privé clôturé - rue Cuvillier (Hochelaga), à 4 min du métro Joliette",
 "quartier": "Hochelaga-Maisonneuve",
 "adresse": "2265, Rue Cuvillier, Montréal, QC H1W 3A8",
 "prix": "2010", "superficie_pi2": "1000", "chambres": "2", "balcon": "non (jardin privé clôturé)",
 "station_metro": "Joliette", "ligne_metro": "verte", "minutes_a_pied": "4",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-5-jardin-cloture-chiens-et-chats-acceptes-hochelaga/1744249653",
 "score": "6",
 "notes": "Rez-de-chaussée sans escalier, cession de bail jusqu'au 30 juin 2027, jardin privé clôturé (max 2 animaux acceptés), internet haute vitesse inclus (valeur 80$), laveuse-sécheuse/lave-vaisselle/frigo/cuisinière inclus, toutes charges incluses sauf électricité, pas de stationnement, non-fumeur, disponible immédiatement.",
 "photo": ""
},
{
 "date_ajout": today, "statut": "NOUVEAU",
 "titre": "Grand 5½ (2 chambres + bureau fermé), balcon et grande terrasse, parking inclus - secteur Hochelaga/Préfontaine, à 10 min du métro Préfontaine",
 "quartier": "Hochelaga-Maisonneuve",
 "adresse": "n/d (secteur Hochelaga/Préfontaine, 2e et dernier étage, Montréal, QC)",
 "prix": "2195", "superficie_pi2": "n/d", "chambres": "2", "balcon": "oui (balcon avant + grande terrasse arrière)",
 "station_metro": "Préfontaine", "ligne_metro": "verte", "minutes_a_pied": "10",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-5-a-hochelaga-parking-terrasse-2-195-dispo/1739376269",
 "score": "6",
 "notes": "2 chambres fermées + petit bureau séparé, stationnement inclus, animaux acceptés (chiens compris), climatisation, hydro inclus, laveuse-sécheuse et lave-vaisselle inclus, chauffage non précisé, vérification de crédit exigée, disponible 1er août 2026 (cession de bail jusqu'en juin 2027), proche des commerces de la rue Ontario et des Promenades Ontario. Superficie non précisée par l'annonce.",
 "photo": ""
},
{
 "date_ajout": today, "statut": "NOUVEAU",
 "titre": "Spacieux 4½ rénové (2 chambres), 950 pi², 2 balcons - La Petite-Patrie, à quelques minutes du métro Rosemont",
 "quartier": "Rosemont-La Petite-Patrie",
 "adresse": "n/d (La Petite-Patrie, Montréal, QC H2S 2H7)",
 "prix": "1975", "superficie_pi2": "950", "chambres": "2", "balcon": "oui (avant et arrière)",
 "station_metro": "Rosemont", "ligne_metro": "verte", "minutes_a_pied": "5-8 (estimé)",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/spacieux-4-a-deux-pas-du-metro-rosemont/1743420224",
 "score": "8",
 "notes": "3e étage d'un sixplex sur rue calme, logement lumineux et bien aéré, eau incluse, laveuse-sécheuse et lave-vaisselle inclus, meubles disponibles au même prix si désiré, animaux limités, 1 mois gratuit jusqu'au 1er décembre, disponible 13 sept. 2026, bail 1 an. L'annonce indique le métro Rosemont « à quelques minutes » sans précision exacte.",
 "photo": ""
},
{
 "date_ajout": today, "statut": "NOUVEAU",
 "titre": "4½ rénové avec sous-sol aménagé (2 chambres), 900 pi², balcon - rue Marie-Anne Est (Plateau), près des métros Mont-Royal et Saint-Laurent",
 "quartier": "Le Plateau-Mont-Royal",
 "adresse": "172, Rue Marie-Anne Est, Montréal, QC H2W 1A5",
 "prix": "1940", "superficie_pi2": "900", "chambres": "2", "balcon": "oui",
 "station_metro": "Mont-Royal", "ligne_metro": "verte", "minutes_a_pied": "7 (estimé)",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/4-1-2-basement-plateau-mont-royal-lease-transfer-1940/1743197854",
 "score": "8",
 "notes": "Cession de bail du 1er oct. 2026 au 30 juin 2027, 1er mois gratuit (moyenne effective ~1724$/mois sur 9 mois), rez-de-chaussée avec sous-sol aménagé (salle familiale + buanderie), chauffage électrique payé par le locataire, meublé (frigo/cuisinière/laveuse-sécheuse), aucun animal. Distance aux métros Mont-Royal et Saint-Laurent estimée à partir de l'adresse (non précisée par l'annonce).",
 "photo": ""
},
{
 "date_ajout": today, "statut": "NOUVEAU",
 "titre": "Grand 4½ neuf, dernier étage (2 chambres + bureau fermé), 900 pi², 2 balcons - avenue Gascon (Centre-Sud/Plateau), à 7 min des métros Frontenac/Préfontaine",
 "quartier": "Ville-Marie (Centre-Sud) / Le Plateau-Mont-Royal",
 "adresse": "n/d (Avenue Gascon, Montréal, QC)",
 "prix": "1900", "superficie_pi2": "900", "chambres": "2", "balcon": "oui (2 balcons)",
 "station_metro": "Frontenac / Préfontaine", "ligne_metro": "verte", "minutes_a_pied": "7",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-4-neuf-dernier-etage-vue-plateau-ville-marie/1739397387",
 "score": "8",
 "notes": "Entièrement rénové (cuisine, salle de bain, plancher, façade), 2 chambres fermées + bureau/salon fermé pouvant servir de 3e chambre, laveuse-sécheuse à l'unité, climatisation, eau et internet inclus, chats acceptés, prix promotionnel 1re année à 1900$ (régulier 2000$ - à vérifier au renouvellement), disponible 5 sept. 2026, bail 1 an. Pourrait être un autre logement du même immeuble que l'annonce avenue Gascon déjà au fichier (2553, Avenue Gascon).",
 "photo": ""
},
{
 "date_ajout": today, "statut": "NOUVEAU",
 "titre": "Cession de bail - 4½ (2 chambres, 2 sdb), 1000 pi², terrasse et cour - Villeray, à deux pas du métro Jarry",
 "quartier": "Villeray-Saint-Michel-Parc-Extension",
 "adresse": "n/d (secteur Parc Jarry, Montréal, QC H2T 2V2)",
 "prix": "2230", "superficie_pi2": "1000", "chambres": "2", "balcon": "oui (grande terrasse + cour)",
 "station_metro": "Jarry", "ligne_metro": "orange", "minutes_a_pied": "5 (estimé)",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/lease-transfer-spacious-2-bed-2-bath-in-villeray/1744270943",
 "score": "7",
 "notes": "2 chambres, 2 salles de bain, rez-de-chaussée avec grande terrasse et cour, à quelques pas du parc Jarry et du métro Jarry (ligne orange). Frigo/cuisinière/lave-vaisselle inclus, branchements laveuse-sécheuse, chauffage et électricité non inclus, animaux acceptés, non-fumeur, cession de bail dès le 1er déc. 2025 jusqu'au 1er mai 2026 puis renouvelable.",
 "photo": ""
},
{
 "date_ajout": today, "statut": "NOUVEAU",
 "titre": "Beau 6½ (4 chambres fermées), 1200 pi², climatisation - secteur Villeray/Rosemont, à 9 min du métro Fabre",
 "quartier": "Villeray-Saint-Michel-Parc-Extension",
 "adresse": "n/d (secteur métro Fabre, Villeray/Rosemont, Montréal, QC)",
 "prix": "2350", "superficie_pi2": "1200", "chambres": "4", "balcon": "n/d",
 "station_metro": "Fabre", "ligne_metro": "bleue", "minutes_a_pied": "9",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/beau-6-4cac-metro-fabre-villeray-rosemont/1743964018",
 "score": "7",
 "notes": "Climatisation incluse, pas de stationnement, animaux limités aux chats, non-fumeur (intérieur et extérieur), cannabis interdit, bail 1 an, secteur très calme, Walk Score 10/Transit Score 10, proche d'une station BIXI. Disponible 1er oct. 2026. Présence d'un balcon non précisée par l'annonce.",
 "photo": ""
},
{
 "date_ajout": today, "statut": "NOUVEAU",
 "titre": "Magnifique 6½ rénové (4 chambres fermées), 1340 pi², balcon et grande cour - Villeray/Saint-Michel, à 5 min du métro Saint-Michel",
 "quartier": "Villeray-Saint-Michel-Parc-Extension",
 "adresse": "n/d (Montréal, QC H2A 2A5, secteur Villeray-Saint-Michel)",
 "prix": "2150", "superficie_pi2": "1340", "chambres": "4", "balcon": "oui (balcon + grande cour arrière)",
 "station_metro": "Saint-Michel", "ligne_metro": "bleue", "minutes_a_pied": "5",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/magnifique-6-5-renove-avec-enorme-cour-a-villeray-st-michel/1744161361",
 "score": "9",
 "notes": "Rez-de-chaussée, planchers de bois, grande cour arrière avec arbre mature, garage + 3 places de stationnement, frigo et four inclus, branchements laveuse-sécheuse au sous-sol, aucun animal, non-fumeur, bail mois par mois, vérification de crédit complète exigée, disponible 1er nov. 2026.",
 "photo": ""
},
]

rows.extend(new_rows)

# Tri : NOUVEAU d'abord, puis score décroissant
def sort_key(row):
    is_new = 0 if row['statut'] == 'NOUVEAU' else 1
    try:
        score = -int(row['score'])
    except (ValueError, TypeError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    w.writerows(rows)

print("Total rows:", len(rows))
print("Nouveaux:", sum(1 for r in rows if r['statut']=='NOUVEAU'))
