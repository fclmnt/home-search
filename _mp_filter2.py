import csv, json

existing_links = set()
with open('annonces.csv') as f:
    r = csv.DictReader(f)
    for row in r:
        existing_links.add(row['lien'].strip())

d = json.load(open('marketplace-raw.json'))

station_keywords = ['prefontaine', 'préfontaine', 'joliette', 'pie-ix', 'pie ix',
                     'rosemont', 'beaubien', 'jean-talon', 'jarry', 'castelnau',
                     'mont-royal', 'laurier', 'sherbrooke', 'papineau', 'frontenac']
price_ok = 0
for it in d['items']:
    if it['url'] in existing_links:
        continue
    carte = ' | '.join(it.get('carte', []))
    extrait = it.get('extrait', '')
    text = (carte + ' ' + extrait).lower()
    if any(k in text for k in station_keywords):
        print(it['url'], '|', carte)
