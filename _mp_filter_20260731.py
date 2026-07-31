import json, re
d = json.load(open('marketplace-raw.json'))
items = d['items']
existing = set(l.strip() for l in open('/tmp/existing_ids.txt') if l.strip())

def parse_price(carte, prix):
    for s in [prix] + carte:
        m = re.search(r'CA?\$([\d,]+)', s)
        if m:
            return int(m.group(1).replace(',', ''))
    return None

def get_beds(carte, extrait):
    for s in carte:
        m = re.search(r'(\d+)\s*Beds?', s, re.I)
        if m:
            return int(m.group(1))
    m = re.search(r'(\d+)\s*beds?', extrait, re.I)
    if m:
        return int(m.group(1))
    return None

def get_loc(carte):
    for s in carte[::-1]:
        if 'QC' in s or 'Québec' in s:
            return s
    return None

exclude_areas = ['Laval', 'Longueuil', 'Brossard', 'Rive-Sud', 'St-Sauveur', 'La Prairie',
                 'Pointe-Claire', 'Repentigny', 'Chateauguay', 'Terrebonne', 'Saint-Lambert',
                 'Boucherville', 'Verdun', 'LaSalle', 'Lachine', 'Vaudreuil', "L'Île", 'Kirkland',
                 'Dorval', 'Beaconsfield', 'Dollard', 'Cote-St-Luc', 'Côte-St-Luc', 'Mercier']

candidates = []
skipped_existing = 0
for it in items:
    if it['id'] in existing:
        skipped_existing += 1
        continue
    price = parse_price(it.get('carte', []), it.get('prix', ''))
    if price is None or not (1900 <= price <= 2400):
        continue
    beds = get_beds(it.get('carte', []), it.get('extrait',''))
    loc = get_loc(it.get('carte', []))
    if loc and any(x in loc for x in exclude_areas):
        continue
    if beds is not None and beds < 2:
        continue
    candidates.append({
        'id': it['id'],
        'url': it['url'],
        'price': price,
        'beds': beds,
        'loc': loc,
        'carte': it.get('carte'),
        'extrait': it.get('extrait', ''),
        'image': it.get('image', '')
    })

print(len(candidates), "candidates,", skipped_existing, "skipped as already in CSV")
json.dump(candidates, open('_mp_candidates_20260731.json', 'w'), ensure_ascii=False, indent=1)
