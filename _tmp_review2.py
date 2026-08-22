import json
d = json.load(open('marketplace-raw.json'))
items = {it['url']: it for it in d.get('items', [])}
it = items['https://www.facebook.com/marketplace/item/1600312628440579']
print(repr(it.get('carte')))
print(repr(it.get('extrait')))
