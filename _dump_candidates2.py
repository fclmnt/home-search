import json, sys
d = json.load(open('marketplace-raw.json'))
items = {it['id']: it for it in d['items']}
ids = ['1757321265282691','1063108592946643','1467989445057194','881047317720134',
       '955934547488568','1941312389888356','1377928947114418']
for i in ids:
    it = items[i]
    print('='*20, i, it['url'])
    print('IMAGE:', it.get('image','')[:80])
    print(it.get('extrait','')[:1600])
    print()
