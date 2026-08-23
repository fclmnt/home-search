import csv

PATH = "annonces.csv"
FIELDS = ["date_ajout","statut","titre","quartier","adresse","prix","superficie_pi2","chambres",
          "balcon","station_metro","ligne_metro","minutes_a_pied","site","lien","score","notes","photo"]

with open(PATH, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rows = list(r)

for row in rows:
    if row["statut"] == "NOUVEAU":
        row["statut"] = "vu"

new_rows = [
{
    "date_ajout": "2026-08-23", "statut": "NOUVEAU",
    "titre": "Grand 5 1/2 meublé, 3 chambres, 2 étages - rue Joliette (Hochelaga), près du métro Joliette",
    "quartier": "Hochelaga-Maisonneuve",
    "adresse": "2160, Rue Joliette, app. 2160, Montréal",
    "prix": "1950", "superficie_pi2": "1200", "chambres": "3", "balcon": "oui",
    "station_metro": "Joliette", "ligne_metro": "verte", "minutes_a_pied": "3 (estimé)",
    "site": "Kijiji", "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-5-1-a-louer-a-hochelaga/1742106501",
    "score": "10",
    "notes": "Meublé, logement sur 2 étages (2e et 3e), électroménagers inclus (laveuse/sécheuse), 1 stationnement inclus, chats acceptés, non-fumeur, disponible 1er sept. 2026",
    "photo": "",
},
{
    "date_ajout": "2026-08-23", "statut": "NOUVEAU",
    "titre": "4½ rénové, 2 chambres, à 2 pas du métro D'Iberville - Villeray",
    "quartier": "Villeray",
    "adresse": "n/d (Villeray, Montréal, QC H1X)",
    "prix": "1915", "superficie_pi2": "950", "chambres": "2", "balcon": "oui",
    "station_metro": "D'Iberville", "ligne_metro": "bleue", "minutes_a_pied": "2 (estimé)",
    "site": "Kijiji", "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/4-haut-de-gamme-renove-a-2-pas-du-metro-iberville/1742390521",
    "score": "7",
    "notes": "Rénové au complet printemps 2024, grand balcon arrière couvert, plancher chauffant salle de bain, comptoirs quartz, non meublé, animaux non acceptés, disponible fin août 2026, Walk Score 94",
    "photo": "",
},
{
    "date_ajout": "2026-08-23", "statut": "NOUVEAU",
    "titre": "5 1/2 entièrement rénové, 3 chambres, à 1 min du métro Rosemont",
    "quartier": "Rosemont-La Petite-Patrie",
    "adresse": "n/d (secteur métro Rosemont, Montréal, QC H2S 2P4)",
    "prix": "2100", "superficie_pi2": "950", "chambres": "3", "balcon": "oui",
    "station_metro": "Rosemont", "ligne_metro": "orange", "minutes_a_pied": "1",
    "site": "Kijiji", "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/metro-rosemont-superbe-5-1-2-entierement-renove/1741822232",
    "score": "8",
    "notes": "Entièrement rénové (comptoirs quartz, granite, plancher bois franc), laveuse-sécheuse empilable, eau incluse, chauffage électrique à la charge du locataire, animaux acceptés, disponible 1er sept. 2026, idéal colocation",
    "photo": "",
},
{
    "date_ajout": "2026-08-23", "statut": "NOUVEAU",
    "titre": "4½ rénové avec immense terrasse privée - rue Saint-Denis (Plateau), à deux pas du métro Laurier (Marketplace)",
    "quartier": "Le Plateau-Mont-Royal",
    "adresse": "5390, Rue Saint-Denis, Montréal",
    "prix": "1925", "superficie_pi2": "n/d", "chambres": "2", "balcon": "oui",
    "station_metro": "Laurier", "ligne_metro": "orange", "minutes_a_pied": "3 (estimé)",
    "site": "Marketplace", "lien": "https://www.facebook.com/marketplace/item/894901667031237",
    "score": "5",
    "notes": "2 chambres fermées, très grande terrasse privée, thermopompe (climatisation/chauffage), électroménagers inclus, stationnement privé possible, disponible immédiatement. Lien Facebook (connexion requise)",
    "photo": "https://scontent-yyz1-1.xx.fbcdn.net/v/t39.30808-6/762129139_10166466656364009_5134374092481479983_n.jpg?stp=c0.169.1536.1536a_dst-jpg_tt6&cstp=mx1536x1536&ctp=s565x565&_nc_cat=111&ccb=1-7&_nc_sid=454cf4&_nc_ohc=3qZUQHAia7oQ7kNvwF-DHR6&_nc_oc=AdojvE3wzung9u7r7US2dLWXA7w6P2lMltspUF2yAJR_BYEVl362GJskK-cwoaXcDW8&_nc_zt=23&_nc_ht=scontent-yyz1-1.xx&_nc_gid=hnqIHFjbxMu6V7YVFERN2g&_nc_ss=7f2a8&oh=00_AQGNED6jmZ6d1aH_1IxGuLM6IOmU3POKDQn9bBZi2nke0Q&oe=6A9125C2",
},
{
    "date_ajout": "2026-08-23", "statut": "NOUVEAU",
    "titre": "2 chambres rénové, près de la rue Mont-Royal et du métro Mont-Royal (Marketplace)",
    "quartier": "Le Plateau-Mont-Royal",
    "adresse": "4408, Avenue de l'Hôtel-de-Ville, Montréal",
    "prix": "2100", "superficie_pi2": "n/d", "chambres": "2", "balcon": "n/d",
    "station_metro": "Mont-Royal", "ligne_metro": "orange", "minutes_a_pied": "5 (estimé)",
    "site": "Marketplace", "lien": "https://www.facebook.com/marketplace/item/3643447005808131",
    "score": "3",
    "notes": "Nouvellement rénové, meublé (table, chaises, canapé, lits), climatisation incluse, isolation phonique/thermique complète, plafonds hauts, animaux acceptés. Lien Facebook (connexion requise)",
    "photo": "https://scontent-yyz1-1.xx.fbcdn.net/v/t39.30808-6/769082955_1572138077922196_3928924517892675151_n.jpg?stp=c0.169.1536.1536a_dst-jpg_tt6&cstp=mx1536x1536&ctp=s565x565&_nc_cat=100&ccb=1-7&_nc_sid=454cf4&_nc_ohc=5lbjrhSykR4Q7kNvwGXZEsS&_nc_oc=AdosPHcT82UDB5JXJB3hFRrzA2ywy8Iz4eDC9_v14IG5fPngcGQrop8r6fkrAZcfxOg&_nc_zt=23&_nc_ht=scontent-yyz1-1.xx&_nc_gid=hnqIHFjbxMu6V7YVFERN2g&_nc_ss=7f2a8&oh=00_AQFUCFiOoITnnQEKag8_p25qfElq9MW43hMXPo8TnhpJ_g&oe=6A91378D",
},
{
    "date_ajout": "2026-08-23", "statut": "NOUVEAU",
    "titre": "5 1/2 Apartment à côté du métro Laurier (Marketplace)",
    "quartier": "Le Plateau-Mont-Royal",
    "adresse": "n/d (secteur métro Laurier, Montréal)",
    "prix": "2286", "superficie_pi2": "n/d", "chambres": "3 (estimé)", "balcon": "n/d",
    "station_metro": "Laurier (estimé du titre)", "ligne_metro": "orange", "minutes_a_pied": "n/d",
    "site": "Marketplace", "lien": "https://www.facebook.com/marketplace/item/1494146445585365",
    "score": "4",
    "notes": "Annonce titre seulement (« 5 1/2 Apartment à côté du métro laurier »), aucune description disponible via le scraper ; quartier et proximité métro estimés à partir du titre, à confirmer. Lien Facebook (connexion requise)",
    "photo": "https://scontent-yyz1-1.xx.fbcdn.net/v/t39.84726-6/699126897_1973485496863353_2557441085218132183_n.jpg?stp=c0.87.526.526a_dst-jpg_p526x395_tt6&_nc_cat=105&ccb=1-7&_nc_sid=92e707&_nc_ohc=1TfRKggdwDcQ7kNvwEurKS5&_nc_oc=AdoR-cEqyxjiGQ0UmeNWANwJPUjdZDGYcYoZbroFxLyW1VqV4CZrGQZ3Dx9LatXKOdo&_nc_zt=14&_nc_ht=scontent-yyz1-1.xx&_nc_gid=V_1P3sgeyFFynjrs9YnECA&_nc_ss=7f2a8&oh=00_AQFKi9JtscuC3zLGzRNAS8-wnmDcB7WEfSrc3K0HAzOrbA&oe=6A911748",
},
]

rows.extend(new_rows)

def sort_key(row):
    is_new = 0 if row["statut"] == "NOUVEAU" else 1
    try:
        score = -int(row["score"])
    except (ValueError, TypeError):
        score = 0
    return (is_new, score)

rows.sort(key=sort_key)

with open(PATH, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    w.writerows(rows)

print("total rows:", len(rows))
print("new rows added:", len(new_rows))
