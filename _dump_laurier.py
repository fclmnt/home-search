import json
with open('marketplace-raw.json') as f:
    d = json.load(f)
items = d.get('items', [])
for it in items:
    if '1334820052136089' in (it.get('url') or ''):
        print(json.dumps(it, indent=2, ensure_ascii=False)[:2000])
