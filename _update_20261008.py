import csv

path = "annonces.csv"
with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# Step 4: flip old NOUVEAU -> vu
for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'

new_rows = [
{
 "date_ajout":"2026-10-08","statut":"NOUVEAU",
 "titre":"Rare grand logement, 3 chambres fermées + 2 bureaux, 1200 pi², balcon - rue Gauthier (Plateau/De Lorimier), à ~8 min du métro Papineau",
 "quartier":"Le Plateau-Mont-Royal","adresse":"2184, Rue Gauthier, Montréal",
 "prix":"2100","superficie_pi2":"1200","chambres":"3","balcon":"oui",
 "station_metro":"Papineau","ligne_metro":"verte","minutes_a_pied":"8 (estimé)",
 "site":"Kijiji","lien":"https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/rare-large-plateau-3-bedrooms-2-office-spaces/1742864871",
 "score":"10",
 "notes":"Grand solarium/balcon arriere prive, 2 salles de bain, eau chaude incluse, laveuse-secheuse in-unit, proche avenue du Mont-Royal (cafes/restos/epiceries/boulangeries), disponible 31 oct. 2026, animaux limites, distance au metro estimee (non confirmee par l'annonce elle-meme)",
 "photo":""
},
{
 "date_ajout":"2026-10-08","statut":"NOUVEAU",
 "titre":"Magnifique 5½ meublé, 3 chambres + bureau, 1600 pi² - Plateau près du parc La Fontaine, à 5 min du métro Sherbrooke",
 "quartier":"Le Plateau-Mont-Royal","adresse":"n/d (Montréal, QC H2L 3V6, secteur parc La Fontaine)",
 "prix":"2199","superficie_pi2":"1600","chambres":"3","balcon":"oui",
 "station_metro":"Sherbrooke","ligne_metro":"orange","minutes_a_pied":"5",
 "site":"Kijiji","lien":"https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/magnifique-5-1-2-sur-le-plateau/1744407582",
 "score":"9",
 "notes":"Entierement meuble avec electromenagers neufs, terrasse arriere, climatisation, wifi illimite inclus, animaux non permis, disponible 5 oct. 2026, adresse exacte non divulguee par l'annonce",
 "photo":""
},
{
 "date_ajout":"2026-10-08","statut":"NOUVEAU",
 "titre":"Cession de bail - 4½ sur 2 étages, 4 terrasses, 950 pi² - secteur Ville-Marie/Hochelaga, à 6 min du métro Frontenac",
 "quartier":"Hochelaga-Maisonneuve","adresse":"n/d (secteur H2K 2R7, Montréal)",
 "prix":"2150","superficie_pi2":"950","chambres":"2","balcon":"oui",
 "station_metro":"Frontenac","ligne_metro":"verte","minutes_a_pied":"6",
 "site":"Kijiji","lien":"https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/4-sur-2-etages-4-terrasses-2-mois-gratuits/1741461785",
 "score":"8",
 "notes":"Cession de bail avec 2 mois gratuits (loyer affiche 2150$), climatisation + echangeur d'air, 4 terrasses, chats acceptes/chiens sous approbation, disponible 1er nov. 2026, aussi a 8 min du metro Prefontaine, secteur Centre-Sud a la frontiere d'Hochelaga, adresse exacte non divulguee par l'annonce",
 "photo":""
},
{
 "date_ajout":"2026-10-08","statut":"NOUVEAU",
 "titre":"5½ rénové, 3 chambres, 1000 pi² - rue Saint-Dominique (Plateau), à quelques pas du métro Sherbrooke",
 "quartier":"Le Plateau-Mont-Royal","adresse":"3477, Rue Saint-Dominique, Montréal",
 "prix":"2100","superficie_pi2":"1000","chambres":"3","balcon":"oui",
 "station_metro":"Sherbrooke","ligne_metro":"orange","minutes_a_pied":"5",
 "site":"Kijiji","lien":"https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/plateau-superbe-5-1-2-de-3-chambres-disponible-le-1er-juillet/1744351205",
 "score":"8",
 "notes":"Balcon arriere 2e etage, climatisation, eau incluse, laveuse-secheuse in-unit, proche boul. Saint-Laurent/McGill, disponible 1er juillet 2026, animaux limites",
 "photo":""
},
{
 "date_ajout":"2026-10-08","statut":"NOUVEAU",
 "titre":"Grand 4½ rez-de-chaussée, garage double & cour privée - avenue Bourbonnière (Hochelaga), <10 min du métro Joliette",
 "quartier":"Hochelaga-Maisonneuve","adresse":"Avenue Bourbonnière (Montréal, QC H1W 3N6)",
 "prix":"1990","superficie_pi2":"901","chambres":"2 (1 sans porte - a verifier)","balcon":"non",
 "station_metro":"Joliette","ligne_metro":"verte","minutes_a_pied":"9 (estime, <10 selon annonce)",
 "site":"Kijiji","lien":"https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-4-1-2-rdc-garage-double-cour-privee-hochelaga/1743962443",
 "score":"6",
 "notes":"Attention : la 2e piece semble etre un bureau sans porte selon l'annonce (a verifier sur place si elle compte comme chambre fermee) ; garage double + cour privee, climatisation, plancher bois/ceramique, animaux limites, disponible 1er oct. 2026, pas de balcon mentionne (cour privee)",
 "photo":""
},
{
 "date_ajout":"2026-10-08","statut":"NOUVEAU",
 "titre":"4½ (2 chambres fermées), 902 pi² - avenue d'Outremont (Villeray), à 3 min du métro L'Acadie",
 "quartier":"Villeray","adresse":"6900, Avenue d'Outremont, app. 205, Montréal",
 "prix":"2200","superficie_pi2":"902","chambres":"2","balcon":"n/d",
 "station_metro":"L'Acadie","ligne_metro":"bleue","minutes_a_pied":"3",
 "site":"Centris","lien":"https://www.centris.ca/fr/condo-appartement~a-louer~montreal-villeray-saint-michel-parc-extension/15057879",
 "score":"4",
 "notes":"Condo neuf (2019), stationnement garage inclus, cuisine equipee, secteur Chabanel/Parc-Extension en developpement (pas encore tres vivant), disponible 3 mars 2026, balcon non mentionne",
 "photo":""
},
]

all_rows = rows + new_rows

def sort_key(r):
    is_new = 0 if r['statut'] == 'NOUVEAU' else 1
    try:
        score = -int(str(r['score']).strip())
    except Exception:
        score = 0
    return (is_new, score)

all_rows.sort(key=sort_key)

with open(path, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    writer.writerows(all_rows)

print("total rows now:", len(all_rows))
print("NOUVEAU count:", sum(1 for r in all_rows if r['statut']=='NOUVEAU'))
