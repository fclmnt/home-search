import json

with open('marketplace-raw.json') as f:
    d = json.load(f)
items = {it['id']: it for it in d.get('items', [])}

ids = ["4223604171217760","1196035375395868","1667192434430051","1747463642917465","973452448907992","1310293694593951"]
for i in ids:
    it = items[i]
    print("="*80)
    print(i, it['url'], it['prix'])
    print(it['extrait'])
    print()
