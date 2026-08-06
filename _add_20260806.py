import csv

FIELDS = ["date_ajout","statut","titre","quartier","adresse","prix","superficie_pi2",
          "chambres","balcon","station_metro","ligne_metro","minutes_a_pied","site",
          "lien","score","notes","photo"]

with open('annonces.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

for row in rows:
    if row['statut'] == 'NOUVEAU':
        row['statut'] = 'vu'

new_rows = [
    {
        "date_ajout": "2026-08-06",
        "statut": "NOUVEAU",
        "titre": "5½ (3 chambres), 1100 pi², balcon privé dans la chambre principale - rue Chapleau (Centre-Sud, près métro Frontenac)",
        "quartier": "Ville-Marie (Centre-Sud)",
        "adresse": "Rue Chapleau, Montréal, QC",
        "prix": "2365",
        "superficie_pi2": "1100",
        "chambres": "3",
        "balcon": "oui",
        "station_metro": "Frontenac",
        "ligne_metro": "verte",
        "minutes_a_pied": "8",
        "site": "Kijiji",
        "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/3-bedroom-apartment-5-1-2-september-1st/1740840292",
        "score": "10",
        "notes": "Cession de bail 12 mois, unité de coin au dernier étage, chambre principale communique avec 2e chambre par porte, laveuse-sécheuse, climatisation, électroménagers inclus, secteur calme et verdoyant, aucun animal, disponible 1er septembre 2026.",
        "photo": "",
    },
    {
        "date_ajout": "2026-08-06",
        "statut": "NOUVEAU",
        "titre": "Grand 5½ (3 chambres), 1400 pi², 2 balcons (avant/arrière) - secteur Parc-Jarry (Villeray), près métro Jean-Talon",
        "quartier": "Villeray",
        "adresse": "n/d (secteur Parc-Jarry, Montréal, QC H2R 2E9)",
        "prix": "1975",
        "superficie_pi2": "1400",
        "chambres": "3",
        "balcon": "oui",
        "station_metro": "Jean-Talon",
        "ligne_metro": "orange",
        "minutes_a_pied": "n/d (courte marche selon l'annonce)",
        "site": "Zumper",
        "lien": "https://www.zumper.com/apartments-for-rent/9730117p/3-bedroom-parc-jarry-montreal-qc",
        "score": "9",
        "notes": "Chats acceptés (chiens refusés), proche marché Jean-Talon et Petite Italie ; la date de disponibilité affichée par la fiche (avril/mai) semble périmée, à valider auprès du proprio avant de contacter.",
        "photo": "",
    },
    {
        "date_ajout": "2026-08-06",
        "statut": "NOUVEAU",
        "titre": "4½ rénové (2 chambres), 1350 pi² - rue Fénelon (Villeray/Saint-Michel), à quelques pas du métro Saint-Michel",
        "quartier": "Villeray-Saint-Michel-Parc-Extension",
        "adresse": "3601, Rue Fénelon, Montréal",
        "prix": "1900",
        "superficie_pi2": "1350",
        "chambres": "2",
        "balcon": "n/d",
        "station_metro": "Saint-Michel",
        "ligne_metro": "bleue",
        "minutes_a_pied": "3 (estimé)",
        "site": "Centris",
        "lien": "https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/17069497",
        "score": "6",
        "notes": "Semi-meublé, 3 électroménagers neufs, plafonds de 11 pieds, Walk Score 95, accès rapide à l'autoroute 40, disponible 10 jours après acceptation de la promesse de location ; balcon non mentionné dans l'annonce.",
        "photo": "",
    },
]

rows.extend(new_rows)

def sort_key(row):
    is_new = 0 if row['statut'] == 'NOUVEAU' else 1
    try:
        score = -int(row['score'])
    except (ValueError, TypeError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(rows)

print('total rows now:', len(rows))
print('NOUVEAU count:', sum(1 for r in rows if r['statut'] == 'NOUVEAU'))
