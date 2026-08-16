import json, re

d = json.load(open('marketplace-raw.json'))
items = d['items']

def parse_price(carte):
    for c in carte:
        m = re.match(r'CA\$([\d,]+)', c)
        if m:
            return int(m.group(1).replace(',', ''))
    return None

def parse_beds(carte):
    for c in carte:
        m = re.search(r'(\d+)\s*(Beds|chambres)', c)
        if m:
            return int(m.group(1))
    return None

def is_mtl(carte):
    for c in carte:
        if 'Montréal' in c or 'Montreal' in c:
            return True
    return False

cands = []
for it in items:
    price = parse_price(it['carte'])
    beds = parse_beds(it['carte'])
    mtl = is_mtl(it['carte'])
    if price and 1900 <= price <= 2400 and beds and beds >= 2 and mtl:
        cands.append(it)

print(len(cands))
for it in cands:
    print(it['url'], it['carte'])
