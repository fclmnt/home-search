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
 "titre":"4½ rénové (2 chambres, 1200 pi²) meublé et chauffé, cour arrière - rue Saint-Dominique, Petite-Italie/Villeray, à 9 min du métro Beaubien",
 "quartier":"Villeray-Saint-Michel-Parc-Extension (secteur Petite Italie)","adresse":"6723, Rue Saint-Dominique, Montréal, QC H2S 3B1",
 "prix":"2200","superficie_pi2":"1200","chambres":"2","balcon":"oui",
 "station_metro":"Beaubien","ligne_metro":"orange","minutes_a_pied":"9",
 "site":"Kijiji","lien":"https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/villeray-superbe-4-1-2-meuble-et-chauffe-avec-cour-arriere/1741717177",
 "score":"8",
 "notes":"Rez-de-chaussée de triplex dans la Petite Italie, entièrement meublé et équipé, tous services inclus (chauffage, hydro, wifi), cour et jardin privés, sous-sol avec buanderie/rangement, climatisation, lave-vaisselle. Bail non renouvelable de 9 mois se terminant le 30 juin 2027, disponible 1er octobre 2026, animaux limités. À proximité du marché Jean-Talon et du parc Jarry.",
 "photo":""
},
{
 "date_ajout":"2026-08-11","statut":"NOUVEAU",
 "titre":"4½ rénové (2 chambres, 970 pi²) avec balcon privé - avenue Christophe-Colomb, Villeray, à 11 min du métro Jarry",
 "quartier":"Villeray-Saint-Michel-Parc-Extension","adresse":"8325, Avenue Christophe-Colomb, Montréal, QC H2P 0C3",
 "prix":"1950","superficie_pi2":"970","chambres":"2","balcon":"oui",
 "station_metro":"Jarry","ligne_metro":"orange","minutes_a_pied":"11",
 "site":"Kijiji","lien":"https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/villeray-superbe-condo-4-1-2-renove-animaux-permis/1741717173",
 "score":"7",
 "notes":"Construction neuve en béton, 3e étage, balcon privé donnant sur le salon, cuisine moderne équipée, climatisation murale, gym et terrasse dans l'immeuble, ascenseur, sécurité 24h, animaux acceptés, disponible 17 août 2026. Internet haute vitesse en sus (45$/mois).",
 "photo":""
},
{
 "date_ajout":"2026-08-11","statut":"NOUVEAU",
 "titre":"Loft 4½ meublé (2 chambres, 950 pi²) avec balcon, tout inclus - rue Saint-André, Villeray/Petite-Patrie, à 2 min du métro Jean-Talon",
 "quartier":"Villeray-Saint-Michel-Parc-Extension","adresse":"7026, Rue Saint-André, Montréal, QC H2S 2N1",
 "prix":"2250","superficie_pi2":"950","chambres":"2","balcon":"oui",
 "station_metro":"Jean-Talon","ligne_metro":"orange/bleue","minutes_a_pied":"2",
 "site":"Kijiji","lien":"https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/villeray-superbe-condo-4-1-2-meuble-tout-inclus/1741836933",
 "score":"7",
 "notes":"Loft entièrement meublé, plafonds de 12 pieds, tout inclus (chauffage, hydro, eau, wifi), climatisation, lave-vaisselle, laveuse-sécheuse, animaux limités, disponible 17 août 2026, bail 1 an. Entre Villeray et la Petite-Patrie, proche marché Jean-Talon et parc Jarry.",
 "photo":""
},
{
 "date_ajout":"2026-08-11","statut":"NOUVEAU",
 "titre":"4 chambres (1 salle de bain), rue Rachel Est - frontière Plateau-Mont-Royal/Hochelaga, à 6 min du métro Préfontaine (Marketplace)",
 "quartier":"Le Plateau-Mont-Royal (secteur est)","adresse":"2481, Rue Rachel Est, Montréal, QC H2H 1R9",
 "prix":"1900","superficie_pi2":"n/d","chambres":"4","balcon":"n/d",
 "station_metro":"Préfontaine","ligne_metro":"verte","minutes_a_pied":"6",
 "site":"Marketplace","lien":"https://www.facebook.com/marketplace/item/2828101067545786",
 "score":"5",
 "notes":"4 chambres fermées, 1 salle de bain, réfrigérateur/cuisinière/laveuse/sécheuse/eau chaude inclus, disponible maintenant. Superficie et présence de balcon non précisées dans l'annonce. Lien Facebook (connexion requise).",
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
