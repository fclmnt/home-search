import json, re, csv

with open('marketplace-raw.json') as f:
    d = json.load(f)
items = d['items']

with open('annonces.csv') as f:
    r = csv.DictReader(f)
    existing = list(r)
existing_links = set(row['lien'] for row in existing)

KEYWORDS = ['Hochelaga', 'Maisonneuve', 'Rosemont', 'Petite-Patrie', 'Plateau', 'Villeray',
            'Prefontaine', 'Préfontaine', 'Joliette', 'Pie-IX', 'Pie IX', 'Beaubien', 'Jean-Talon',
            'Mont-Royal', 'Laurier', 'Sherbrooke', 'Jarry', 'Castelnau', 'Masson', 'Frontenac',
            'Ontario', 'Marché', 'metro', 'métro']

def parse_price(carte):
    for c in carte:
        m = re.search(r'CA\$([\d,]+)', c)
        if m:
            return int(m.group(1).replace(',', ''))
    return None

for it in items:
    url = it['url']
    if url in existing_links:
        continue
    price = parse_price(it['carte'])
    if price is None or price < 1900 or price > 2400:
        continue
    text = it['extrait']
    kw_hits = [k for k in KEYWORDS if k.lower() in text.lower()]
    target_hits = [k for k in kw_hits if k.lower() not in ('metro', 'métro', 'sherbrooke', 'ontario', 'marché')]
    if not target_hits:
        continue
    print('=====')
    print(url, '| price:', price, '| kw:', kw_hits)
    print(it['carte'])
    print(text[:1500].replace('\n', ' | '))
