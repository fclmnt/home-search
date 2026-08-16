# -*- coding: utf-8 -*-
import csv

PATH = 'annonces.csv'
FIELDS = ['date_ajout','statut','titre','quartier','adresse','prix','superficie_pi2',
          'chambres','balcon','station_metro','ligne_metro','minutes_a_pied','site',
          'lien','score','notes','photo']

with open(PATH, newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'

TODAY = '2026-08-16'

new_rows = [
{
 'date_ajout': TODAY, 'statut': 'NOUVEAU',
 'titre': "5½ meublé, balcon arrière - rue Saint-Dominique (Plateau)",
 'quartier': 'Le Plateau-Mont-Royal',
 'adresse': '3477, Rue Saint-Dominique, Montréal, QC',
 'prix': '2100', 'superficie_pi2': '1000', 'chambres': '3', 'balcon': 'oui (balcon arrière au 2e étage)',
 'station_metro': 'Sherbrooke', 'ligne_metro': 'orange', 'minutes_a_pied': '7',
 'site': 'Logis Québec',
 'lien': 'https://www.logisquebec.com/appartement-a-louer-le-plateau-mont-royal-l357644',
 'score': '8',
 'notes': "Meublé partiellement, four/frigo/laveuse-sécheuse inclus, disponible immédiatement, aucune mention d'animaux.",
 'photo': '',
},
{
 'date_ajout': TODAY, 'statut': 'NOUVEAU',
 'titre': "5½ rénové, petite terrasse - rue Saint-Dominique (Plateau, limite Mile-End)",
 'quartier': 'Le Plateau-Mont-Royal (limite Mile-End)',
 'adresse': '5571 Rue Saint-Dominique, Montréal',
 'prix': '2000', 'superficie_pi2': '1100', 'chambres': '3', 'balcon': 'oui (terrasse + rangement)',
 'station_metro': 'Rosemont', 'ligne_metro': 'orange', 'minutes_a_pied': '6',
 'site': 'Logis Québec',
 'lien': 'https://www.logisquebec.com/appartement-a-louer-le-plateau-mont-royal-l357647',
 'score': '9',
 'notes': "Disponible immédiatement. Même immeuble déjà repéré au 5561/5571 à 2075$ précédemment; nouvelle fiche à prix réduit.",
 'photo': '',
},
{
 'date_ajout': TODAY, 'statut': 'NOUVEAU',
 'titre': "4½ meublé, cour privée - rue Saint-Dominique (Villeray/Petite Italie)",
 'quartier': 'Villeray',
 'adresse': '6723, Rue Saint-Dominique, Montréal',
 'prix': '2000', 'superficie_pi2': '1200', 'chambres': '2', 'balcon': 'n/d (grande cour arrière privée + jardin)',
 'station_metro': 'De Castelnau', 'ligne_metro': 'orange', 'minutes_a_pied': '5-8',
 'site': 'Logis Québec',
 'lien': 'https://www.logisquebec.com/appartement-a-louer-villeray_saint-michel_parc-extension-l357656',
 'score': '6',
 'notes': "Meublé, hydro inclus, animaux acceptés. Bail non renouvelable de 9 mois (1er oct. au 30 juin 2027).",
 'photo': '',
},
{
 'date_ajout': TODAY, 'statut': 'NOUVEAU',
 'titre': "5½ rénové, balcon - avenue Bourbonnière (Vieux-Rosemont / frontière Hochelaga)",
 'quartier': 'Rosemont-La Petite-Patrie (Vieux-Rosemont, frontière Hochelaga-Maisonneuve)',
 'adresse': '5100 Avenue Bourbonnière, app. 6, Montréal, QC H1X 2M8',
 'prix': '2200', 'superficie_pi2': 'n/d', 'chambres': '3', 'balcon': 'oui',
 'station_metro': 'Pie-IX', 'ligne_metro': 'verte', 'minutes_a_pied': '10',
 'site': 'Zumper',
 'lien': 'https://www.zumper.com/address/5100-ave-bourbonniere-montreal-qc-h1x-2m8-can',
 'score': '7',
 'notes': "Laveuse/sécheuse en unité incluses. Aucun animal accepté. Proche du Stade olympique.",
 'photo': '',
},
{
 'date_ajout': TODAY, 'statut': 'NOUVEAU',
 'titre': "4½ loft meublé, tout inclus - rue Saint-André (Villeray / Marché Jean-Talon)",
 'quartier': 'Villeray',
 'adresse': '7026 Rue Saint-André, Montréal',
 'prix': '2250', 'superficie_pi2': '950', 'chambres': '2', 'balcon': 'n/d',
 'station_metro': 'Jean-Talon', 'ligne_metro': 'orange', 'minutes_a_pied': '2',
 'site': 'Logis Québec',
 'lien': 'https://www.logisquebec.com/appartement-a-louer-villeray_saint-michel_parc-extension-l356896',
 'score': '5',
 'notes': "Loft meublé, plafonds de 12 pi, insonorisé. Hydro+wifi+climatisation inclus. Disponible immédiatement. Près du parc Jarry et du marché Jean-Talon.",
 'photo': '',
},
{
 'date_ajout': TODAY, 'statut': 'NOUVEAU',
 'titre': "5½ rénové, électroménagers inclus - rue Fabre (Rosemont/La Petite-Patrie)",
 'quartier': 'Rosemont-La Petite-Patrie',
 'adresse': 'n/d (Rue Fabre entre St-Zotique et Bélanger, Montréal, QC H2G 2Z3)',
 'prix': '2150', 'superficie_pi2': '1100', 'chambres': '3', 'balcon': 'oui',
 'station_metro': 'Jean-Talon (estimation, non nommée dans l\'annonce)', 'ligne_metro': 'orange', 'minutes_a_pied': '9-12 (estimation incertaine)',
 'site': 'Kijiji',
 'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/magnifique-5-1-2-a-louer-avec-electromenagers/1740949940',
 'score': '9',
 'notes': "3e étage, 5 électroménagers inclus (laveuse/sécheuse, lave-vaisselle, frigo), non-fumeur, aucun animal, disponible 27 juillet 2026, bail 1 an. Distance exacte au métro non confirmée par l'annonce.",
 'photo': '',
},
{
 'date_ajout': TODAY, 'statut': 'NOUVEAU',
 'titre': "4½ lumineux avec bureau, 2 balcons - Marché St-Jacques / Parc Lafontaine",
 'quartier': 'Le Plateau-Mont-Royal (frontière Village/Centre-Sud, quartier à reconfirmer)',
 'adresse': "n/d (secteur Marché St-Jacques / Parc Lafontaine; géolocalisation Kijiji erronée indiquait Pointe-Claire)",
 'prix': '2273', 'superficie_pi2': '1233', 'chambres': '2', 'balcon': 'oui (2 balcons: rue + cour)',
 'station_metro': 'Beaudry / Sherbrooke', 'ligne_metro': 'verte', 'minutes_a_pied': '5',
 'site': 'Kijiji',
 'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/bright-top-floor-4-1-2-w-office-steps-to-parc-lafontaine/1739463983',
 'score': '9',
 'notes': "Dernier étage, bureau fermé additionnel. Disponible 1er juillet 2026, aucun animal, bail 1 an. Adresse exacte non confirmée (géolocalisation de l'annonce incohérente) - à valider avec le propriétaire; secteur à la limite Plateau/Village.",
 'photo': '',
},
{
 'date_ajout': TODAY, 'statut': 'NOUVEAU',
 'titre': "Condo/appartement meublé à louer - rue De Bullion (Plateau, près Prince-Arthur)",
 'quartier': 'Le Plateau-Mont-Royal',
 'adresse': '3558, Rue De Bullion, Montréal',
 'prix': '2400', 'superficie_pi2': 'n/d', 'chambres': '3', 'balcon': 'oui (balcon privé sur cour intérieure)',
 'station_metro': 'Saint-Laurent', 'ligne_metro': 'verte', 'minutes_a_pied': '9',
 'site': 'Centris',
 'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-le-plateau-mont-royal/12966012',
 'score': '7',
 'notes': "Meublé, chauffage/électricité/internet inclus, animaux acceptés sous conditions, non-fumeur, disponible 1er décembre 2026.",
 'photo': '',
},
{
 'date_ajout': TODAY, 'statut': 'NOUVEAU',
 'titre': "Condo/appartement à louer - rue De La Roche (Rosemont-La Petite-Patrie)",
 'quartier': 'Rosemont-La Petite-Patrie',
 'adresse': '6030, Rue De La Roche, Montréal',
 'prix': '2000', 'superficie_pi2': '1233', 'chambres': '3', 'balcon': 'n/d',
 'station_metro': 'Rosemont', 'ligne_metro': 'orange', 'minutes_a_pied': '10',
 'site': 'Centris',
 'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/18159712',
 'score': '7',
 'notes': "7 pièces au total, 1 salle de bain, disponible 1er septembre 2026.",
 'photo': '',
},
{
 'date_ajout': TODAY, 'statut': 'NOUVEAU',
 'titre': "Condo/appartement 4½ à louer - avenue Christophe-Colomb (Rosemont-La Petite-Patrie)",
 'quartier': 'Rosemont-La Petite-Patrie',
 'adresse': '5726, Avenue Christophe-Colomb, Montréal',
 'prix': '2250', 'superficie_pi2': '1000', 'chambres': '2', 'balcon': 'n/d',
 'station_metro': 'Rosemont', 'ligne_metro': 'orange', 'minutes_a_pied': '7',
 'site': 'Centris',
 'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/16659579',
 'score': '5',
 'notes': "Lumineux et bien entretenu. Disponible 5 jours après acceptation de la promesse de location.",
 'photo': '',
},
]

rows.extend(new_rows)

def sort_key(r):
    is_new = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        score = -float(r['score'])
    except (ValueError, TypeError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open(PATH, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    for r in rows:
        w.writerow(r)

print('total rows:', len(rows))
print('new rows added:', len(new_rows))
