import csv

FIELDS = ["date_ajout","statut","titre","quartier","adresse","prix","superficie_pi2",
          "chambres","balcon","station_metro","ligne_metro","minutes_a_pied","site",
          "lien","score","notes","photo"]

rows = []
with open('annonces.csv', newline='', encoding='utf-8') as f:
    r = csv.DictReader(f)
    for row in r:
        if row['statut'] == 'NOUVEAU':
            row['statut'] = 'vu'
        rows.append(row)

new_row = {
    "date_ajout": "2026-08-14",
    "statut": "NOUVEAU",
    "titre": "6 1/2 (2 chambres fermées + bureau) avec cour ensoleillée - rue Chapleau (Centre-Sud), 7 min du métro Frontenac",
    "quartier": "Centre-Sud",
    "adresse": "2284, Rue Chapleau, Montréal, QC H2K 3H3",
    "prix": "1900",
    "superficie_pi2": "1000",
    "chambres": "2",
    "balcon": "n/d",
    "station_metro": "Frontenac",
    "ligne_metro": "verte",
    "minutes_a_pied": "7 (estimé)",
    "site": "Marketplace",
    "lien": "https://www.facebook.com/marketplace/item/1769236844204807",
    "score": "6",
    "notes": "RDC avec cour ensoleillee, 2 chambres fermees + bureau, pas d'electromenagers inclus, pas de chauffage inclus, animaux acceptes, dispo 1er sept. (ou 1er oct.), visite sur rendez-vous dimanche 16 aout. Lien Facebook (connexion requise).",
    "photo": "https://scontent-yyz1-1.xx.fbcdn.net/v/t39.84726-6/774043819_1023625023824951_1565954371442702056_n.jpg?stp=c0.87.526.526a_dst-jpg_p526x395_tt6&_nc_cat=103&ccb=1-7&_nc_sid=92e707&_nc_ohc=GKHYcC-wl3QQ7kNvwEqJEIC&_nc_oc=Adrw0WL1RwcpStBH7xEpIvQH4WoOc_RtGT7YNXvvP6HrKHDOWsI54aUSkblSPkEBMGk&_nc_zt=14&_nc_ht=scontent-yyz1-1.xx&_nc_gid=bdGocsibirzlTiJQ0D1--A&_nc_ss=7f2a8&oh=00_AQFtGikvCLa1__cMY8hGMC0K8DmfvJYbuaEFNeLY_t28ag&oe=6A84E3D9",
}
rows.append(new_row)

def sort_key(row):
    is_new = 0 if row['statut'] == 'NOUVEAU' else 1
    try:
        score = -int(row['score'])
    except (ValueError, KeyError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    for row in rows:
        w.writerow(row)

print("total rows:", len(rows))
print("NOUVEAU count:", sum(1 for r in rows if r['statut'] == 'NOUVEAU'))
