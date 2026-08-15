import json, re

with open('_new_mp_items.json') as f:
    items = json.load(f)

def parse_price(carte):
    if not carte:
        return None
    m = re.search(r'CA\$\s?([\d,]+)', carte[0])
    if not m:
        return None
    return int(m.group(1).replace(',', ''))

def parse_beds(carte):
    if len(carte) < 2:
        return None
    text = carte[1]
    m = re.search(r'(\d+)\s*(chambre|bed)', text, re.I)
    if m:
        return int(m.group(1))
    return None

excluded_suburbs = ['st-lambert','saint-lambert','laval','longueuil','brossard','lasalle','pierrefonds',
                     'dollard','kirkland','pointe-claire','dorval','anjou','saint-leonard','st-leonard',
                     'montreal-nord','montréal-nord','riviere-des-prairies','riviere-des-prairies',
                     'pointe-aux-trembles','lachine','verdun','saint-hubert','st-hubert','boucherville',
                     'repentigny','terrebonne','blainville','candiac','chateauguay','longue-pointe']

candidates = []
rejected_price = 0
rejected_suburb = 0
no_price = 0

for it in items:
    carte = it.get('carte', [])
    price = parse_price(carte)
    if price is None:
        no_price += 1
        continue
    if price < 1900 or price > 2400:
        rejected_price += 1
        continue
    loc = carte[2].lower() if len(carte) > 2 else ''
    if any(s in loc for s in excluded_suburbs):
        rejected_suburb += 1
        continue
    beds = parse_beds(carte)
    candidates.append(dict(it, _price=price, _beds=beds, _loc=(carte[2] if len(carte) > 2 else '')))

print('total items:', len(items))
print('no_price:', no_price)
print('rejected_price:', rejected_price)
print('rejected_suburb:', rejected_suburb)
print('candidates:', len(candidates))
with open('_candidates_20260815_17h.json', 'w') as f:
    json.dump(candidates, f, ensure_ascii=False, indent=1)
for c in candidates:
    print(c['_price'], '|', c['_beds'], '|', c['_loc'], '|', c['url'])
