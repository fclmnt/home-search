import json
with open('marketplace-raw.json') as f:
    d = json.load(f)
items = d.get('items', [])
targets = ['1334820052136089', '1328856108696346', '1492650335981877']
for it in items:
    url = it.get('url') or ''
    if any(t in url for t in targets):
        print('URL:', url)
        print('CARTE:', it.get('carte'))
        print('EXTRAIT FULL:')
        print(it.get('extrait'))
        print('====')
