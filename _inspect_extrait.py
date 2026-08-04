import json
d = json.load(open('marketplace-raw.json'))
items = {it['id']: it for it in d['items']}
for tid in ['1554806613022043','1726543035012300','1079557258085987']:
    it = items[tid]
    ex = it.get('extrait','')
    print('===', tid)
    print(ex[:1000])
    print()
