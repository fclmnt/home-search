import json
with open('marketplace-raw.json') as f:
    d = json.load(f)
items = d.get('items', [])
print(len(items))
for it in items:
    extrait = (it.get('extrait') or '')
    carte = it.get('carte') or []
    if len(extrait) > 50:
        print('URL:', it.get('url'))
        print('CARTE:', carte)
        print('EXTRAIT:', extrait[:500].replace(chr(10), ' | '))
        print('---')
