import json, re
with open('marketplace-raw.json') as f:
    d = json.load(f)
items = d.get('items', [])
for it in items:
    extrait = (it.get('extrait') or '')
    m = re.search(r'Rentals\s*\n([^\n]+, Montréal, QC)', extrait)
    if m:
        print(it.get('url'), '|', m.group(1), '|', it.get('carte'))
