import json, re, csv

with open('marketplace-raw.json') as f:
    d = json.load(f)
items = {it['id']: it for it in d['items']}

with open('annonces.csv') as f:
    existing_links = set(row['lien'] for row in csv.DictReader(f))

def parse_price(s):
    m = re.search(r'CA\$([\d,]+)', s or '')
    return int(m.group(1).replace(',', '')) if m else None

def parse_beds(carte_text):
    for pat in [r'(\d+)\s*Beds', r'(\d+)\s*chambres?', r'(\d+)\s*habitaciones']:
        m = re.search(pat, carte_text)
        if m:
            return int(m.group(1))
    return None

def find_postal(text):
    m = re.search(r'\bH[0-9][A-Z]\s?\d[A-Z]\d\b', text)
    return m.group(0) if m else None

def find_address(text):
    m = re.search(r'\d{2,5}[,]?\s+(?:Rue|Avenue|Ave|Boulevard|Boul\.?|Chemin)\s+[^\n,]+', text)
    return m.group(0) if m else None

# target postal prefixes (2-char) roughly for our neighborhoods
TARGET_PREFIX = ['H1V','H1W','H1X','H1L','H1N',  # Hochelaga-Maisonneuve
                 'H2S','H2G','H1Y','H1Z','H2E',  # Rosemont/Petite-Patrie/Villeray
                 'H2J','H2T','H2W','H2X',  # Plateau
                 'H2R','H2P',  # Villeray
                 'H2K','H2L','H2W']  # Centre-Sud

results = []
for id_, it in items.items():
    if it['url'] in existing_links:
        continue
    carte = it.get('carte', [])
    carte_text = ' | '.join(carte) if isinstance(carte, list) else str(carte)
    price = parse_price(it.get('prix', '') or carte_text)
    if price is None or price < 1900 or price > 2400:
        continue
    if 'Montréal, QC' not in carte_text and 'Montreal' not in carte_text:
        continue
    beds = parse_beds(carte_text)
    if beds is None or beds < 2:
        continue
    extrait = it.get('extrait', '') or ''
    postal = find_postal(extrait) or find_postal(carte_text)
    address = find_address(carte_text) or find_address(extrait)
    results.append((id_, it['url'], price, beds, postal, address))

print('total:', len(results))
for r in results:
    prefix = r[4][:3] if r[4] else None
    marker = ' <<< TARGET' if prefix in TARGET_PREFIX else ''
    print(r[0], r[2], r[3], 'postal=', r[4], 'addr=', r[5], marker)
