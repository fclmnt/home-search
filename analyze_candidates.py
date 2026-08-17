import json, re

with open('/Users/fclement/home-search/marketplace-raw.json') as f:
    data = json.load(f)
items = data['items']


def get_loc(carte):
    for c in carte:
        if isinstance(c, str) and c.endswith(', QC'):
            return c
    return None


def get_beds(carte):
    for c in carte:
        m = re.search(r'(\d+)\s*(Beds|Bed|chambres|chambre)', c, re.I)
        if m:
            return int(m.group(1))
    return None


by_id = {it['id']: it for it in items}

candidates = []
for it in items:
    carte = it.get('carte', [])
    loc = get_loc(carte)
    beds = get_beds(carte)
    if loc is None:
        loc = 'UNKNOWN'
    is_mtl = 'Montréal' in loc or loc == 'UNKNOWN'
    if is_mtl and (beds is None or beds >= 2):
        candidates.append(it['id'])

print(len(candidates))


def extract_address(extrait):
    lines = extrait.split('\n')
    for i, l in enumerate(lines):
        if l.strip() == 'Rentals' and i + 1 < len(lines):
            return lines[i + 1].strip()
    return None


def extract_rental_location(extrait):
    m = re.search(r'Rental Location\n([^\n]+)', extrait)
    return m.group(1) if m else None


def extract_transit(extrait):
    m = re.search(r'Nearby Transit\n(.*?)(?:\nAd\n|\nSeller information|\Z)', extrait, re.S)
    if not m:
        return None
    block = m.group(1)
    block = block.replace('Provided by Walk Score®︎\n', '')
    return block.strip()


def extract_sqft(extrait):
    m = re.search(r'([\d,]{3,6})\s*(square feet|sq\.?\s*ft|pi2|pi²|pieds carrés)', extrait, re.I)
    if m:
        return m.group(1)
    return None


def extract_desc_snippet(extrait):
    m = re.search(r'Description\n(.*?)(?:\n See more|\nGetting Around|\Z)', extrait, re.S)
    if m:
        return m.group(1).strip()[:600]
    return None


out = []
for cid in candidates:
    it = by_id[cid]
    extrait = it.get('extrait', '')
    carte = it.get('carte', [])
    addr = extract_address(extrait)
    rl = extract_rental_location(extrait)
    transit = extract_transit(extrait)
    sqft = extract_sqft(extrait)
    desc = extract_desc_snippet(extrait)
    beds = get_beds(carte)
    out.append(dict(id=cid, url=it['url'], image=it.get('image'), prix=it['prix'], beds=beds, addr=addr, rl=rl,
                     sqft=sqft, transit=transit, desc=desc, carte=carte))

with open('/Users/fclement/home-search/candidates_digest.json', 'w') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

n_addr = sum(1 for x in out if x['addr'])
n_transit = sum(1 for x in out if x['transit'])
n_sqft = sum(1 for x in out if x['sqft'])
print(n_addr, n_transit, n_sqft)
print('done')
