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
    if m:
        return int(m.group(1).replace(',', ''))
    return None

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

candidates = []
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
    candidates.append((it, price, beds))

print('total candidates:', len(candidates))
for it, price, beds in candidates:
    extrait = it.get('extrait', '') or ''
    sqft_m = re.search(r'([\d,]{3,6})\s*square feet', extrait)
    sqft = sqft_m.group(1) if sqft_m else 'n/d'
    balcony = bool(re.search(r'balcon|balcony|terrasse', extrait, re.I))
    # nearby transit block
    transit_m = re.search(r'Nearby Transit(.{0,400})', extrait, re.S)
    transit = transit_m.group(1)[:300].replace('\n', ' | ') if transit_m else ''
    avail_m = re.search(r'Available (\d{4}/\d{2}/\d{2})', extrait)
    avail = avail_m.group(1) if avail_m else 'n/d'
    print('=====')
    print(it['url'], '| price=', price, '| beds=', beds, '| sqft=', sqft, '| balcony=', balcony, '| avail=', avail)
    print('TRANSIT:', transit)
    desc_m = re.search(r'Description\s*\n(.{0,500})', extrait, re.S)
    if desc_m:
        print('DESC:', desc_m.group(1).replace('\n', ' ')[:500])
