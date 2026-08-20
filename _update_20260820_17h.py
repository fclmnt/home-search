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
    'date_ajout': '2026-08-20',
    'statut': 'NOUVEAU',
    'titre': "Cession de bail — 7½ (4 chambres + den), 1400 pi², balcons avant/arrière - Villeray, à 4 min du métro Jean-Talon",
    'quartier': 'Villeray',
    'adresse': 'n/d (secteur Villeray, Montréal, QC H2R 2R6)',
    'prix': '2000',
    'superficie_pi2': '1400',
    'chambres': '4',
    'balcon': 'oui',
    'station_metro': 'Jean-Talon',
    'ligne_metro': 'orange',
    'minutes_a_pied': '4',
    'site': 'Kijiji',
    'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/lease-assignment-beautiful-4-bedroom-upper-duplex-in-villeray/1742196370',
    'score': '9',
    'notes': "Cession de bail, 7 1/2 a l'etage superieur d'un duplex, balcons avant et arriere, laveuse-secheuse-lave-vaisselle-frigo-cuisiniere inclus, meubles disponibles, 1 chat permis, max 3 locataires, travaux de construction temporaires a l'etage inferieur (fin prevue fin octobre 2026), libre 1er octobre 2026, bail 1 an, stationnement rue disponible, a 4 min du marche Jean-Talon.",
    'photo': '',
},
{
    'date_ajout': '2026-08-20',
    'statut': 'NOUVEAU',
    'titre': "5½ ensoleillé (3 chambres), balcon - Rosemont/Petite-Patrie (secteur Saint-André/Bellechasse), à 6-8 min des métros Beaubien/Rosemont",
    'quartier': 'Rosemont / La Petite-Patrie',
    'adresse': 'n/d (secteur Saint-André/Bellechasse, Montréal, QC H2S 2K4)',
    'prix': '2200',
    'superficie_pi2': 'n/d',
    'chambres': '3',
    'balcon': 'oui',
    'station_metro': 'Beaubien',
    'ligne_metro': 'orange',
    'minutes_a_pied': '6-8',
    'site': 'Kijiji',
    'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-appartement-5-ensoleille-rosemont-petite-patrie/1742222174',
    'score': '6',
    'notes': "Reprise de bail recherchee pour un 5 1/2 ensoleille au 3e etage, balcon accessible depuis une chambre, laveuse-secheuse et electromenagers inclus, animaux acceptes, frais de services publics ~150$/mois en supplement, libre 1er octobre 2026, bail 1 an, meubles actuels a vendre en option, proche Plaza Saint-Hubert.",
    'photo': '',
},
]

rows = new_rows + rows

def sort_key(r):
    is_new = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        score = -float(r['score'])
    except (ValueError, TypeError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("done, total rows:", len(rows))
