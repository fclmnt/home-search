import json, re

with open('_candidates_20260815_17h.json') as f:
    candidates = json.load(f)

def extract_info(extrait):
    info = {}
    m = re.search(r'([\d,]+)\s*square feet', extrait)
    if m:
        info['sqft'] = m.group(1)
    m = re.search(r'Rental Location\s*\n(.+)', extrait)
    if m:
        info['loc'] = m.group(1).strip()
    else:
        # try first address-like line
        m2 = re.search(r'\n(\d+[^\n]{0,60}Montr[eé]al[^\n]{0,30})\n', extrait)
        if m2:
            info['loc'] = m2.group(1).strip()
    m = re.search(r'[Mm][ée]tro[^\n.]{0,60}', extrait)
    if m:
        info['metro_mention'] = m.group(0).strip()
    return info

out = []
for c in candidates:
    extrait = c.get('extrait') or ''
    info = extract_info(extrait)
    out.append({
        'url': c['url'],
        'price': c['_price'],
        'beds': c['_beds'],
        'sqft': info.get('sqft', 'n/d'),
        'loc': info.get('loc', 'n/d'),
        'metro': info.get('metro_mention', ''),
    })

for o in out:
    print(f"{o['price']:5} | {str(o['beds']):4} | sqft={o['sqft']:>6} | {o['loc'][:60]:60} | metro={o['metro']} | {o['url']}")
