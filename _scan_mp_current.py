import json, re
with open('marketplace-raw.json') as f:
    d = json.load(f)
items = d['items']

def parse_price(it):
    m = re.search(r'CA\$([\d,]+)', it.get('prix','') or '')
    if not m:
        for c in it.get('carte',[]):
            m = re.search(r'CA\$([\d,]+)', c)
            if m: break
    if m:
        return int(m.group(1).replace(',',''))
    return None

kept = []
for it in items:
    price = parse_price(it)
    if price is None: continue
    if price < 1900 or price > 2400: continue
    carte_text = ' '.join(it.get('carte',[]))
    if 'Montr' not in carte_text:
        continue
    kept.append((price, it))

print('kept count:', len(kept))
for price, it in kept:
    print(price, '|', it.get('url'), '|', it.get('carte'))
