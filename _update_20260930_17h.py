import csv

with open('annonces.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# Passer les anciennes NOUVEAU à vu
for row in rows:
    if row['statut'] == 'NOUVEAU':
        row['statut'] = 'vu'

new_rows = [
    {
        'date_ajout': '2026-09-30',
        'statut': 'NOUVEAU',
        'titre': "5½ neuf, 3 chambres, semi-meublé - à 8 min du métro Préfontaine (Hochelaga)",
        'quartier': 'Hochelaga-Maisonneuve',
        'adresse': '3257, Rue Sainte-Catherine Est, app. 102, Montréal, QC',
        'prix': '2270',
        'superficie_pi2': '1206',
        'chambres': '3',
        'balcon': 'n/d',
        'station_metro': 'Préfontaine',
        'ligne_metro': 'verte',
        'minutes_a_pied': '8 (estimé)',
        'site': 'Centris',
        'lien': 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/18618728',
        'score': '8',
        'notes': "Annonce Centris : construction neuve (2026), 1206 pi², 3 chambres (2 au sous-sol), semi-meublé, arret d'autobus devant l'immeuble, proche commerces/restos. Walk Score 90. Disponible 5 jours apres acceptation. Balcon non precise dans l'annonce. Distance au metro Prefontaine (ligne verte) estimee a 8 min de marche.",
        'photo': '',
    },
    {
        'date_ajout': '2026-09-30',
        'statut': 'NOUVEAU',
        'titre': "Grand 5½, 3 chambres fermées, balcon, stationnement intérieur - secteur Villeray/Pie-IX",
        'quartier': 'Villeray-Saint-Michel-Parc-Extension',
        'adresse': 'Boulevard Pie-IX, Montréal, QC H2A 2G5',
        'prix': '1945',
        'superficie_pi2': '950',
        'chambres': '3',
        'balcon': 'oui',
        'station_metro': 'Jean-Talon ou Fabre (à confirmer)',
        'ligne_metro': 'bleue',
        'minutes_a_pied': '10 (estimé)',
        'site': 'Kijiji',
        'lien': 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-5-a-villeray-3-chambres-stationnement-interieur/1744183021',
        'score': '8',
        'notes': "3 chambres fermees, balcon inclus, meuble, eau incluse, stationnement interieur prive (2 places), laveuse/secheuse dans l'unite, animaux non acceptes, disponible 1er nov. 2026. Adresse precise non communiquee par l'annonceur (secteur Pie-IX/Villeray, code postal H2A 2G5) ; station de metro et distance a pied estimees a partir du secteur, a confirmer.",
        'photo': '',
    },
]

rows = new_rows + rows

def sort_key(row):
    is_new = 0 if row['statut'] == 'NOUVEAU' else 1
    try:
        score = -int(row['score'])
    except (ValueError, KeyError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("done", len(rows))
