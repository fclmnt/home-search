import json
d = json.load(open('marketplace-raw.json'))
items = d.get('items', [])
empty = sum(1 for it in items if not (it.get('extrait') or '').strip())
print('empty extrait:', empty, '/', len(items))
for it in items:
    if it.get('id') == '779551624922094':
        print(json.dumps(it, indent=2, ensure_ascii=False)[:1500])
