import json, re
d = json.load(open('marketplace-raw.json'))
items = {it['url']: it for it in d['items']}
c = json.load(open('_candidates_20260814_2.json'))
for x in c:
    it = items[x['url']]
    extrait = it.get('extrait', '')
    m = re.search(r'Rental Location\n(.*?)\n', extrait)
    loc = m.group(1) if m else ''
    m2 = re.search(r'Rentals\n(.*?)\n', extrait)
    loc2 = m2.group(1) if m2 else ''
    print(x['prix'], '|', loc, '|', loc2, '|', x['url'])
