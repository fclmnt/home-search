import json, re
d = json.load(open('marketplace-raw.json'))
items = d['items']
existing = set(l.strip() for l in open('_existing_ids.txt') if l.strip())

def parse_price(carte, prix, extrait):
    for s in [prix] + carte:
        m = re.search(r'CA?\$([\d,]+)', s)
        if m:
            return int(m.group(1).replace(',', ''))
    m = re.search(r'CA?\$([\d,]+)\s*/\s*Month', extrait)
    if m:
        return int(m.group(1).replace(',', ''))
    return None

def get_beds(extrait, carte):
    m = re.search(r'(\d+)\s*beds?\s*·', extrait, re.I)
    if m:
        return int(m.group(1))
    for s in carte:
        m = re.search(r'(\d+)\s*Beds?', s)
        if m:
            return int(m.group(1))
    return None

def get_sqft(extrait):
    m = re.search(r'([\d,]+)\s*square feet', extrait, re.I)
    if m:
        return int(m.group(1).replace(',', ''))
    return None

def get_loc(carte):
    for s in carte[::-1]:
        if 'QC' in s or 'Québec' in s:
            return s
    return None

def get_desc(extrait):
    m = re.search(r'Description\n(.*?)(?:\n See more|\nSee translation|\nGetting Around|$)', extrait, re.S)
    if m:
        return m.group(1).strip()
    return ''

def get_avail(extrait):
    m = re.search(r'Available ([^\n·]+)', extrait)
    return m.group(1).strip() if m else None

def get_rental_loc(extrait):
    m = re.search(r'Rental Location\n(.*?)\n', extrait)
    return m.group(1).strip() if m else None

candidates = []
for it in items:
    if it['id'] in existing:
        continue
    extrait = it.get('extrait', '')
    carte = it.get('carte', [])
    price = parse_price(carte, it.get('prix', ''), extrait)
    if price is None or not (1900 <= price <= 2400):
        continue
    loc = get_loc(carte)
    if loc and any(x in loc for x in ['Laval', 'Longueuil', 'Brossard', 'Rive-Sud', 'St-Sauveur', 'La Prairie',
                                       'Pointe-Claire', 'Repentigny', 'Châteauguay', 'Terrebonne', 'Boucherville',
                                       'Saint-Lambert', 'Blainville', "L'Île", 'Ile-Perrot', "Ile-Bizard"]):
        continue
    beds = get_beds(extrait, carte)
    if beds is not None and beds < 2:
        continue
    sqft = get_sqft(extrait)
    if sqft is not None and sqft < 850:
        continue
    desc = get_desc(extrait)
    candidates.append({
        'id': it['id'],
        'url': it['url'],
        'price': price,
        'beds': beds,
        'sqft': sqft,
        'loc': loc,
        'rental_loc': get_rental_loc(extrait),
        'avail': get_avail(extrait),
        'desc': desc,
        'image': it.get('image', ''),
    })

print(len(candidates), "candidates")
json.dump(candidates, open('_mp_candidates2.json', 'w'), ensure_ascii=False, indent=1)
