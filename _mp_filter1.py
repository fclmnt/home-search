import csv, json

existing_links = set()
existing_addr_price = set()
with open('annonces.csv') as f:
    r = csv.DictReader(f)
    for row in r:
        existing_links.add(row['lien'].strip())
        existing_addr_price.add((row['adresse'].strip(), row['prix'].strip()))

d = json.load(open('marketplace-raw.json'))
print('total items', len(d['items']))

keywords = ['hochelaga', 'maisonneuve', 'rosemont', 'petite-patrie', 'petite italie',
            'villeray', 'plateau', 'mile-end', 'mile end', 'prefontaine', 'préfontaine',
            'joliette', 'pie-ix', 'pie ix', 'beaubien', 'jean-talon', 'jarry',
            'castelnau', 'mont-royal', 'laurier', 'sherbrooke']

count = 0
for it in d['items']:
    if it['url'] in existing_links:
        continue
    carte = ' | '.join(it.get('carte', []))
    extrait = it.get('extrait', '')
    text = (carte + ' ' + extrait).lower()
    if not any(k in text for k in keywords):
        continue
    count += 1
    print('---')
    print(it['url'])
    print(carte)
    print(extrait[:400].replace(chr(10), ' / '))

print('candidates:', count)
