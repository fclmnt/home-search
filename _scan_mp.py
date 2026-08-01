import json, re
d = json.load(open('marketplace-raw.json'))
items = d['items']
for it in items:
    if it['id'] == '27364351529932787':
        continue
    extrait = it.get('extrait','')
    lines = extrait.split('\n')
    addr = ''
    for l in lines[:8]:
        if ('Montréal' in l or 'QC' in l) and len(l) < 90 and any(c.isdigit() for c in l):
            addr = l
            break
    carte = ' | '.join(it.get('carte',[]))
    print(it['id'], '::', carte[:60], '::', addr[:90])
