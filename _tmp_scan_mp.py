import json, re

with open('marketplace-raw.json') as f:
    d = json.load(f)
items = d['items']

for it in items:
    carte = ' | '.join(it.get('carte', []))
    m = re.search(r'(\d+)\s*(chambre|bed)', carte, re.I)
    if m and int(m.group(1)) >= 2:
        extrait = it.get('extrait', '')
        lines = extrait.split('\n')
        addr_line = ''
        for l in lines[:6]:
            if 'Montréal' in l or 'QC' in l:
                addr_line = l
                break
        print(it['id'], '|', it['prix'], '|', carte, '|', addr_line)
