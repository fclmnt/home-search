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
    'date_ajout': '2026-08-21',
    'statut': 'NOUVEAU',
    'titre': "4½ - 2 chambres, 2 salles de bain, 1400 pi², près métro Monk (Marketplace)",
    'quartier': 'Ville-Émard (Sud-Ouest)',
    'adresse': '5787 Boulevard Monk, Montréal, QC H4E 3H2',
    'prix': '2195',
    'superficie_pi2': '1400',
    'chambres': '2',
    'balcon': 'n/d',
    'station_metro': 'Monk',
    'ligne_metro': 'verte',
    'minutes_a_pied': '10-12',
    'site': 'Marketplace',
    'lien': 'https://www.facebook.com/marketplace/item/1747296433138639',
    'score': '7',
    'notes': "Cession de bail jusqu'en juin 2027 (option de renouvellement), disponible 1er septembre 2026, cuisine/salon a aire ouverte, electromenagers inclus (four, frigo, lave-vaisselle, laveuse-secheuse), stationnement dans la rue. Quartier Ville-Emard, a l'oppose de Hochelaga sur la ligne verte (extremite sud-ouest) - a evaluer selon la tolerance au trajet. Lien Facebook (connexion requise).",
    'photo': 'https://scontent-yyz1-1.xx.fbcdn.net/v/t39.84726-6/763119959_1360376115596175_1743883061212377860_n.jpg?stp=c134.0.540.540a_dst-jpg_p180x540_tt6&_nc_cat=108&ccb=1-7&_nc_sid=92e707&_nc_ohc=T7GmmILLUT4Q7kNvwFZHa-_&_nc_oc=Ado8LpOjL2dU_QC1EwTiwQR2yA-wDv5yvEJwEu21lVdHOIY8h8lXWVBCwULh2LT3vcI&_nc_zt=14&_nc_ht=scontent-yyz1-1.xx&_nc_gid=sXY3Jdj1CztJ9pZCttdteg&_nc_ss=7f2a8&oh=00_AQHxAILBHiYdpR-XcXz2gH-sLhZD8F9am85nrErRNe09ZA&oe=6A8E0BD4',
},
{
    'date_ajout': '2026-08-21',
    'statut': 'NOUVEAU',
    'titre': "Appartement 2 chambres + bureau, quartier central Plateau, à ~11 min du métro Sherbrooke (Marketplace)",
    'quartier': 'Le Plateau-Mont-Royal',
    'adresse': '3984 Rue de Bullion, Montréal, QC H2W 2E4',
    'prix': '2300',
    'superficie_pi2': 'n/d',
    'chambres': '2',
    'balcon': 'n/d',
    'station_metro': 'Sherbrooke',
    'ligne_metro': 'orange',
    'minutes_a_pied': '11',
    'site': 'Marketplace',
    'lien': 'https://www.facebook.com/marketplace/item/1528694045314689',
    'score': '3',
    'notes': "Deux chambres fermees + un espace de bureau, electromenagers inclus, bail 1 an, disponible maintenant, quartier central (Walk Score 100, Bike Score 98). Superficie non indiquee. Lien Facebook (connexion requise).",
    'photo': 'https://scontent-yyz1-1.xx.fbcdn.net/v/t39.30808-6/722994642_10164255701674834_4384640404152492239_n.jpg?stp=c342.0.1365.1365a_dst-jpg_tt6&cstp=mx1365x1365&ctp=s565x565&_nc_cat=100&ccb=1-7&_nc_sid=454cf4&_nc_ohc=P20jq1k6qjIQ7kNvwF35WB_&_nc_oc=AdrWOhKe-TO43O_pi7-zm4f94i1vfAPIWDFFxE3h49ZzbSfBqp_EeJowVqfsNEyEzmY&_nc_zt=23&_nc_ht=scontent-yyz1-1.xx&_nc_gid=-RRMTc1fIutY57-pjw9YmQ&_nc_ss=7f2a8&oh=00_AQHvo5JUjbFeFE0mNam3RiJtgV0tjwf8rAM1aebC8RWpDQ&oe=6A8E14C9',
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
