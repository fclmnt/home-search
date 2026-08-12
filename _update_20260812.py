import csv

FIELDS = ["date_ajout","statut","titre","quartier","adresse","prix","superficie_pi2","chambres","balcon","station_metro","ligne_metro","minutes_a_pied","site","lien","score","notes","photo"]

with open('annonces.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'

new_rows = [
{
 "date_ajout":"2026-08-12","statut":"NOUVEAU",
 "titre":"3 chambres fermées (1152 pi²) meublé, chauffé, WiFi inclus, terrasse - Promenade Ontario, Hochelaga-Maisonneuve, à 5 min du métro Joliette",
 "quartier":"Hochelaga-Maisonneuve","adresse":"Promenade Ontario, Montréal, QC H1W 1R9 (numéro civique non précisé)",
 "prix":"2400","superficie_pi2":"1152","chambres":"3","balcon":"oui","station_metro":"Joliette","ligne_metro":"verte","minutes_a_pied":"5",
 "site":"Kijiji","lien":"https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/3-chambres-wifi-meuble-eclaire-chauffe-metro-joliette-terrasse/1741860585",
 "score":"10","notes":"Entièrement meublé et équipé, WiFi et chauffage inclus, climatisation, buanderie, 2 salles de bain, animaux limités, disponible 11 août 2026. Airbnb/sous-location/garderie/commerce interdits.",
 "photo":""
},
{
 "date_ajout":"2026-08-12","statut":"NOUVEAU",
 "titre":"5½ (2 chambres, 1000 pi²) avec balcon, animaux acceptés - Hochelaga-Maisonneuve, à 8 min du métro Joliette",
 "quartier":"Hochelaga-Maisonneuve","adresse":"Montréal, QC H1W 3A8 (adresse exacte non précisée par l'annonceur)",
 "prix":"1995","superficie_pi2":"1000","chambres":"2","balcon":"oui","station_metro":"Joliette","ligne_metro":"verte","minutes_a_pied":"8",
 "site":"Kijiji","lien":"https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/simon/1741402243",
 "score":"8","notes":"Annonce titrée « Simon », adresse exacte non fournie par l'annonceur — à valider avant visite. 2 chambres fermées + 1 pièce moyenne sans fenêtre. Animaux acceptés (chiens et chats), disponible 1er septembre 2026 (entrée possible dès le 21 août).",
 "photo":""
},
{
 "date_ajout":"2026-08-12","statut":"NOUVEAU",
 "titre":"7½ (3 chambres, 1200 pi²) cachet d'origine 1907 - La Petite-Patrie, à 2 min du métro Beaubien",
 "quartier":"La Petite-Patrie/Rosemont","adresse":"Montréal, QC H2S 2R7 (adresse exacte non précisée par l'annonceur)",
 "prix":"2290","superficie_pi2":"1200","chambres":"3","balcon":"n/d","station_metro":"Beaubien","ligne_metro":"orange","minutes_a_pied":"2",
 "site":"Kijiji","lien":"https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/71-2-3-cac-metro-beaubien/1741631676",
 "score":"7","notes":"Cachet d'origine 1907, non meublé, non-fumeur, aucun animal, disponible 1er septembre 2026. Présence d'un balcon non mentionnée dans l'annonce.",
 "photo":""
},
{
 "date_ajout":"2026-08-12","statut":"NOUVEAU",
 "titre":"5½ (3 chambres, 1000 pi²) avec balcon arrière - rue Saint-Dominique, Plateau-Mont-Royal (Quartier Latin), à 7 min du métro Saint-Laurent",
 "quartier":"Le Plateau-Mont-Royal (secteur Quartier Latin/UQAM)","adresse":"3477, Rue Saint-Dominique, Montréal",
 "prix":"2200","superficie_pi2":"1000","chambres":"3","balcon":"oui","station_metro":"Saint-Laurent","ligne_metro":"verte","minutes_a_pied":"7",
 "site":"Kijiji","lien":"https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/plateau-superbe-5-1-2-de-3-chambres-disponible-le-1er-juillet/1741717185",
 "score":"9","notes":"Four/frigo/laveuse/sécheuse inclus, climatisation, eau incluse, bail 1 an, animaux limités, disponible 1er juillet 2026. L'annonce mentionnait le métro Sherbrooke mais la station la plus proche vérifiée est Saint-Laurent.",
 "photo":""
},
{
 "date_ajout":"2026-08-12","statut":"NOUVEAU",
 "titre":"5½ (3 chambres, 1250 pi²) avec balcon, plancher flottant neuf - rue Léonard-De Vinci, Villeray/Saint-Michel, à 11 min du métro Saint-Michel",
 "quartier":"Saint-Michel/Villeray","adresse":"rue Léonard-De Vinci, entre 17e et 18e avenue, Montréal, QC H2A 2N9",
 "prix":"1935","superficie_pi2":"1250","chambres":"3","balcon":"oui","station_metro":"Saint-Michel","ligne_metro":"bleue","minutes_a_pied":"11",
 "site":"Kijiji","lien":"https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-5-1-2-dans-villeray-a-louer-pour-septembre/1741798163",
 "score":"9","notes":"2e étage, plancher flottant neuf, aucun animal, non-fumeur, bail 1 an, disponible 1er septembre 2026.",
 "photo":""
},
{
 "date_ajout":"2026-08-12","statut":"NOUVEAU",
 "titre":"5½ (3 chambres) avec concierge, électros inclus - rue Davidson, Hochelaga-Maisonneuve, à 3 min du métro Joliette",
 "quartier":"Hochelaga-Maisonneuve","adresse":"2591 Rue Davidson, Montréal, QC H1W 2Z3",
 "prix":"2095","superficie_pi2":"n/d","chambres":"3","balcon":"n/d","station_metro":"Joliette","ligne_metro":"verte","minutes_a_pied":"3",
 "site":"Logisquebec","lien":"https://www.logisquebec.com/appartement-a-louer-mercier_hochelaga-maisonneuve-l357002",
 "score":"5","notes":"Deux unités disponibles dans l'immeuble (102 et 302, même prix), disponible maintenant, animaux acceptés (petits), électros inclus (four, micro-ondes, laveuse-sécheuse, lave-vaisselle, frigo), concierge sur place.",
 "photo":"https://i.logisquebec.com/i-a-louer/80864/357002/1.jpg"
},
{
 "date_ajout":"2026-08-12","statut":"NOUVEAU",
 "titre":"5½ (3 chambres, 1100 pi²) meublé, mur de brique - rue Saint-Dominique, Plateau-Mont-Royal (limite Mile-End), à 6 min du métro Rosemont",
 "quartier":"Le Plateau-Mont-Royal (limite Mile-End)","adresse":"5561 Rue Saint-Dominique, Montréal",
 "prix":"2075","superficie_pi2":"1100","chambres":"3","balcon":"oui","station_metro":"Rosemont","ligne_metro":"orange","minutes_a_pied":"6",
 "site":"Logisquebec","lien":"https://www.logisquebec.com/appartement-a-louer-le-plateau-mont-royal-l357139",
 "score":"9","notes":"Meublé et équipé, wifi inclus, disponible immédiatement, mur de brique apparent, salon/salle à manger ouvert.",
 "photo":"https://i.logisquebec.com/i-a-louer/112098/357139/img_5778_jpg_6a7b438a91d83.jpg"
},
{
 "date_ajout":"2026-08-12","statut":"NOUVEAU",
 "titre":"5½ (3 chambres, 1100 pi²) rez-de-chaussée avec terrasse - rue Saint-Dominique, Plateau-Mont-Royal (limite Mile-End), à 6 min du métro Rosemont",
 "quartier":"Le Plateau-Mont-Royal (limite Mile-End)","adresse":"5571 Rue Saint-Dominique, Montréal",
 "prix":"2075","superficie_pi2":"1100","chambres":"3","balcon":"oui","station_metro":"Rosemont","ligne_metro":"orange","minutes_a_pied":"6",
 "site":"Logisquebec","lien":"https://www.logisquebec.com/appartement-a-louer-le-plateau-mont-royal-l357134",
 "score":"9","notes":"Rez-de-chaussée, accès à une petite terrasse (BBQ + rangement), tous électroménagers inclus, disponible immédiatement. Unité voisine de celle du 5561 Saint-Dominique (même secteur).",
 "photo":"https://i.logisquebec.com/i-a-louer/112098/357134/758427288_10174783720475263_3825985666760897901_n_jpg_6a7b3e3cb1ac5.jpg"
},
{
 "date_ajout":"2026-08-12","statut":"NOUVEAU",
 "titre":"5½ spacieux (3 chambres) avec balcon sur rue - 13e avenue, Villeray, à 5 min du métro Saint-Michel",
 "quartier":"Villeray/Saint-Michel/Parc-Extension","adresse":"13e Avenue, Montréal (numéro civique non précisé)",
 "prix":"2250","superficie_pi2":"n/d","chambres":"3","balcon":"oui","station_metro":"Saint-Michel","ligne_metro":"orange","minutes_a_pied":"5",
 "site":"Logisquebec","lien":"https://www.logisquebec.com/appartement-a-louer-villeray_saint-michel_parc-extension-l356898",
 "score":"6","notes":"Bail jusqu'au 30 juin 2027, disponible immédiatement, aucun animal, thermostats électroniques, hydro/internet à la charge du locataire (~30$+20$/mois).",
 "photo":""
},
]

rows.extend(new_rows)

def sort_key(r):
    is_new = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        score = -int(r['score'])
    except:
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    for r in rows:
        w.writerow(r)

print("Total rows:", len(rows))
print("New rows added:", len(new_rows))
