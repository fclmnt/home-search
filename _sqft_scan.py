import json, re
d = json.load(open('marketplace-raw.json'))
items = d['items']
for it in items:
    extrait = it.get('extrait','')
    m = re.search(r'(\d{3,5})\s*square feet', extrait)
    if m and int(m.group(1)) >= 850:
        carte = it.get('carte',[])
        print(it['url'], carte)
        lines = extrait.split('\n')
        for l in lines[:6]:
            print('   ', l)
        print()
