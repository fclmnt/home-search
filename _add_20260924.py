import csv

PATH = "annonces.csv"
TODAY = "2026-09-24"
FIELDS = ["date_ajout","statut","titre","quartier","adresse","prix","superficie_pi2",
          "chambres","balcon","station_metro","ligne_metro","minutes_a_pied","site",
          "lien","score","notes","photo"]
FB = " Lien Facebook (connexion requise)."
RPP = "Rosemont-La Petite-Patrie"

def row(i, titre, quartier, adresse, prix, sup, ch, balcon, station, ligne, mins, score, notes):
    return {"date_ajout": TODAY, "statut": "NOUVEAU", "titre": titre, "quartier": quartier,
            "adresse": adresse, "prix": str(prix), "superficie_pi2": str(sup), "chambres": str(ch),
            "balcon": balcon, "station_metro": station, "ligne_metro": ligne, "minutes_a_pied": mins,
            "site": "Marketplace", "lien": f"https://www.facebook.com/marketplace/item/{i}",
            "score": str(score), "notes": notes + FB, "photo": ""}

new_rows = [
    row("4692029684455917", "5½ rénové, 3 chambres, 1100 pi², 2 balcons - av. De Châteaubriand (Petite-Patrie), à 5 min du métro Jean-Talon (Marketplace)",
        RPP, "6911, Avenue De Châteaubriand, Montréal, QC H2S 2N9", 2100, 1100, 3, "oui (2 balcons)",
        "Jean-Talon", "orange/bleue", "5", 9,
        "Rez-de-chaussée, plancher bois franc, entrée laveuse/sécheuse, lave-vaisselle. Métro Jean-Talon à 350 m, marché Jean-Talon à 450 m, Plaza St-Hubert adjacente, face à un parc. Non chauffé, non éclairé. Libre immédiatement."),
    row("1965931567448549", "5½ rénové, 3 chambres, 1100 pi², terrasse privée - av. De Châteaubriand (Petite-Patrie), à 5 min du métro Jean-Talon (Marketplace)",
        RPP, "6909, Avenue De Châteaubriand, Montréal, QC H2S 2N9", 2100, 1100, 3, "oui (terrasse privée)",
        "Jean-Talon", "orange/bleue", "5", 9,
        "Même immeuble et même propriétaire que le 6911. Rez-de-chaussée, sous-sol de rangement, stationnement inclus selon une 2e annonce du même logement (item 910103881888546, libre 1er oct.)."),
    row("2503222060152123", "5½ sur 2 étages, 3 chambres, 1600 pi², grande terrasse + jardin - rue Clark (Petite Italie), près du métro De Castelnau (Marketplace)",
        RPP + " (Petite Italie)", "6725, Rue Clark, Montréal", 2300, 1600, 3, "oui (grande terrasse arrière)",
        "De Castelnau", "bleue", "5 (estimé)", 9,
        "1er étage d'un duplex + grand sous-sol aménagé avec porte-patio (superficie inclut le sous-sol). Jardin privé, 1 stationnement. À quelques pas du marché Jean-Talon. Animaux acceptés. Disponible maintenant."),
    row("2322777655136518", "5½, 3 chambres, 1250 pi², grande terrasse - av. Christophe-Colomb (Rosemont), près du métro Rosemont (Marketplace)",
        RPP, "5726, Avenue Christophe-Colomb, Montréal, QC H2S 2G1", 2250, 1250, 3, "oui (grande terrasse/balcon privé)",
        "Rosemont", "orange", "7 (estimé)", 9,
        "Planchers de bois, fraîchement peint, cuisine avec beaucoup de rangement, bain/douche. Disponible maintenant."),
    row("2476229422857514", "Grand logement 4 chambres, 2 sdb, 1800 pi², 2 balcons - rue Bélanger, près du métro Fabre (Marketplace)",
        RPP + " (limite Villeray)", "2302, Rue Bélanger, Montréal, QC H2G 1C8", 2299, 1800, 4, "oui (2 balcons)",
        "Fabre", "bleue", "8 (estimé)", 9,
        "Inclus : frigo, four, laveuse/sécheuse, climatisation, eau chaude. Stationnement disponible. Animaux acceptés. Disponible 30 sept."),
    row("932028789914106", "Grand 5½ rénové, 3 chambres, 1100 pi² - boul. Pie-IX, en face du métro Pie-IX (Marketplace)",
        "Hochelaga-Maisonneuve (secteur Stade olympique)", "2645, Boulevard Pie-IX, app. 1, Montréal", 1950, 1100, 3, "n/d",
        "Pie-IX", "verte", "1-2", 7,
        "Rez-de-chaussée, 6 électros neufs, thermopompe murale, eau chaude et wifi inclus, hydro non inclus. Stationnement 100$/mois. Face au métro Pie-IX, coin Stade olympique / Collège Maisonneuve (secteur moins commerçant). Disponible maintenant."),
    row("3697426357064639", "Cession de bail - Grand 5½, 3 chambres fermées, balcons avant/arrière - rue de Chambly (Hochelaga), près du métro Joliette (Marketplace)",
        "Hochelaga-Maisonneuve", "1663, Rue de Chambly, Montréal, QC H1W 3H9", 2000, "n/d", 3, "oui (petits balcons avant et arrière)",
        "Joliette", "verte", "7 (estimé)", 7,
        "Cession de bail, libre 1er octobre. Récemment rénové, peu coûteux en électricité l'hiver. Distance à pied de la place Valois et du métro Joliette."),
    row("1356255536683378", "7½ rénové, 2 chambres + bureau, 1250 pi², balcons - Hochelaga-Maisonneuve (Marketplace)",
        "Hochelaga-Maisonneuve", "n/d (Hochelaga-Maisonneuve, emplacement approximatif)", 2000, 1250, 2, "oui (balcons refaits 2022)",
        "n/d", "n/d", "n/d", 7,
        "2e étage d'un triplex, double salon, salle à manger, cuisine rénovée 2026 avec îlot, plafonds 9 pi, brique apparente, bois franc. Septembre gratuit si emménagement avant le 1er oct. Adresse non précisée : distance au métro à confirmer."),
    row("1085848001073355", "5½, 2 chambres, ~1000 pi², terrasse privée neuve - rue De Normanville (Rosemont/Petite-Patrie) (Marketplace)",
        RPP, "5905, Rue De Normanville, Montréal", 2100, 1000, 2, "oui (terrasse privée en bois)",
        "Rosemont ou Beaubien", "orange", "8-10 (estimé)", 7,
        "2e étage, très lumineux, beaucoup de rangement, électroménagers inclus. Quartier familial près des parcs, cafés, épiceries."),
    row("956903644139206", "5½, 3 chambres fermées, ~1300 pi², balcons avant/arrière (Marketplace)",
        "n/d (apparu dans la recherche « Hochelaga »)", "n/d (Montréal, emplacement non précisé)", 1900, 1300, 3, "oui (avant et arrière)",
        "n/d", "n/d", "n/d", 7,
        "Triplex, cour arrière avec remise, 2 stationnements, disponible 1er octobre. « Loyer à discuter ». Emplacement et quartier non précisés : à confirmer avant de se déplacer."),
    row("1279356684246355", "Cession de bail - 5½, 3 chambres, balcon + grande terrasse - Quartier latin, à 3 min du métro Sherbrooke (Marketplace)",
        "Ville-Marie (Quartier latin, limite Plateau)", "n/d (Quartier latin, Montréal)", 2383, "n/d", 3, "oui (balcon attenant à une chambre + grande terrasse arrière)",
        "Sherbrooke", "orange", "3", 6,
        "Cession de bail fin septembre/octobre (date flexible). Berri-UQAM (verte) à 6 min. Non meublé ; électros et meubles à vendre par les locataires actuels. Près du parc La Fontaine."),
    row("1629756992004734", "5½ ensoleillé, 3 chambres, balcon - St-André / Bellechasse (Petite-Patrie), entre métros Beaubien et Rosemont (Marketplace)",
        RPP, "6200, Rue Saint-André, Montréal, QC H2S 2K5", 2200, "n/d", 3, "oui (attenant à une chambre)",
        "Beaubien / Rosemont", "orange", "6 (estimé)", 6,
        "3e étage, reprise de bail, dès le 1er octobre (flexible). Électros neufs inclus (four, plaques, lave-vaisselle, frigo, laveuse, sécheuse). Hydro (~100$/mois) et internet non inclus."),
    row("1124423763719846", "5½ rénové, 3 chambres, balcon arrière - face au marché Jean-Talon (Petite Italie), à 5 min du métro (Marketplace)",
        RPP + " (Petite Italie)", "n/d (face au marché Jean-Talon)", 2280, "n/d", 3, "oui (arrière)",
        "Jean-Talon", "orange/bleue", "5", 6,
        "3e étage, lumineux, thermopompe. Non meublé sauf lave-vaisselle (électros rachetables). Entrée laveuse/sécheuse."),
    row("1067090456037266", "5½ de caractère, 3 chambres, grand balcon arrière - av. De Lorimier (Petite-Patrie) (Marketplace)",
        RPP, "6844, Avenue De Lorimier, Montréal, QC H2G 2P9", 2100, "n/d", 3, "oui (grand balcon arrière)",
        "Fabre", "bleue", "8-10 (estimé)", 6,
        "2 pièces doubles + 1 chambre fermée. Boiseries et vitraux d'origine, cuisine et salle de bain rénovées, bois franc. Climatisation disponible."),
    row("1072188295313273", "Grand 6½, 4 chambres, balcon - rue St-Hubert (Villeray), près de 2 métros (Marketplace)",
        "Villeray", "7823, Rue Saint-Hubert, Montréal, QC H2R 2P1", 1950, "n/d", 4, "oui",
        "Jarry", "orange", "5 (estimé)", 6,
        "Près de deux métros (Jarry / Jean-Talon), écoles, Plaza St-Hubert. Entrée laveuse/sécheuse. Chiens acceptés. Disponible maintenant. Annonce très succincte."),
    row("1392048279502553", "Grand 6½, 3 chambres, cour privée + patio - rue William-David (Hochelaga-Maisonneuve), près du métro Pie-IX (Marketplace)",
        "Hochelaga-Maisonneuve", "1629, Rue William-David, Montréal", 2300, "n/d", 3, "non (grande cour arrière privée avec patio)",
        "Pie-IX", "verte", "7 (estimé)", 5,
        "Rez-de-chaussée, salle à manger indépendante, 1 stationnement extérieur, rangement. « Quelques minutes de marche du métro Pie-IX » selon l'annonce."),
    row("1396791209276859", "5½ neuf, 3 chambres - St-Dominique / Beaubien (Petite-Patrie), près du métro Beaubien (Marketplace)",
        RPP, "6528, Rue Saint-Dominique, Montréal, QC H2S 3A7", 2099, "n/d", 3, "n/d",
        "Beaubien", "orange", "4 (estimé)", 4,
        "Loyer réel 2290$ avec janvier gratuit (≈2099$/mois). Rez-de-chaussée, comptoirs quartz, climatisation. Électros haut de gamme en option (25$/électro), stationnement 111$/mois. Pas de chien."),
    row("28984369011158039", "Grand 5½, 3 grandes chambres - rue Jean-Talon Est, sur le marché Jean-Talon (Marketplace)",
        RPP, "192, Rue Jean-Talon Est, Montréal, QC H2R 1S7", 2280, "n/d", 3, "n/d",
        "Jean-Talon / De Castelnau", "orange/bleue", "2-3", 4,
        "Directement sur le marché Jean-Talon. Climatisation, lave-vaisselle. Disponible maintenant. Publiée le 24 sept."),
    row("2316914842389828", "5½ rénové, 2e étage de duplex - rue Boucher (Plateau), à 1 min du métro Laurier (Marketplace)",
        "Le Plateau-Mont-Royal", "422, Rue Boucher, Montréal, QC H2J 1B6", 2300, "n/d", 3, "n/d",
        "Laurier", "orange", "1", 4,
        "Cuisinière, frigo, laveuse et sécheuse inclus, meublé possible. Chauffage et électricité exclus. Disponible maintenant."),
    row("1616666300119740", "Grand 6½ sur 2 étages, 4 chambres - rue De Bordeaux (Villeray), à 5 min du métro Fabre (Marketplace)",
        "Villeray", "7401, Rue De Bordeaux, Montréal, QC H2E 2M6", 1975, "n/d", 4, "non (accès à un patio)",
        "Fabre", "bleue", "5", 4,
        "1 salle de bain + 1 salle d'eau, salle de lavage. Petits animaux acceptés. Non chauffé, non éclairé. Stationnement en sus. Disponible immédiatement."),
    row("1557967656126394", "Grand logement sur 2 étages, 4 chambres + bureau, 2 sdb - rue Villeray, à 12 min des métros Fabre/Jarry (Marketplace)",
        "Villeray", "1180, Rue Villeray, Montréal", 2000, "n/d", 4, "n/d (espace extérieur)",
        "Fabre / Jarry", "bleue/orange", "12", 4,
        "Entrées privées, face à un parc, branchements laveuse/sécheuse, chauffage électrique."),
    row("2580584145719249", "7½ (2 chambres + 2 pièces au sous-sol), petit balcon - Villeray / d'Iberville, à 3 rues du métro D'Iberville (Marketplace)",
        "Villeray (secteur est)", "n/d (angle Villeray / d'Iberville, Montréal)", 2250, "n/d", 2, "oui (petit balcon arrière couvert)",
        "D'Iberville", "bleue", "4 (estimé)", 4,
        "Rez-de-chaussée + sous-sol (2 pièces polyvalentes, salle de lavage, toilette). Accès cour arrière. Propriétaire occupant. Bail 1 ou 2 ans dès le 11 oct. 2026."),
]

with open(PATH, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

links = {r["lien"] for r in rows}
addr_prix = {(r["adresse"].strip().lower(), r["prix"]) for r in rows}
added = []
for n in new_rows:
    if n["lien"] in links or (not n["adresse"].startswith("n/d") and (n["adresse"].strip().lower(), n["prix"]) in addr_prix):
        print("doublon ignoré:", n["lien"]); continue
    added.append(n)

for r in rows:
    if r["statut"] == "NOUVEAU" and r["date_ajout"] < TODAY:
        r["statut"] = "vu"

def sc(r):
    try: return int(r["score"])
    except: return 0
allrows = added + rows
allrows.sort(key=lambda r: (r["statut"] != "NOUVEAU", -sc(r)))

with open(PATH, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    for r in allrows:
        w.writerow({k: r.get(k, "") for k in FIELDS})
print(f"{len(added)} ajoutées, total {len(allrows)}")
