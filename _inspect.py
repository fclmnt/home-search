import json, sys
with open('marketplace-raw.json') as f:
    d = json.load(f)
items = d['items']
target = sys.argv[1] if len(sys.argv) > 1 else '1006821535655752'
for it in items:
    if it['id'] == target:
        print(json.dumps(it, indent=2, ensure_ascii=False)[:4000])
        break
