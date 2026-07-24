import json, re

with open('marketplace-raw.json') as f:
    d = json.load(f)
items = d['items']


def parse_price(it):
    p = it.get('prix', '')
    m = re.search(r'CA\$([\d,]+)', p)
    if m:
        return int(m.group(1).replace(',', ''))
    return None


def parse_beds(text):
    m = re.search(r'(\d+)\s*beds?\b', text, re.I)
    if m:
        return int(m.group(1))
    m = re.search(r'(\d+)\s*chambres?', text, re.I)
    if m:
        return int(m.group(1))
    m = re.search(r'(\d+)\s*1/2', text)
    if m:
        return int(m.group(1)) - 1  # 5 1/2 => 2 chambres approx (not reliable)
    return None


def parse_sqft(text):
    m = re.search(r'([\d,]+)\s*square feet', text, re.I)
    if m:
        return int(m.group(1).replace(',', ''))
    m2 = re.search(r'(\d{3,5})\s*(pi2|pi²|p2|pieds carrés|sq\.?\s*ft)', text, re.I)
    if m2:
        return int(m2.group(1))
    return None

def parse_transit(text):
    # capture lines after "Nearby Transit" section
    idx = text.find('Nearby Transit')
    if idx == -1:
        return []
    chunk = text[idx:idx+600]
    lines = [l.strip() for l in chunk.split('\n') if l.strip()]
    return lines[:15]

def parse_location(it, text):
    carte = it.get('carte', [])
    loc = None
    for c in carte:
        if isinstance(c, str) and ('QC' in c) and 'CA$' not in c:
            loc = c
            break
    # try Rental Location section
    idx = text.find('Rental Location')
    addr = None
    if idx != -1:
        chunk = text[idx:idx+200]
        lines = [l.strip() for l in chunk.split('\n') if l.strip()]
        if len(lines) > 1:
            addr = lines[1]
    return loc, addr

def parse_desc_address(text):
    # look for street-address-like patterns in Description section
    idx = text.find('Description')
    if idx == -1:
        return None
    chunk = text[idx:idx+800]
    m = re.search(r'\d{3,5}[,]?\s+[A-Za-zÀ-ÿ0-9\'\.\- ]{3,40}(?:Avenue|Rue|Boulevard|Blvd|St-|Ste-|Chemin)[A-Za-zÀ-ÿ0-9\'\.\- ]*', chunk)
    return m.group(0) if m else None


results = []
for it in items:
    price = parse_price(it)
    text = it.get('extrait', '')
    beds = parse_beds(text)
    sqft = parse_sqft(text)
    loc, rental_loc = parse_location(it, text)
    desc_addr = parse_desc_address(text)
    transit = parse_transit(text)
    results.append({
        'id': it['id'],
        'url': it['url'],
        'price': price,
        'beds': beds,
        'sqft': sqft,
        'loc': loc,
        'rental_loc': rental_loc,
        'desc_addr': desc_addr,
        'transit': transit,
    })

# Filter candidates: beds >= 2, price in range (scraper already filtered but double check)
candidates = [r for r in results if (r['beds'] is None or r['beds'] >= 2)]
print(f"Total items: {len(results)}, candidates (beds>=2 or unknown): {len(candidates)}")
for r in candidates:
    print(r['id'], r['price'], 'beds=', r['beds'], 'sqft=', r['sqft'], '|', r['desc_addr'] or r['rental_loc'] or r['loc'])
    if r['transit']:
        print('   transit:', ' / '.join(r['transit'][:6]))
