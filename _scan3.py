import json, re, unicodedata

d = json.load(open('marketplace-raw.json'))
items = d['items']

banlieue = ['Terrebonne','Longueuil','Laval','Mirabel','Piedmont','Salaberry-de-Valleyfield','Ste-Therese','St-Jerome','Sainte-Therese','Saint-Jerome']

def norm(s):
    return unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode().lower()

already = {'996601396306892','26167104542875598','2530475880748926','1034425322444723','2129210164276639','935122996305742','1095559666684265'}

for it in items:
    if it['id'] in already:
        continue
    carte = it.get('carte', [])
    loc = carte[-1] if carte else ''
    if any(norm(b) in norm(loc) for b in banlieue):
        continue
    prix_str = it.get('prix','')
    m = re.search(r'[\d,]+', prix_str)
    if not m:
        continue
    prix = int(m.group().replace(',',''))
    if prix < 1900 or prix > 2400:
        continue
    extrait = it.get('extrait','')
    hay = norm(extrait)
    if 'square feet' in hay or 'pi2' in hay or 'pieds carres' in hay or re.search(r'\b(9\d{2}|1[0-4]\d{2})\s*(sq|pi)', hay):
        print(it['id'], prix, carte, '|', it['url'])
        print(extrait[:300])
        print('---')
