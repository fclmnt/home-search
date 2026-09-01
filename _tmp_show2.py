import json
d = json.load(open('marketplace-raw.json'))
items = d['items']
ids = ['1523025982577197', '1292817129693989']
for it in items:
    if it['id'] in ids:
        print('=====', it['id'])
        print('url:', it['url'])
        print('carte:', it['carte'])
        print('image:', it.get('image'))
        print('extrait:')
        print(it.get('extrait', ''))
        print()
