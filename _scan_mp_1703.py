import json, re
d = json.load(open('marketplace-raw.json'))
items = d['items']
print(len(items))
apt = []
for it in items:
    carte_text = ' '.join(it.get('carte', []))
    if re.search(r'Bed|chambre|Apartment|Appartement|½|1/2', carte_text, re.I):
        apt.append(it)
print('apt-like count:', len(apt))
for it in apt:
    print('---')
    print(it['id'], it['url'])
    print(it.get('carte'))
