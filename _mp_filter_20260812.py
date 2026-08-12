import json, re
data = json.load(open('marketplace-raw.json'))
items = data['items']

exclude_cities = ['Laval','Longueuil','Brossard','Mascouche','Candiac','Deux-Montagnes','Ste-Rose','Ste-Therese','Sainte-Therese','Rawdon','Delson','Repentigny','Terrebonne','Boisbriand','Blainville']

kept = []
for it in items:
    carte = ' '.join(it.get('carte', []))
    if 'Montréal' not in carte:
        continue
    if any(c in carte for c in exclude_cities):
        continue
    m = re.search(r'(\d+)\s*(Beds|chambres)', carte)
    beds = int(m.group(1)) if m else None
    if beds is not None and beds < 2:
        continue
    kept.append((it['url'], carte, beds, it))
print(len(kept))
for u,c,b,it in kept:
    print(b, '|', c[:150], '|', u)
