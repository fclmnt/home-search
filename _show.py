import json
d = json.load(open('marketplace-raw.json'))
items = {it['id']: it for it in d['items']}
ids = ['996601396306892','26167104542875598','2530475880748926','1034425322444723','2129210164276639']
for i in ids:
    it = items[i]
    print('='*20, i, it['prix'])
    print(it['extrait'])
    print()
