import json
d = json.load(open('marketplace-raw.json'))
items = {it['id']: it for it in d['items']}
ids = ['1554806613022043','1007470455527090','1726543035012300','1330675911783970','1524263869204684','1515437773170309','1079557258085987']
for tid in ids:
    it = items[tid]
    print('=====', tid, it['url'])
    print(it.get('extrait',''))
    print()
