import csv

path = "annonces.csv"
with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

print("before:", len(rows))
for r in rows:
    if r['statut'] == 'NOUVEAU':
        r['statut'] = 'vu'

new_rows = [
{
 "date_ajout":"2026-08-11","statut":"NOUVEAU",
 "titre":"Penthouse 2 étages (2 chambres, 1372-1400 pi²) avec 2 balcons - boul. Pie-IX, Hochelaga-Maisonneuve, à 10 min du métro Pie-IX",
 "quartier":"Hochelaga-Maisonneuve","adresse":"1859, Boulevard Pie-IX, Montréal, QC H1V 2C7",
 "prix":"2250","superficie_pi2":"1372","chambres":"2","balcon":"oui",
 "station_metro":"Pie-IX","ligne_metro":"verte","minutes_a_pied":"10",
 "site":"Zumper","lien":"https://www.zumper.com/listings/773677p/2-bedroom-maisonneuve-montreal-qc",
 "score":"9",
 "notes":"Penthouse d'angle sur deux étages (1372 à 1400 pi² selon la fiche), 2 balcons privés dont un sur cour, non meublé, laveuse-sécheuse et lave-vaisselle inclus, stationnement inclus, aucun animal, chauffage/eau/électricité/internet non inclus, secteur Maisonneuve (pas Mercier), à la limite ouest de Pie-IX autorisée.",
 "photo":""
},
{
 "date_ajout":"2026-08-11","statut":"NOUVEAU",
 "titre":"Superbe 5½ rénové (3 chambres, 950 pi²), balcon - Rosemont/La Petite-Patrie, à 1 min du métro Rosemont",
 "quartier":"Rosemont-La Petite-Patrie","adresse":"n/d (secteur métro Rosemont, Montréal, QC H2S 2P4)",
 "prix":"2100","superficie_pi2":"950","chambres":"3","balcon":"oui",
 "station_metro":"Rosemont","ligne_metro":"orange","minutes_a_pied":"1",
 "site":"Kijiji","lien":"https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/metro-rosemont-superbe-5-1-2-entierement-renove/1741822232",
 "score":"8",
 "notes":"Entièrement rénové (quartz, granit, bois franc), laveuse-sécheuse empilable incluse, chauffage électrique et internet aux frais du locataire, animaux acceptés, disponible 1er septembre 2026, bail 1 an.",
 "photo":""
},
{
 "date_ajout":"2026-08-11","statut":"NOUVEAU",
 "titre":"Grand 4½ (2 chambres, 900 pi²) avec balcon, électros et AC inclus - Hochelaga-Maisonneuve",
 "quartier":"Hochelaga-Maisonneuve","adresse":"n/d (Montréal, QC H1W 3N5)",
 "prix":"1900","superficie_pi2":"900","chambres":"2","balcon":"oui",
 "station_metro":"Joliette ou Pie-IX","ligne_metro":"verte","minutes_a_pied":"8 (estimé)",
 "site":"Kijiji","lien":"https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-4-1-2-avec-balcon-electros-ac-inclus/1740573339",
 "score":"8",
 "notes":"Grand balcon arrière donnant sur jardin calme, tous électroménagers inclus (laveuse-sécheuse, lave-vaisselle, thermopompe), internet et eau inclus, aucun animal, non-fumeur, disponible 1er août 2026, secteur à l'ouest de Pie-IX (limite est respectée).",
 "photo":""
},
{
 "date_ajout":"2026-08-11","statut":"NOUVEAU",
 "titre":"Grand 4½ rénové (2 chambres, 1200 pi²) avec balcon - avenue Henri-Julien, secteur Villeray, à 5 min du métro Jarry",
 "quartier":"Villeray","adresse":"8226, Avenue Henri-Julien, Montréal, QC H2P 2J2",
 "prix":"1900","superficie_pi2":"1200","chambres":"2","balcon":"oui",
 "station_metro":"Jarry","ligne_metro":"orange","minutes_a_pied":"5",
 "site":"Zumper","lien":"https://www.zumper.com/listings/14837712p/2-bedroom-parc-extension-montreal-qc",
 "score":"8",
 "notes":"Balcon arrière, disponible 1er août, animaux non permis, bail long terme uniquement. Secteur à la limite Villeray/Parc-Extension.",
 "photo":""
},
{
 "date_ajout":"2026-08-11","statut":"NOUVEAU",
 "titre":"4½ rénové (2 chambres, 925 pi²) avec patio privé - avenue De Chateaubriand, Rosemont, à 2 min du métro Rosemont",
 "quartier":"Rosemont-La Petite-Patrie","adresse":"5661, Avenue De Chateaubriand, Montréal, QC H2S 0B6",
 "prix":"1960","superficie_pi2":"925","chambres":"2","balcon":"oui",
 "station_metro":"Rosemont","ligne_metro":"orange","minutes_a_pied":"2",
 "site":"Zumper","lien":"https://www.zumper.com/address/5661-ave-de-chateaubriand-montreal-qc-h2s-0b6-can",
 "score":"7",
 "notes":"Unité de coin au dernier étage avec patio privé, 2 salles de bain, table de cuisine/frigo/lave-vaisselle/laveuse-sécheuse et stationnement inclus, vue sur le mont Royal et le Stade olympique, animaux non permis, date de disponibilité négociable.",
 "photo":""
},
{
 "date_ajout":"2026-08-11","statut":"NOUVEAU",
 "titre":"Grand 6½ (possiblement jusqu'à 4 chambres) avec balcon - rue Rivard, Plateau-Mont-Royal, à 5 min du métro Sherbrooke",
 "quartier":"Le Plateau-Mont-Royal","adresse":"4077, Rue Rivard, Montréal, QC H2L 4H9",
 "prix":"2100","superficie_pi2":"n/d","chambres":"3","balcon":"oui",
 "station_metro":"Sherbrooke","ligne_metro":"orange","minutes_a_pied":"5",
 "site":"Zumper","lien":"https://www.zumper.com/apartment-buildings/p531167/appartement-6-1-2-a-louer-plateau-mont-royal-2100-mois-1er-juillet-parc-la-fontaine-montreal-qc",
 "score":"6",
 "notes":"6½ décrit comme grand logement (superficie non précisée), possiblement jusqu'à 4 chambres selon l'annonce (à valider), balcon privé, salle de bain rénovée, disponible 1er juillet, animaux non permis, visites sur rendez-vous. Variante identique au 4073 Rue Rivard (2200$, dispo 1er mai) chez le même propriétaire.",
 "photo":""
},
{
 "date_ajout":"2026-08-11","statut":"NOUVEAU",
 "titre":"5½ neuf (3 chambres) avec balcon - rue Durocher, limite Plateau/Milton-Parc, à 7 min du métro McGill",
 "quartier":"Le Plateau-Mont-Royal","adresse":"3518, Rue Durocher, Montréal, QC H2X 2E5",
 "prix":"2395","superficie_pi2":"n/d","chambres":"3","balcon":"oui",
 "station_metro":"McGill","ligne_metro":"verte","minutes_a_pied":"7",
 "site":"LogisQuébec","lien":"https://www.logisquebec.com/appartement-a-louer-le-plateau-mont-royal-l355132",
 "score":"6",
 "notes":"Immeuble neuf (Jardin Desbarats, 2025), superficie non précisée, 3 chambres fermées, balcon, prix à la limite haute du budget (2395$). Adresse à la frontière Plateau-Mont-Royal / Milton-Parc (McGill Ghetto) — à valider selon vos préférences de secteur.",
 "photo":""
},
{
 "date_ajout":"2026-08-11","statut":"NOUVEAU",
 "titre":"5½ (3 chambres, 1000 pi²) - avenue De Lorimier, Rosemont/La Petite-Patrie, près métro (ligne bleue, à valider)",
 "quartier":"Rosemont-La Petite-Patrie","adresse":"6844, Avenue De Lorimier, Montréal, QC",
 "prix":"2300","superficie_pi2":"1000","chambres":"3","balcon":"n/d",
 "station_metro":"Fabre (à valider)","ligne_metro":"bleue","minutes_a_pied":"8 (estimé)",
 "site":"Centris","lien":"https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/27124862",
 "score":"6",
 "notes":"Semi-meublé, disponible 2 jours après acceptation, Walk Score 94. Station de métro la plus proche estimée par recoupement Walk Score/Moovit, non confirmée directement par la fiche Centris — à valider avant de se déplacer.",
 "photo":""
},
{
 "date_ajout":"2026-08-11","statut":"NOUVEAU",
 "titre":"4½ rénové (2 chambres, 900 pi²) avec cour arrière - Sud-Ouest, près marché Atwater et métro Lionel-Groulx (Marketplace)",
 "quartier":"Saint-Henri (Sud-Ouest)","adresse":"n/d (secteur marché Atwater, Montréal, QC)",
 "prix":"1950","superficie_pi2":"900","chambres":"2","balcon":"non",
 "station_metro":"Lionel-Groulx","ligne_metro":"verte/orange","minutes_a_pied":"7 (estimé)",
 "site":"Marketplace","lien":"https://www.facebook.com/marketplace/item/1348417457196084",
 "score":"6",
 "notes":"Rez-de-chaussée avec cour arrière gazonnée (pas de balcon), laveuse-sécheuse et réfrigérateur inclus, à quelques pas du marché Atwater, Walk Score 99/Transit Score 96, disponible 1er juillet. Lien Facebook (connexion requise).",
 "photo":"https://scontent-yyz1-1.xx.fbcdn.net/v/t39.30808-6/748811511_10175166457760512_4211218329908652441_n.jpg?stp=c0.364.945.945a_dst-jpg_tt6&cstp=mx945x945&ctp=s565x565&_nc_cat=100&ccb=1-7&_nc_sid=454cf4&_nc_ohc=eGRACPj40VQQ7kNvwFEyiu1&_nc_oc=Adr4JDiKbtS7BZMmMyXoesxS4XeJw05eAfBisYvramOx3Vkrx4B8QVhs3Ft0-Bg88W4&_nc_zt=23&_nc_ht=scontent-yyz1-1.xx&_nc_gid=uZUZxQwfjiYjo5O_RDebUQ&_nc_ss=7f2a8&oh=00_AQFITT611kq7OuAN4pfmMMcmrlHPqJq0Yd3-vIHITd5z9g&oe=6A80D870"
},
{
 "date_ajout":"2026-08-11","statut":"NOUVEAU",
 "titre":"Condo 2 chambres (935 pi²) rénové - Ville-Émard, juste en face du métro Angrignon (Marketplace)",
 "quartier":"Ville-Émard","adresse":"n/d (Montréal, QC H4E 2S2)",
 "prix":"1950","superficie_pi2":"935","chambres":"2","balcon":"non",
 "station_metro":"Angrignon","ligne_metro":"verte","minutes_a_pied":"2",
 "site":"Marketplace","lien":"https://www.facebook.com/marketplace/item/2535118233580246",
 "score":"5",
 "notes":"Unité de coin rénovée, électroménagers inclus (frigo, cuisinière, lave-vaisselle, laveuse, sécheuse), ascenseur, garage intérieur inclus, animaux acceptés sous conditions, disponible 1er juillet 2026. Secteur hors des quartiers prioritaires (extrémité ouest de la ligne verte). Lien Facebook (connexion requise).",
 "photo":"https://scontent-yyz1-1.xx.fbcdn.net/v/t39.84726-6/756632406_1023494280537700_7765241118148178522_n.jpg?stp=c90.0.540.540a_dst-jpg_p180x540_tt6&_nc_cat=100&ccb=1-7&_nc_sid=92e707&_nc_ohc=P-KynWpbVNYQ7kNvwEHPtqb&_nc_oc=AdoCiitSI0ZfDm0wVMI3D84zaRteza-39Ny-J93o0mOWkESZ5CXQLekrSLm_UCK5oTg&_nc_zt=14&_nc_ht=scontent-yyz1-1.xx&_nc_gid=uZUZxQwfjiYjo5O_RDebUQ&_nc_ss=7f2a8&oh=00_AQFPflXj3tTrbILJYIvjb5AMGnF2yl2HCg8d8Q-zO8n1hw&oe=6A80EA70"
},
{
 "date_ajout":"2026-08-11","statut":"NOUVEAU",
 "titre":"5½ (3 chambres) - rue Bélanger, Rosemont/La Petite-Patrie, à 5 min du métro D'Iberville",
 "quartier":"Rosemont-La Petite-Patrie","adresse":"2470, Rue Bélanger, Montréal, QC",
 "prix":"1995","superficie_pi2":"n/d","chambres":"3","balcon":"n/d",
 "station_metro":"D'Iberville","ligne_metro":"bleue","minutes_a_pied":"5",
 "site":"Centris","lien":"https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/9637205",
 "score":"4",
 "notes":"Logement de 6 pièces avec 3 chambres fermées (plus spacieux qu'un 5½), superficie non précisée par la fiche, animaux non acceptés, non-fumeurs, disponible 30 jours après acceptation de la promesse de location.",
 "photo":""
},
]

rows.extend(new_rows)
print("after:", len(rows))

def score_key(r):
    try:
        return float(r['score'])
    except Exception:
        return -1

nouveau = [r for r in rows if r['statut'] == 'NOUVEAU']
vu = [r for r in rows if r['statut'] != 'NOUVEAU']
nouveau.sort(key=score_key, reverse=True)
vu.sort(key=score_key, reverse=True)
final = nouveau + vu

with open(path, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(final)

print("wrote", len(final), "rows. NOUVEAU count:", len(nouveau))
