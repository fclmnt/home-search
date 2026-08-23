import json
d = json.load(open('marketplace-raw.json'))
items = d['items']
for it in items:
    print(it['id'], '|', it['prix'], '|', it['carte'], '|', it['extrait'][:250].replace(chr(10),' / '))
    print()
