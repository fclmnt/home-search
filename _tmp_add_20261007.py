import csv

rows_to_add = [
{
 "date_ajout": "2026-10-07",
 "statut": "NOUVEAU",
 "titre": "3 chambres fermées meublé, 1200 pi², balcon - HOMA, à 1 min du métro Pie-IX",
 "quartier": "Hochelaga-Maisonneuve",
 "adresse": "n/d (Montréal, QC H1V 2E7)",
 "prix": "2100",
 "superficie_pi2": "1200",
 "chambres": "3",
 "balcon": "oui",
 "station_metro": "Pie-IX",
 "ligne_metro": "verte",
 "minutes_a_pied": "1",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/3-bedroom-apartment-fully-furnished-in-homa/1744496516",
 "score": "10",
 "notes": "Meuble avec bureau dedie, toutes charges incluses (chauffage, hydro, eau), climatisation, stationnement prive inclus, laveuse-secheuse a l'unite, animaux acceptes, bail mensuel possible, disponible immediatement.",
 "photo": "",
},
{
 "date_ajout": "2026-10-07",
 "statut": "NOUVEAU",
 "titre": "3 chambres renove, 1100 pi², rue Cuvillier (Hochelaga), a 4 min du metro Joliette",
 "quartier": "Hochelaga-Maisonneuve",
 "adresse": "Rue Cuvillier, Montreal, QC H1W 3A8",
 "prix": "2200",
 "superficie_pi2": "1100",
 "chambres": "3",
 "balcon": "n/d",
 "station_metro": "Joliette",
 "ligne_metro": "verte",
 "minutes_a_pied": "4",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/newly-renovated-3-bedroom-apartment-for-rent/1744478830",
 "score": "8",
 "notes": "Electromenagers neufs inclus, stationnement prive, internet haute vitesse inclus, animaux a discuter, disponible 1er dec. 2026, bail 1 an. Rue Cuvillier deja representee par d'autres annonces similaires dans le meme secteur ; numero civique non precise par l'annonceur.",
 "photo": "",
},
{
 "date_ajout": "2026-10-07",
 "statut": "NOUVEAU",
 "titre": "4½ renove (2 chambres), 900 pi², balcons avant/arriere - rue de Bordeaux (Plateau), proche metro Mont-Royal",
 "quartier": "Le Plateau-Mont-Royal",
 "adresse": "Rue de Bordeaux, Montreal, QC (secteur Mont-Royal / de Bordeaux)",
 "prix": "2200",
 "superficie_pi2": "900",
 "chambres": "2",
 "balcon": "oui (avant et arriere)",
 "station_metro": "Mont-Royal",
 "ligne_metro": "verte",
 "minutes_a_pied": "10 (estime)",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/4-5-plateau-transfer-de-bail-1er-novembre-1er-decembre/1740921142",
 "score": "8",
 "notes": "Transfert de bail jusqu'au 31 juillet 2027 (renouvelable), entierement renove, semi-meuble (electromenagers inclus), climatisation, stationnement rue, disponible 1er nov. ou 1er dec. 2026. Electricite/internet non inclus. Distance au metro estimee (non precisee dans l'annonce).",
 "photo": "",
},
{
 "date_ajout": "2026-10-07",
 "statut": "NOUVEAU",
 "titre": "4½ renove (2 chambres), 950 pi², 2 balcons - secteur De Lorimier / Parc La Fontaine (Plateau), proche metro Sherbrooke",
 "quartier": "Le Plateau-Mont-Royal",
 "adresse": "n/d (Montreal, QC H2K 4G3, secteur De Lorimier / Parc La Fontaine)",
 "prix": "2230",
 "superficie_pi2": "950",
 "chambres": "2",
 "balcon": "oui (2 balcons)",
 "station_metro": "Sherbrooke",
 "ligne_metro": "verte",
 "minutes_a_pied": "11 (estime)",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/cession-de-bail-4-1-2-lumineux-charmant-sur-le-plateau/1743158327",
 "score": "8",
 "notes": "Cession de bail, 3e et dernier etage, semi-meuble (electromenagers inclus), climatisation, petit chien accepte, disponible 6 oct. 2026. Distance au metro estimee a partir du secteur H2K (non precisee dans l'annonce).",
 "photo": "",
},
{
 "date_ajout": "2026-10-07",
 "statut": "NOUVEAU",
 "titre": "4½ renove (2 chambres), 900 pi², balcon - Plateau-Mont-Royal (proche Mile End), metro Rosemont/Beaubien/Laurier",
 "quartier": "Le Plateau-Mont-Royal",
 "adresse": "n/d (Montreal, QC H2T 2V4)",
 "prix": "2100",
 "superficie_pi2": "900",
 "chambres": "2",
 "balcon": "oui",
 "station_metro": "Laurier",
 "ligne_metro": "verte",
 "minutes_a_pied": "11 (estime)",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/beautiful-apartment-available-as-of-now-plateau-mont-royal/1743509536",
 "score": "8",
 "notes": "Disponible immediatement, lumineux, proche commerces et cafes (secteur Mile End), animaux non admis, electromenagers inclus, laveuse-secheuse a l'unite. Station la plus proche parmi Rosemont/Beaubien/Laurier (mentionnees dans l'annonce) et distance estimees, non precisees explicitement.",
 "photo": "",
},
{
 "date_ajout": "2026-10-07",
 "statut": "NOUVEAU",
 "titre": "4½ unite de coin (2 chambres), 980 pi², balcon - coin Villeray et Chambord (Villeray), proche metro De Castelnau",
 "quartier": "Villeray",
 "adresse": "n/d (coin rue Villeray et rue Chambord, Montreal, QC)",
 "prix": "1900",
 "superficie_pi2": "980",
 "chambres": "2",
 "balcon": "oui",
 "station_metro": "De Castelnau",
 "ligne_metro": "orange",
 "minutes_a_pied": "10 (estime)",
 "site": "Kijiji",
 "lien": "https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/a-louer-4-1-2-coin-villeray-et-chambord-montreal/1744362598",
 "score": "7",
 "notes": "Unite de coin lumineuse, chauffage/hydro/eau inclus, thermopompe (chauffage+climatisation), laveuse-secheuse/lave-vaisselle/frigo/cuisiniere inclus, rangement au sous-sol, bail a terme fixe jusqu'au 30 juin 2028, verification de credit requise. Station de metro et distance estimees a partir de l'intersection (non precisees dans l'annonce).",
 "photo": "",
},
]

fieldnames = ["date_ajout","statut","titre","quartier","adresse","prix","superficie_pi2","chambres","balcon","station_metro","ligne_metro","minutes_a_pied","site","lien","score","notes","photo"]

with open("annonces.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    existing = list(reader)

all_rows = existing + rows_to_add

def sort_key(r):
    is_new = 0 if r["statut"] == "NOUVEAU" else 1
    try:
        score = -int(r["score"])
    except Exception:
        score = 0
    return (is_new, score)

all_rows.sort(key=sort_key)

with open("annonces.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_rows)

print("Total rows:", len(all_rows))
print("New rows added:", len(rows_to_add))
