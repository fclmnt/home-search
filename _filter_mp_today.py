import json, re, csv

d = json.load(open('marketplace-raw.json'))
items = d['items']

existing_links = set()
with open('annonces.csv') as f:
    r = csv.DictReader(f)
    for row in r:
        if row['lien']:
            existing_links.add(row['lien'].strip())

candidates = []
for it in items:
    if it['url'] in existing_links:
        continue
    carte = ' '.join(it.get('carte', []))
    extrait = it.get('extrait', '')
    text = (carte + ' ' + extrait).lower()
    m = re.search(r'(\d+)\s*beds?', text)
    if not m:
        m2 = re.search(r'(\d+)\s*chambres?', text)
        beds = int(m2.group(1)) if m2 else None
    else:
        beds = int(m.group(1))
    if beds is None or beds < 2:
        continue
    candidates.append((it, beds))

print('candidates with >=2 beds:', len(candidates))
for it, beds in candidates:
    print('====', beds, 'beds')
    print(it['url'])
    print(it['prix'])
    print(it['carte'])
    print(it['extrait'][:500].replace(chr(10), ' | '))
