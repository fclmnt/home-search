import json
with open('marketplace-raw.json') as f:
    d = json.load(f)
items = {it['id']: it for it in d.get('items', [])}
for i in ["1667192434430051","973452448907992","1310293694593951"]:
    print(i, items[i]['image'])
