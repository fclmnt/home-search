import csv

PATH = 'annonces.csv'
FIELDS = ['date_ajout','statut','titre','quartier','adresse','prix','superficie_pi2','chambres',
          'balcon','station_metro','ligne_metro','minutes_a_pied','site','lien','score','notes','photo']

with open(PATH, newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'

new_rows = [
{
 'date_ajout': '2026-08-31', 'statut': 'NOUVEAU',
 'titre': 'Grand 6½ rénové à 2 pas du métro Pie-IX (ligne verte)',
 'quartier': 'Hochelaga-Maisonneuve',
 'adresse': 'n/d (Montréal, QC H1W 3S5)',
 'prix': '1995', 'superficie_pi2': '900', 'chambres': '3', 'balcon': 'oui',
 'station_metro': 'Pie-IX', 'ligne_metro': 'verte', 'minutes_a_pied': '5',
 'site': 'Kijiji',
 'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-6-renove-a-2-pas-du-metro-pie-ix-ligne-verte/1742650298',
 'score': '9',
 'notes': "3e et dernier étage d'un triplex, thermopompe neuve (chauffage et climatisation inclus), eau incluse, 1 chat stérilisé accepté sous conditions, non-fumeur, aucun stationnement, disponible 1er septembre 2026, à 10 min de la Promenade Ontario.",
 'photo': '',
},
{
 'date_ajout': '2026-08-31', 'statut': 'NOUVEAU',
 'titre': 'Cession de bail — Grand 4½ meublé avec terrasse privée et jardin, près métro Préfontaine/Frontenac',
 'quartier': 'Centre-Sud (limitrophe Hochelaga)',
 'adresse': 'n/d (Montréal, QC H2K 2S2)',
 'prix': '2000', 'superficie_pi2': '900', 'chambres': '2', 'balcon': 'oui',
 'station_metro': 'Préfontaine', 'ligne_metro': 'verte', 'minutes_a_pied': '7',
 'site': 'Kijiji',
 'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/cession-de-bail-grand-4-meuble-avec-terrasse-privee-jardin/1742732549',
 'score': '8',
 'notes': "Cession de bail, meublé, buanderie interne, climatisation, eau incluse ; animaux limités ; bail mensuel possible ; disponible 1er octobre 2026 ; quartier Centre-Sud/Ville-Marie (hors des 4 quartiers prioritaires mais limitrophe d'Hochelaga, à 7-8 min des stations Préfontaine et Frontenac).",
 'photo': '',
},
{
 'date_ajout': '2026-08-31', 'statut': 'NOUVEAU',
 'titre': 'Condo 2 chambres, 1050 pi² — Avenue de l’Esplanade (Plateau-Mont-Royal)',
 'quartier': 'Le Plateau-Mont-Royal',
 'adresse': '5818, Avenue de l’Esplanade, Montréal, QC',
 'prix': '2100', 'superficie_pi2': '1050', 'chambres': '2', 'balcon': 'n/d',
 'station_metro': 'Rosemont ou Laurier', 'ligne_metro': 'orange', 'minutes_a_pied': '12',
 'site': 'Centris',
 'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-le-plateau-mont-royal/26600322',
 'score': '5',
 'notes': "Animaux non acceptés ; disponible 1er juillet 2026 ; salon double pouvant servir de 3e chambre ; laveuse/sécheuse intégrées ; balcon non précisé dans l'annonce ; à la limite haute de la distance au métro (~12 min).",
 'photo': '',
},
{
 'date_ajout': '2026-08-31', 'statut': 'NOUVEAU',
 'titre': '4½ entièrement rénové avec terrasse — rue Fénelon (Villeray/Saint-Michel)',
 'quartier': 'Villeray',
 'adresse': '3611, Rue Fénelon, Montréal, QC',
 'prix': '1900', 'superficie_pi2': '1350', 'chambres': '2', 'balcon': 'oui',
 'station_metro': 'Saint-Michel', 'ligne_metro': 'bleue', 'minutes_a_pied': '9',
 'site': 'DuProprio',
 'lien': 'https://duproprio.com/fr/location/montreal/villeray-st-michel-parc-extension/4-1-2-a-louer/hab-3611-rue-fenelon-1140156',
 'score': '8',
 'notes': "Disponible immédiatement ; cour privée ; électroménagers neufs ; climatisation ; secteur à la limite Villeray/Saint-Michel.",
 'photo': '',
},
{
 'date_ajout': '2026-08-31', 'statut': 'NOUVEAU',
 'titre': 'GRAND 5½ meublé et rénové, 3 chambres, 2 balcons — 13e Avenue (Villeray/Saint-Michel)',
 'quartier': 'Villeray',
 'adresse': 'n/d (13e Avenue, secteur Villeray/Saint-Michel, Montréal)',
 'prix': '2250', 'superficie_pi2': 'n/d', 'chambres': '3', 'balcon': 'oui',
 'station_metro': 'Saint-Michel', 'ligne_metro': 'bleue', 'minutes_a_pied': '5',
 'site': 'logisquebec',
 'lien': 'https://www.logisquebec.com/appartement-a-louer-villeray_saint-michel_parc-extension-l359398',
 'score': '6',
 'notes': "Meublé ; bail jusqu'au 30 juin 2027 ; animaux non acceptés ; attention : l'annonce mentionne qu'une chambre de ce logement est aussi louée séparément à 750$/mois, ce qui suggère un possible arrangement de type colocation à clarifier avant de contacter sérieusement.",
 'photo': '',
},
{
 'date_ajout': '2026-08-31', 'statut': 'NOUVEAU',
 'titre': '3 chambres neuf, balcon privé — 304 Rue Villeray (Villeray)',
 'quartier': 'Villeray',
 'adresse': '304, Rue Villeray, app. 304, Montréal, QC H2R 1G7',
 'prix': '2095', 'superficie_pi2': '1000', 'chambres': '3', 'balcon': 'oui',
 'station_metro': 'De Castelnau', 'ligne_metro': 'orange', 'minutes_a_pied': '9',
 'site': 'Zumper',
 'lien': 'https://www.zumper.com/address/304-rue-villeray-montreal-qc-h2r-1g7-can',
 'score': '8',
 'notes': "Jamais habité (neuf) ; climatisation murale ; animaux acceptés (chats et chiens) ; assurance responsabilité 2M$ exigée ; bail 1 an ; non-fumeur.",
 'photo': '',
},
]

rows.extend(new_rows)

def sort_key(r):
    is_new = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        score = -int(r['score'])
    except (ValueError, TypeError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open(PATH, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    w.writerows(rows)

print('total rows now:', len(rows))
print('new rows added:', len(new_rows))
