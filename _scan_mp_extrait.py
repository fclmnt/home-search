import json, re, csv

d = json.load(open('marketplace-raw.json'))
items = d['items']

with open('annonces.csv') as f:
    existing_rows = list(csv.DictReader(f))
existing_links = set(r['lien'] for r in existing_rows)

def get_carte_text(it):
    return ' '.join(it.get('carte', []))

def get_price(it):
    m = re.search(r'CA\$([\d,]+)', get_carte_text(it))
    return int(m.group(1).replace(',', '')) if m else None

def get_beds(it):
    text = get_carte_text(it) + ' ' + (it.get('extrait') or '')
    m = re.search(r'(\d+)\s*[Bb]eds?', text)
    if m:
        return int(m.group(1))
    m2 = re.search(r'(\d+)\s*chambres?', text)
    if m2:
        return int(m2.group(1))
    return None

exclude_cities = {'Longueuil, QC', 'Laval, QC', 'Repentigny, QC', 'Westmount, QC',
                   'Hampstead, QC', 'Pointe-Claire, QC', 'St-Constant, QC',
                   'Montréal-Est, QC', 'St-Sulpice, QC', 'Richelieu, QC'}

result = []
for it in items:
    if it.get('url') in existing_links:
        continue
    carte = it.get('carte', [])
    city = carte[-1] if carte else ''
    if city in exclude_cities:
        continue
    price = get_price(it)
    if price is None or price < 1900 or price > 2400:
        continue
    beds = get_beds(it)
    if beds is None or beds < 2:
        continue
    if it.get('extrait'):
        result.append(it)

print('with non-empty extrait matching filters:', len(result))
for it in result:
    print(it['url'])
