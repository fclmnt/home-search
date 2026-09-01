import json, re
d = json.load(open('marketplace-raw.json'))
items = d['items']
target_prefixes = ('H1V','H1W','H1X','H1Y','H1Z','H2G','H2H','H2J','H2K','H2L','H2S','H2R','H2E','H2W','H2T','H2X','H2Y')
for it in items:
    ex = it.get('extrait','')
    m = re.search(r'H\d[A-Z] ?\d[A-Z]\d', ex)
    if m:
        pc = m.group(0).replace(' ', '')
        if pc[:3] in target_prefixes:
            print(it['id'], it.get('prix'), pc, it.get('carte'))
