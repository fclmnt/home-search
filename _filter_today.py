import json, re, csv, os

d = json.load(open('marketplace-raw.json'))
items = d['items']

def price_num(s):
    m = re.search(r'CA\$?([\d,]+)', s)
    if m:
        try:
            return int(m.group(1).replace(',', ''))
        except Exception:
            return None
    return None

known_ids = set()
if os.path.exists('annonces.csv'):
    for r in csv.DictReader(open('annonces.csv', newline='', encoding='utf-8')):
        m = re.search(r'/marketplace/item/(\d+)', r.get('lien', ''))
        if m:
            known_ids.add(m.group(1))

candidates = []
for it in items:
    if it['id'] in known_ids:
        continue
    text = ' '.join(it.get('carte', [])) + ' ' + it.get('prix', '')
    if re.search(r'chambre|bed|appartement|apartment|studio|1/2|1½|4½|5½', text, re.I):
        p = price_num(it.get('prix', ''))
        candidates.append((it['id'], p, text[:100]))

print(len(candidates), "candidats (sur", len(items), "items,", len(known_ids), "deja connus)")
for c in candidates:
    print(c)
