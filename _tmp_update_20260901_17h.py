import csv

with open('annonces.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'

new_row = {
    'date_ajout': '2026-09-01',
    'statut': 'NOUVEAU',
    'titre': 'Superbe condo 4 1/2 rénové, animaux permis — à quelques pas du métro Jarry',
    'quartier': 'Villeray',
    'adresse': '8325, Avenue Christophe-Colomb, Montréal (Villeray-Saint-Michel-Parc-Extension)',
    'prix': '1950',
    'superficie_pi2': '970',
    'chambres': '2',
    'balcon': 'oui',
    'station_metro': 'Jarry',
    'ligne_metro': 'orange',
    'minutes_a_pied': '10-12 (estimé)',
    'site': 'Kijiji',
    'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/villeray-superbe-condo-4-1-2-renove-animaux-permis/1742864175',
    'score': '7',
    'notes': "Construction neuve en béton, gym et terrasse sur le toit dans l'immeuble, animaux acceptés, thermopompe murale, disponible depuis le 17 août 2026.",
    'photo': '',
}

rows.append(new_row)

def sort_key(r):
    is_new = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        score = -float(r['score'])
    except (ValueError, TypeError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    writer.writerows(rows)

print('done, total rows:', len(rows))
