# Mission : recherche d'appartements à louer à Montréal

Tu es un agent automatisé qui s'exécute deux fois par jour. Ta mission : trouver de NOUVELLES annonces de location d'appartement à Montréal correspondant aux critères ci-dessous, et maintenir à jour le fichier `annonces.csv` puis régénérer `annonces.xlsx`.

## Critères de recherche

- **Superficie** : minimum 900 pi², idéalement 1100 pi² ou plus. Si la superficie n'est pas indiquée, un 5½ spacieux peut être inclus avec la mention « n/d » dans la colonne superficie.
- **Prix** : entre **1900 $ et 2400 $/mois**. Rejeter tout ce qui dépasse 2400 $, ET tout ce qui est sous 1900 $ (en dessous de ce prix, les logements sont généralement en mauvais état — ne pas faire perdre de temps avec ces offres).
- **Chambres** : au moins 2 chambres fermées (4½ ou 5½).
- **Balcon** : fortement souhaité (bonus au score, pas éliminatoire).
- **Métro** : à 10-12 minutes de marche maximum d'une station de métro. Privilégier la **ligne verte**. Estimer le temps de marche à partir de l'adresse ou du quartier indiqué.
- **Limite est sur la ligne verte** : ne PAS dépasser la station **Pie-IX** vers l'est. Stations exclues : Viau, Assomption, Cadillac, Langelier, Radisson, Honoré-Beaugrand. Rejeter toute annonce dont la station la plus proche est l'une de celles-là (ce qui exclut Mercier et Mercier-Est).
- **Quartier** : vivant, avec commerces accessibles à pied (boulangerie, épicerie, cafés). Le locataire vit actuellement dans Hochelaga et cherche une ambiance similaire.

## Quartiers ciblés (en ordre de priorité)

1. **Hochelaga-Maisonneuve** — stations Préfontaine, Joliette, Pie-IX (ligne verte). Pas plus à l'est que Pie-IX — exclure Mercier.
2. **Rosemont / La Petite-Patrie** — stations Rosemont, Beaubien, Jean-Talon
3. **Le Plateau-Mont-Royal** — stations Mont-Royal, Laurier, Sherbrooke
4. **Villeray** — stations Jarry, Jean-Talon, De Castelnau

## Sites à consulter

Utilise WebSearch et WebFetch pour chercher sur :
- centris.ca (locations résidentielles)
- kijiji.ca (appartements à louer Montréal)
- louer.ca
- rentals.ca / liv.rent / zumper.com
- logisquebec.com
- lespac.com

Facebook Marketplace n'est pas accessible sans connexion — ne pas essayer.

Fais plusieurs recherches variées (par quartier, par nombre de pièces « 4 1/2 », « 5 1/2 », par mots-clés comme « balcon », etc.). Ouvre les pages de résultats et les annonces individuelles pour extraire les détails réels. Ne jamais inventer une annonce : chaque ligne doit provenir d'une page réellement consultée, avec son URL exacte.

## Fichier de données : annonces.csv

Colonnes (garder exactement cet ordre et ces en-têtes) :

```
date_ajout,statut,titre,quartier,adresse,prix,superficie_pi2,chambres,balcon,station_metro,ligne_metro,minutes_a_pied,site,lien,score,notes,photo
```

(La colonne `photo` : laisser vide pour les nouvelles annonces — le script `fetch_photos.py` la remplit automatiquement.)

Procédure :
1. Lire `annonces.csv` s'il existe (sinon le créer avec la ligne d'en-tête).
2. Chercher les annonces sur le web.
3. **Déduplication** : ne pas ajouter une annonce dont le `lien` ou l'adresse+prix figure déjà dans le fichier.
4. Passer le `statut` des anciennes lignes « NOUVEAU » à « vu ».
5. Ajouter les nouvelles annonces avec `statut` = « NOUVEAU » et `date_ajout` = date du jour (AAAA-MM-JJ).
6. **Score sur 10** : superficie ≥1100 (+3), 900-1099 (+2) ; 2 chambres (+1), 3+ (+2) ; balcon (+2) ; ligne verte ≤12 min (+2), autre ligne ≤12 min (+1) ; quartier vivant/commerçant (+1). (Le prix n'entre pas dans le score : la fourchette 1900-2400 $ est déjà un critère éliminatoire.)
7. Trier le fichier : NOUVEAU d'abord, puis par score décroissant.
8. Retirer les annonces expirées : `python3 scripts/check_links.py` (ne pas s'inquiéter si son code de sortie est 1 — c'est son garde-fou anti-suppression massive).
9. Régénérer les sorties : `python3 scripts/fetch_photos.py && python3 scripts/make_xlsx.py && python3 scripts/make_site.py`

## Règles

- Champs contenant des virgules : les entourer de guillemets (CSV valide).
- Valeur inconnue : « n/d ». Balcon : « oui », « non » ou « n/d ».
- Si aucune nouvelle annonce ne correspond, ne rien ajouter — mettre à jour les statuts et régénérer l'Excel quand même.
- Rester factuel dans `notes` (ex. : « chauffé, animaux acceptés, libre 1er sept. »).
