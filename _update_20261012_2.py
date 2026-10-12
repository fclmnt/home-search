import csv

path = "annonces.csv"
with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

changed = 0
for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'
        changed += 1
print("flipped", changed, "rows to vu")

new_row = {
    'date_ajout': '2026-10-12',
    'statut': 'NOUVEAU',
    'titre': "5½ rénové, 3 chambres fermées, 1250 pi², balcon - rue Saint-Louis (Plateau-Mont-Royal), face au parc Jeanne-Mance",
    'quartier': 'Le Plateau-Mont-Royal',
    'adresse': 'Rue Saint-Louis, Montréal, QC H2W 2N4',
    'prix': '2195',
    'superficie_pi2': '1250',
    'chambres': '3',
    'balcon': 'oui',
    'station_metro': 'Mont-Royal',
    'ligne_metro': 'orange',
    'minutes_a_pied': '10-12 (estimé, à vérifier)',
    'site': 'Kijiji',
    'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/5-1-2-plateau-emplacement-parfait/1736891738',
    'score': '9',
    'notes': "Chauffé et eau chaude inclus, laveuse-sécheuse et lave-vaisselle inclus, animaux acceptés, face au parc Jeanne-Mance, libre 1er oct. 2026. ATTENTION : loyer promotionnel la 1re année (2195$), remonte à 2645$/mois au renouvellement - à vérifier avant de visiter.",
    'photo': '',
}

rows.append(new_row)

def sort_key(r):
    is_new = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        score = -int(r['score'])
    except (ValueError, TypeError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    writer.writerows(rows)

print("total rows now", len(rows))
