import json, re, csv

existing_links = set()
existing_addrs = set()
with open('annonces.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        existing_links.add(row['lien'].strip())
        existing_addrs.add((row['adresse'].strip(), row['prix'].strip()))

d = json.load(open('marketplace-raw.json'))
items = d['items']
print('total items:', len(items))

candidates = []
for it in items:
    url = it.get('url','')
    if url in existing_links:
        continue
    extrait = it.get('extrait','')
    carte = it.get('carte', [])
    prix_raw = it.get('prix','')
    m = re.search(r'CA\$([\d,]+)', prix_raw)
    if not m:
        continue
    price = int(m.group(1).replace(',',''))
    if price < 1900 or price > 2400:
        continue
    bedm = re.search(r'(\d+)\s*(?:beds|bed|chambres|chambre)', extrait, re.I)
    beds = int(bedm.group(1)) if bedm else None
    if beds is not None and beds < 2:
        continue
    candidates.append({'url':url,'price':price,'beds':beds,'carte':carte,'extrait':extrait[:400]})

print('candidates after filter:', len(candidates))
for c in candidates:
    print(c['url'], c['price'], c['beds'])
    print(' ', c['carte'])
    print(' ', c['extrait'][:250].replace(chr(10),' | '))
    print()
