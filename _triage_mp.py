import json, re

with open('marketplace-raw.json') as f:
    d = json.load(f)
items = d['items']


def parse_price(p):
    m = re.search(r'([\d,]+)', p)
    return int(m.group(1).replace(',', '')) if m else None


def parse_beds(text):
    m = re.search(r'(\d+)\s*beds?', text, re.I)
    return int(m.group(1)) if m else None


def parse_sqft(text):
    m = re.search(r'([\d,]+)\s*square feet', text, re.I)
    if m:
        return int(m.group(1).replace(',', ''))
    m2 = re.search(r'(\d{3,5})\s*(pi2|pi²|p2|pieds carrés)', text, re.I)
    if m2:
        return int(m2.group(1))
    return None


def parse_address(text):
    lines = text.split('\n')
    for i, l in enumerate(lines):
        if l.strip() == 'Rentals' and i + 1 < len(lines):
            return lines[i + 1].strip()
    return None


results = []
for it in items:
    price = parse_price(it.get('prix', ''))
    text = it.get('extrait', '')
    beds = parse_beds(text)
    sqft = parse_sqft(text)
    addr = parse_address(text)
    carte = it.get('carte', [])
    loc = carte[2] if len(carte) > 2 else ''
    results.append({
        'id': it['id'],
        'price': price,
        'beds': beds,
        'sqft': sqft,
        'addr': addr,
        'loc': loc,
    })

for r in results:
    print(r['id'], r['price'], 'beds=', r['beds'], 'sqft=', r['sqft'], '|', r['addr'], '|', r['loc'])
