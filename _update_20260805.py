import csv, json

d = json.load(open('marketplace-raw.json'))
mp_items = {it['url']: it for it in d['items']}

TODAY = '2026-08-05'

new_rows = [
    {
        'date_ajout': TODAY, 'statut': 'NOUVEAU',
        'titre': "Spacieux 4 chambres meublable, secteur Rachel/Fullum (Plateau/Sainte-Marie, limite Hochelaga), à ~6 min du métro Frontenac",
        'quartier': 'Le Plateau-Mont-Royal',
        'adresse': 'Rue Rachel Est (près Fullum), Montréal, QC H2H 1R6',
        'prix': '1900', 'superficie_pi2': 'n/d', 'chambres': '4', 'balcon': 'n/d',
        'station_metro': 'Frontenac', 'ligne_metro': 'verte', 'minutes_a_pied': '6 (estimé)',
        'site': 'Marketplace',
        'lien': 'https://www.facebook.com/marketplace/item/1646298396460474',
        'score': '5',
        'notes': "4 chambres, 1 salle de bain, 5 électros inclus (frigo/cuisinière/lave-vaisselle/laveuse-sécheuse), climatisation incluse, chats et petits chiens (<20lbs) acceptés, stationnement rue, secteur Plateau/Mile-End/Sainte-Marie à la limite de Hochelaga, arrêt de bus Rachel/Fullum à quelques pas. Lien Facebook (connexion requise).",
        'photo': mp_items['https://www.facebook.com/marketplace/item/1646298396460474']['image'],
    },
    {
        'date_ajout': TODAY, 'statut': 'NOUVEAU',
        'titre': "5 1/2 in Hochelaga (Marketplace)",
        'quartier': 'Hochelaga-Maisonneuve',
        'adresse': 'n/d (secteur Hochelaga-Maisonneuve, Montréal)',
        'prix': '2000', 'superficie_pi2': 'n/d', 'chambres': '2 (estimé)', 'balcon': 'n/d',
        'station_metro': 'n/d', 'ligne_metro': 'n/d', 'minutes_a_pied': 'n/d',
        'site': 'Marketplace',
        'lien': 'https://www.facebook.com/marketplace/item/2583777198803688',
        'score': '2',
        'notes': "Annonce titre seulement (« 5 1/2 in Hochelaga »), aucune description ni adresse disponible via le scraper. Nombre de chambres estimé à 2 selon la nomenclature standard d'un 5½, à confirmer. Lien Facebook (connexion requise) pour plus de détails.",
        'photo': mp_items['https://www.facebook.com/marketplace/item/2583777198803688']['image'],
    },
    {
        'date_ajout': TODAY, 'statut': 'NOUVEAU',
        'titre': "Logement 6 1/2 à louer dans Villeray (Marketplace)",
        'quartier': 'Villeray',
        'adresse': 'n/d (secteur Villeray, Montréal)',
        'prix': '2000', 'superficie_pi2': 'n/d', 'chambres': '3 (estimé)', 'balcon': 'n/d',
        'station_metro': 'n/d', 'ligne_metro': 'n/d', 'minutes_a_pied': 'n/d',
        'site': 'Marketplace',
        'lien': 'https://www.facebook.com/marketplace/item/1020450404083699',
        'score': '3',
        'notes': "Annonce titre seulement (« Logement a loué 6 1/2 dans villeray »), aucune description ni adresse disponible via le scraper. Nombre de chambres estimé à 3 selon la nomenclature standard d'un 6½, à confirmer. Lien Facebook (connexion requise) pour plus de détails.",
        'photo': mp_items['https://www.facebook.com/marketplace/item/1020450404083699']['image'],
    },
    {
        'date_ajout': TODAY, 'statut': 'NOUVEAU',
        'titre': "Grand 5½ (2 chambres + bureau) avec terrasse - secteur Hochelaga/Préfontaine",
        'quartier': 'Hochelaga-Maisonneuve',
        'adresse': "n/d (secteur Hochelaga/Préfontaine, Montréal, QC H1V 2X2)",
        'prix': '2195', 'superficie_pi2': 'n/d', 'chambres': '3', 'balcon': 'oui',
        'station_metro': 'Préfontaine', 'ligne_metro': 'verte', 'minutes_a_pied': '10',
        'site': 'Kijiji',
        'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-5-a-hochelaga-parking-terrasse-2-195-dispo/1739376269',
        'score': '7',
        'notes': "2 chambres fermées + bureau séparé, balcon avant + grande terrasse arrière, stationnement inclus, animaux acceptés (dont chiens), hydro inclus, meubles existants en vente possible, cession de bail jusqu'en juin 2027, 1er mois à 1995$ (promo). Adresse exacte non communiquée par l'annonce (Kijiji).",
        'photo': '',
    },
    {
        'date_ajout': TODAY, 'statut': 'NOUVEAU',
        'titre': "5½ rénové, 3 chambres, près métro Pie-IX (Rosemont)",
        'quartier': 'Rosemont-La Petite-Patrie',
        'adresse': '4419, Avenue Charlemagne, Montréal',
        'prix': '1900', 'superficie_pi2': '1200', 'chambres': '3', 'balcon': 'oui',
        'station_metro': 'Pie-IX', 'ligne_metro': 'verte', 'minutes_a_pied': '10',
        'site': 'LogisQuébec',
        'lien': 'https://www.logisquebec.com/appartement-a-louer-rosemont_la-petite-patrie-l355773',
        'score': '10',
        'notes': "Récemment rénové, non meublé, proche du Parc Maisonneuve et du Jardin botanique, disponible 1er juillet 2026.",
        'photo': '',
    },
    {
        'date_ajout': TODAY, 'statut': 'NOUVEAU',
        'titre': "Condo 2 chambres, immeuble Neuville avec piscine/gym - Rachel Est (Plateau)",
        'quartier': 'Le Plateau-Mont-Royal',
        'adresse': '1101, Rue Rachel Est, app. 906, Montréal',
        'prix': '2349', 'superficie_pi2': 'n/d', 'chambres': '2', 'balcon': 'oui',
        'station_metro': 'Mont-Royal', 'ligne_metro': 'orange', 'minutes_a_pied': '10',
        'site': 'Centris',
        'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-le-plateau-mont-royal/22654513',
        'score': '5',
        'notes': "Immeuble « Neuville » avec piscine intérieure, gym, terrasse toit BBQ, stationnement optionnel +220$/mois, animaux acceptés, 1 mois gratuit offert, disponible 1er juillet 2026.",
        'photo': '',
    },
    {
        'date_ajout': TODAY, 'statut': 'NOUVEAU',
        'titre': "Meublé 2 chambres, 927 pi² - avenue Christophe-Colomb (Plateau, proche parc Lafontaine)",
        'quartier': 'Le Plateau-Mont-Royal',
        'adresse': '4267, Avenue Christophe-Colomb, Montréal',
        'prix': '2200', 'superficie_pi2': '927', 'chambres': '2', 'balcon': 'n/d',
        'station_metro': 'Mont-Royal', 'ligne_metro': 'orange', 'minutes_a_pied': '7',
        'site': 'Centris',
        'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-le-plateau-mont-royal/9876964',
        'score': '5',
        'notes': "Meublé, Walk Score 98, proche parc Lafontaine et rue Mont-Royal, disponible 7 jours après acceptation.",
        'photo': '',
    },
    {
        'date_ajout': TODAY, 'statut': 'NOUVEAU',
        'titre': "Meublé 2 chambres avec balcons avant/arrière - rue Messier (Plateau, coin Mont-Royal/parc Baldwin)",
        'quartier': 'Le Plateau-Mont-Royal',
        'adresse': '4450, Rue Messier, Montréal',
        'prix': '1980', 'superficie_pi2': 'n/d', 'chambres': '2', 'balcon': 'oui',
        'station_metro': 'Mont-Royal', 'ligne_metro': 'orange', 'minutes_a_pied': '12',
        'site': 'Centris',
        'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-le-plateau-mont-royal/15249448',
        'score': '5',
        'notes': "Meublé (literie, serviettes, vaisselle incluses), balcons avant et arrière, chauffage/hydro non inclus, animaux non acceptés, disponible 2 jours après acceptation.",
        'photo': '',
    },
    {
        'date_ajout': TODAY, 'statut': 'NOUVEAU',
        'titre': "Grand 5½ rénové (3 chambres dont sous-sol), 1200 pi², cour clôturée - rue Villeray, à 5 min du métro Saint-Michel",
        'quartier': 'Villeray',
        'adresse': '3007, Rue Villeray, Montréal',
        'prix': '1990', 'superficie_pi2': '1200', 'chambres': '3', 'balcon': 'oui',
        'station_metro': 'Saint-Michel', 'ligne_metro': 'bleue', 'minutes_a_pied': '5',
        'site': 'Centris',
        'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/13104723',
        'score': '9',
        'notes': "Rez-de-chaussée rénové avec sous-sol aménagé (1 des 3 chambres au sous-sol), grande cour arrière clôturée, porte-patio et balcon neufs, climatisation, aussi cross-annoncé sur Facebook Marketplace, disponible 1er juillet 2026.",
        'photo': '',
    },
    {
        'date_ajout': TODAY, 'statut': 'NOUVEAU',
        'titre': "2 chambres, planchers de chêne, 900 pi² - avenue d'Outremont (Villeray/Parc-Extension), près métro Acadie",
        'quartier': 'Villeray',
        'adresse': "7597, Avenue d'Outremont, Montréal",
        'prix': '2350', 'superficie_pi2': '900', 'chambres': '2', 'balcon': 'n/d',
        'station_metro': 'Acadie', 'ligne_metro': 'bleue', 'minutes_a_pied': '4',
        'site': 'Centris',
        'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/23405105',
        'score': '5',
        'notes': "Planchers de chêne à larges lattes, climatisation murale, Walk Score 97, proche Petite-Italie/parc Jarry/Marché Jean-Talon, disponible 5 jours après acceptation ; la station la plus proche est Acadie plutôt que Jarry/Jean-Talon/De Castelnau.",
        'photo': '',
    },
    {
        'date_ajout': TODAY, 'statut': 'NOUVEAU',
        'titre': "5½ neuf (3 chambres), 1091 pi² - avenue Merritt (Parc-Extension/Villeray), près métro De Castelnau",
        'quartier': 'Villeray',
        'adresse': '9411, Avenue Merritt, app. 7, Montréal',
        'prix': '1950', 'superficie_pi2': '1091', 'chambres': '3', 'balcon': 'n/d',
        'station_metro': 'De Castelnau', 'ligne_metro': 'orange', 'minutes_a_pied': '6',
        'site': 'Centris',
        'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/20930648',
        'score': '6',
        'notes': "Construction neuve (2026), animaux non acceptés, électros inclus (frigo/cuisinière/lave-vaisselle/laveuse-sécheuse), climatiseur mural, disponible 1er juillet 2026 ; 2 autres unités similaires dans le même immeuble (app. 6 à 2060$, app. 8 à 2070$).",
        'photo': '',
    },
    {
        'date_ajout': TODAY, 'statut': 'NOUVEAU',
        'titre': "Condo neuf 2 chambres, 970 pi², balcon privé - avenue Christophe-Colomb (Villeray), près métro Jarry",
        'quartier': 'Villeray',
        'adresse': '8325, Avenue Christophe-Colomb, Montréal (H2P 0C3)',
        'prix': '2050', 'superficie_pi2': '970', 'chambres': '2', 'balcon': 'oui',
        'station_metro': 'Jarry', 'ligne_metro': 'orange', 'minutes_a_pied': '10',
        'site': 'LogisQuébec',
        'lien': 'https://www.logisquebec.com/condo-a-louer-villeray_saint-michel_parc-extension-l356021',
        'score': '7',
        'notes': "Construction neuve en béton, climatiseur mural, gym et terrasse sur le toit dans l'immeuble, internet disponible en sus (45$/mois), animaux permis, disponible immédiatement ; aussi annoncé sur Kijiji et DuProprio (même immeuble qu'une 2e unité de 1054 pi² à 2305$).",
        'photo': '',
    },
]

fieldnames = ['date_ajout','statut','titre','quartier','adresse','prix','superficie_pi2',
              'chambres','balcon','station_metro','ligne_metro','minutes_a_pied','site',
              'lien','score','notes','photo']

# Read existing rows
with open('annonces.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    existing_rows = list(reader)

# Flip NOUVEAU -> vu
for row in existing_rows:
    if row['statut'] == 'NOUVEAU':
        row['statut'] = 'vu'

all_rows = existing_rows + new_rows

def score_key(row):
    try:
        s = int(row['score'])
    except (ValueError, KeyError):
        s = 0
    return s

def sort_key(row):
    is_new = 0 if row['statut'] == 'NOUVEAU' else 1
    return (is_new, -score_key(row))

all_rows.sort(key=sort_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    for row in all_rows:
        writer.writerow({k: row.get(k, '') for k in fieldnames})

print(f"Total rows written: {len(all_rows)} (added {len(new_rows)} new)")
