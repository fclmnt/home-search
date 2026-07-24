import csv

path = 'annonces.csv'
with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'

new_rows = [
{
 'date_ajout': '2026-07-24', 'statut': 'NOUVEAU',
 'titre': 'Condo 4½ de 1000 pi² rénové, entrée privée, 2 chambres fermées - Parc Angus (Rosemont), 900m du métro Joliette',
 'quartier': 'Rosemont-La Petite-Patrie',
 'adresse': '4295, Rue Moïse-Picard, Montréal',
 'prix': '1950', 'superficie_pi2': '1000', 'chambres': '2', 'balcon': 'oui',
 'station_metro': 'Joliette', 'ligne_metro': 'verte', 'minutes_a_pied': '11',
 'site': 'Marketplace', 'lien': 'https://www.facebook.com/marketplace/item/1326176662918618',
 'score': '8',
 'notes': "Condo entièrement rénové, entrée privée, 2 grandes chambres fermées + coin bureau, 2 balcons dont 1 grande terrasse, plancher chauffant salle de bain, thermopompe, situé dans les Shops Angus, disponible 31 juillet, lien exige une connexion Facebook",
 'photo': ''
},
{
 'date_ajout': '2026-07-24', 'statut': 'NOUVEAU',
 'titre': 'Cession de bail - Grand 5½ à Hochelaga, parking + terrasse, 10 min du métro Préfontaine',
 'quartier': 'Hochelaga-Maisonneuve',
 'adresse': 'Secteur rue Ontario / Promenades Ontario, Montréal',
 'prix': '2195', 'superficie_pi2': 'n/d', 'chambres': '2', 'balcon': 'oui',
 'station_metro': 'Préfontaine', 'ligne_metro': 'verte', 'minutes_a_pied': '10',
 'site': 'Marketplace', 'lien': 'https://www.facebook.com/marketplace/item/1026228803107774',
 'score': '6',
 'notes': "Cession de bail (bail court jusqu'en juin 2027), 2e et dernier étage, 2 vraies chambres + petit bureau, terrasse arrière + balcon avant, 1 place de stationnement incluse, animaux acceptés, près de la rue Ontario et Promenades Ontario, disponible 1er août, lien exige une connexion Facebook",
 'photo': ''
},
{
 'date_ajout': '2026-07-24', 'statut': 'NOUVEAU',
 'titre': 'Grand 4½ de 900 pi² avec balcon, électros et AC inclus - Hochelaga-Maisonneuve',
 'quartier': 'Hochelaga-Maisonneuve',
 'adresse': 'Montréal, QC H1W 3N5 (secteur Hochelaga-Maisonneuve)',
 'prix': '1900', 'superficie_pi2': '900', 'chambres': '2', 'balcon': 'oui',
 'station_metro': 'Joliette ou Pie-IX', 'ligne_metro': 'verte', 'minutes_a_pied': '5-10',
 'site': 'Kijiji', 'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-4-1-2-avec-balcon-electros-ac-inclus/1740573339',
 'score': '8',
 'notes': "2 chambres + bureau, grand balcon arrière avec vue sur jardin, laveuse/sécheuse, lave-vaisselle, thermopompe/climatisation, aucun animal, disponible 1er août, vérification de crédit exigée",
 'photo': ''
},
{
 'date_ajout': '2026-07-24', 'statut': 'NOUVEAU',
 'titre': '5½ de 998 pi², 2 chambres + bureau, balcon et accès cour - Plateau (rue St-André, entre Roy et Cherrier), 5 min du métro Sherbrooke',
 'quartier': 'Le Plateau-Mont-Royal',
 'adresse': 'Rue St-André (entre Roy et Cherrier), Montréal, QC H2L 3V7',
 'prix': '1950', 'superficie_pi2': '998', 'chambres': '2', 'balcon': 'oui',
 'station_metro': 'Sherbrooke', 'ligne_metro': 'orange', 'minutes_a_pied': '5',
 'site': 'Kijiji', 'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/5-1-2-plateau-2-ch-bureau-balcon-acces-cour/1740581764',
 'score': '7',
 'notes': "3e étage, 2 chambres fermées + bureau fermé avec accès balcon, cour partagée, chauffage non inclus, animaux limités (pas de chien), près du parc La Fontaine, disponible 1er août",
 'photo': ''
},
{
 'date_ajout': '2026-07-24', 'statut': 'NOUVEAU',
 'titre': '5½ de 1000 pi², 2 chambres, grande cour privée - Plateau (rue Parthenais), 5 min du métro Mont-Royal',
 'quartier': 'Le Plateau-Mont-Royal',
 'adresse': '4242, Rue Parthenais, Montréal, QC H2H 2G3',
 'prix': '1900', 'superficie_pi2': '1000', 'chambres': '2', 'balcon': 'n/d',
 'station_metro': 'Mont-Royal', 'ligne_metro': 'orange', 'minutes_a_pied': '5',
 'site': 'Kijiji', 'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/5-2-ch-plateau-est-cour-privee-stationnement-tout-equipe/1737761531',
 'score': '5',
 'notes': "Rez-de-chaussée, très grande cour arrière privée (pas de balcon mentionné), 2 places de stationnement en sus, laveuse/sécheuse et lave-vaisselle inclus, chauffage et eau chaude inclus, animaux à discuter, disponible immédiatement",
 'photo': ''
},
{
 'date_ajout': '2026-07-24', 'statut': 'NOUVEAU',
 'titre': '5½ de 1000 pi², 3 chambres, balcon - rue Berri, 200 m du métro Mont-Royal',
 'quartier': 'Le Plateau-Mont-Royal',
 'adresse': 'Rue Berri, Montréal, QC H2J 2R2',
 'prix': '2000', 'superficie_pi2': '1000', 'chambres': '3', 'balcon': 'oui',
 'station_metro': 'Mont-Royal', 'ligne_metro': 'orange', 'minutes_a_pied': '3',
 'site': 'Kijiji', 'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/plateau-logement-5-1000pi-2000/1740923305',
 'score': '8',
 'notes': "Plafonds de 9 pieds, fenêtres est-ouest, laveuse/sécheuse dans l'unité, pas de stationnement, non meublé, aucun animal, à 2 min des pharmacies/cafés/restos/épiceries, disponible 1er septembre",
 'photo': ''
},
{
 'date_ajout': '2026-07-24', 'statut': 'NOUVEAU',
 'titre': '5½ de 1100 pi², 3 chambres fermées - rue de Bullion (Plateau), 11 min du métro Sherbrooke',
 'quartier': 'Le Plateau-Mont-Royal',
 'adresse': '3984, Rue de Bullion, Montréal, QC H2W 2E4',
 'prix': '2275', 'superficie_pi2': '1100', 'chambres': '3', 'balcon': 'n/d',
 'station_metro': 'Sherbrooke', 'ligne_metro': 'orange', 'minutes_a_pied': '11',
 'site': 'Kijiji', 'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/5-1-2-au-plateau-three-3-bedroom-apartment-in-plateau/1740633307',
 'score': '7',
 'notes': "2e étage d'un 6-plex, plafonds de 9,5 pieds, planchers de bois, laveuse/sécheuse inclus, chauffage/électricité non inclus, animaux acceptés, disponible 1er août",
 'photo': ''
},
{
 'date_ajout': '2026-07-24', 'statut': 'NOUVEAU',
 'titre': 'Grand 5½ rénové de 1200 pi², 3 chambres - avenue Charlemagne (Rosemont), 7 min du métro Pie-IX',
 'quartier': 'Rosemont-La Petite-Patrie',
 'adresse': '4419, Av. Charlemagne, Montréal, QC H1X 2H2',
 'prix': '1900', 'superficie_pi2': '1200', 'chambres': '3', 'balcon': 'n/d',
 'station_metro': 'Pie-IX', 'ligne_metro': 'verte', 'minutes_a_pied': '7',
 'site': 'Kijiji', 'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-5-1-2-renove-a-louer-au-rdc-a-rosemont/1740506864',
 'score': '8',
 'notes': "Rez-de-chaussée, climatisation, près du Parc Maisonneuve, Jardin botanique, Stade olympique et Promenade Masson, aucun animal, disponible 1er juillet",
 'photo': ''
},
{
 'date_ajout': '2026-07-24', 'statut': 'NOUVEAU',
 'titre': '5½ lumineux de 946 pi², 2 chambres fermées, 2 balcons - Rosemont/La Petite-Patrie, près du métro Beaubien',
 'quartier': 'Rosemont-La Petite-Patrie',
 'adresse': 'Montréal, QC H2G 2S1 (secteur Cinéma Beaubien)',
 'prix': '1950', 'superficie_pi2': '946', 'chambres': '2', 'balcon': 'oui',
 'station_metro': 'Beaubien', 'ligne_metro': 'orange', 'minutes_a_pied': '10 (estimé)',
 'site': 'Kijiji', 'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/5-lumineux-2-ch-fermees-renove-rosemont-petite-patrie/1739560132',
 'score': '7',
 'notes': "3e étage, 2 chambres fermées + salle à manger (ancienne 3e chambre), salle de bain avec puits de lumière, laveuse/sécheuse et lave-vaisselle inclus, animaux limités, près de la rue St-Hubert et Cinéma Beaubien, disponible 1er juillet",
 'photo': ''
},
]

# dedupe check against existing links (safety)
existing_links = {r['lien'] for r in rows}
added = 0
for nr in new_rows:
    if nr['lien'] not in existing_links:
        rows.append(nr)
        added += 1

def sort_key(r):
    is_new = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        score = -int(r['score'])
    except:
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Added {added} new rows. Total rows now: {len(rows)}")
