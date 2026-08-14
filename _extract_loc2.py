import json, re
d = json.load(open('marketplace-raw.json'))
items = {it['url']: it for it in d['items']}
c = json.load(open('_candidates_20260814_2.json'))
found = 0
for x in c:
    it = items[x['url']]
    extrait = it.get('extrait', '')
    m = re.search(r'Rental Location\n(.*?)\n', extrait)
    loc = m.group(1) if m else ''
    if loc:
        found += 1
        print(x['prix'], '|', loc, '|', x['url'])
print('total with loc:', found, '/', len(c))
