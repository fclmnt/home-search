import json
d = json.load(open('marketplace-raw.json'))
items = {it['id']: it for it in d['items']}
for i in ['935122996305742','1095559666684265','2129210164276639']:
    it = items[i]
    print('='*20, i, it['prix'], it['carte'])
    print(it['extrait'][:1500])
    print()
