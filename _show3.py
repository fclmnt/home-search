import json
d = json.load(open('marketplace-raw.json'))
items = {it['id']: it for it in d['items']}
it = items['2129210164276639']
print(it['extrait'])
