import json, re
d = json.load(open('marketplace-raw.json'))
items = d.get('items', [])
existing = set(json.load(open('/tmp/existing_links.json')))

def get_city(it):
    carte = it.get('carte')
    if isinstance(carte, list) and carte:
        return carte[-1]
    return ''

def get_beds(it):
    carte = it.get('carte')
    if isinstance(carte, list):
        for c in carte:
            m = re.search(r'(\d+)\s*Beds?', str(c))
            if m:
                return int(m.group(1))
            m2 = re.search(r'(\d+)\s*chambres?', str(c))
            if m2:
                return int(m2.group(1))
    return None

exclude_cities = {'Longueuil, QC','Laval, QC','Repentigny, QC','Westmount, QC','Hampstead, QC'}

candidates = []
for it in items:
    if it.get('url') in existing:
        continue
    city = get_city(it)
    if city in exclude_cities:
        continue
    beds = get_beds(it)
    if beds is None or beds < 2:
        continue
    candidates.append((it, beds))

print('candidates (2+ beds, Montreal-ish):', len(candidates))
print()
for it, beds in candidates:
    extrait = it.get('extrait','') or ''
    # try to find address line - look for lines with digits + street-type word
    addr_match = re.search(r'\n(\d{1,5}[^\n]{0,60}(Rue|Avenue|Boulevard|Boul\.|Chemin|Place)[^\n]{0,60})\n', extrait)
    addr = addr_match.group(1) if addr_match else ''
    sqft_match = re.search(r'(\d{3,5})\s*square feet', extrait)
    sqft = sqft_match.group(1) if sqft_match else 'n/d'
    balcony = 'balcony' in extrait.lower() or 'balcon' in extrait.lower()
    print(f"{it['url']} | beds={beds} | sqft={sqft} | balcony={balcony} | addr={addr!r}")
