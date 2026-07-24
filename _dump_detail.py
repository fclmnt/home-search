import json
ids = ["1024759733814907","1034802492591491","2246780299474534","1751858266169561",
"1549744883437861","895501206243401","3222347224619384","1526494782507278",
"1006821535655752","1282291854109189"]
with open('marketplace-raw.json') as f:
    d = json.load(f)
items = {it['id']: it for it in d['items']}
for i in ids:
    it = items[i]
    print('=== ', i, ' ===')
    print('URL:', it['url'])
    print('PRIX:', it.get('prix'))
    print('EXTRAIT:')
    print(it.get('extrait',''))
    print()
