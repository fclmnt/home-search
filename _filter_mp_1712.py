import json, re

d = json.load(open('marketplace-raw.json'))
items = d['items']

NEIGH_KW = [
    'hochelaga','maisonneuve','rosemont','petite-patrie','petite patrie',
    'plateau','villeray','mile-end','mile end','beaubien','jean-talon',
    'jean talon','laurier','mont-royal','sherbrooke','prefontaine','préfontaine',
    'joliette','pie-ix','pie ix','castelnau','jarry','saint-michel','st-michel',
    'masson','ontario','de lorimier','delorimier','papineau',
]
EXCLUDE_KW = ['viau','assomption','cadillac','langelier','radisson','honore-beaugrand',
              "honoré-beaugrand", 'mercier', 'anjou', 'longue-pointe', 'longue pointe',
              'pointe-aux-trembles', 'rivière-des-prairies', 'montreal-nord', 'montréal-nord']

def get_price(it):
    for c in it['carte']:
        m = re.search(r'CA\$([\d,]+)', c)
        if m:
            return int(m.group(1).replace(',', ''))
    m = re.search(r'CA\$([\d,]+)', it.get('prix',''))
    if m:
        return int(m.group(1).replace(',', ''))
    return None

candidates = []
for it in items:
    price = get_price(it)
    if price is None or price < 1900 or price > 2400:
        continue
    text = (' '.join(it['carte']) + ' ' + it.get('extrait','')).lower()
    if any(kw in text for kw in EXCLUDE_KW):
        continue
    if not any(kw in text for kw in NEIGH_KW):
        continue
    candidates.append((price, it))

print(f"Total items: {len(items)}, candidates: {len(candidates)}")
for price, it in candidates:
    beds = re.search(r'(\d+)\s*beds?', it.get('extrait',''), re.I)
    print('---')
    print('price:', price, 'url:', it['url'])
    print('carte:', it['carte'][:3])
    print('beds match:', beds.group(0) if beds else None)
