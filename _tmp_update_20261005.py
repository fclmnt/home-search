import csv

with open('annonces.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# flip old NOUVEAU -> vu
for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'

new_rows = [
{
 'date_ajout': '2026-10-05',
 'statut': 'NOUVEAU',
 'titre': '5½ (3 chambres fermées), proche métro Jarry - secteur rue Saint-Denis, Villeray',
 'quartier': 'Villeray',
 'adresse': '8321, Rue Saint-Denis, Montréal, QC',
 'prix': '1975',
 'superficie_pi2': 'n/d',
 'chambres': '3',
 'balcon': 'n/d',
 'station_metro': 'Jarry',
 'ligne_metro': 'orange',
 'minutes_a_pied': '5 (estimé)',
 'site': 'Centris',
 'lien': 'https://www.centris.ca/en/condos-apartments~for-rent~montreal-villeray-saint-michel-parc-extension/28716271',
 'score': '4',
 'notes': "Immeuble de 1955, planchers de bois franc, cuisine renovee, a distance de marche d'un cegep, garderie, parc, piste cyclable et ecoles. Disponible 5 jours apres acceptation de la promesse de location. Balcon et superficie non precises par l'annonce. Distance au metro Jarry estimee a partir de l'adresse (non confirmee par l'annonce).",
 'photo': '',
},
{
 'date_ajout': '2026-10-05',
 'statut': 'NOUVEAU',
 'titre': '4½ rénové (2 chambres, sous-sol), 1080 pi² - rue Marie-Anne Est, Plateau-Mont-Royal',
 'quartier': 'Le Plateau-Mont-Royal',
 'adresse': '2484, Rue Marie-Anne Est, app. 1, Montréal, QC',
 'prix': '1995',
 'superficie_pi2': '1080',
 'chambres': '2',
 'balcon': 'n/d',
 'station_metro': 'Mont-Royal',
 'ligne_metro': 'orange',
 'minutes_a_pied': '9 (estimé)',
 'site': 'Centris',
 'lien': 'https://www.centris.ca/en/condos-apartments~for-rent~montreal-le-plateau-mont-royal/27584406',
 'score': '5',
 'notes': "Logement au sous-sol, climatisation centrale, animaux non acceptes, disponible 5 jours apres acceptation de la promesse de location, Walk Score 97, a distance de marche des metros Mont-Royal et Frontenac (temps estime, non precise par l'annonce). Note : une autre annonce (LogisQuebec, l353552) existe a la meme adresse civique pour un autre logement (4half condo 2019, 2075$) - probablement une unite differente du meme immeuble.",
 'photo': '',
},
]

rows.extend(new_rows)

def score_key(r):
    is_new = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        s = -int(r['score'])
    except Exception:
        s = 0
    return (is_new, s)

rows.sort(key=score_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print('total rows:', len(rows))
print('NOUVEAU count:', sum(1 for r in rows if r['statut'] == 'NOUVEAU'))
