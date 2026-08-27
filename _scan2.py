import json, re, unicodedata

d = json.load(open('marketplace-raw.json'))
items = d['items']

banlieue = ['Terrebonne','Longueuil','Laval','Mirabel','Piedmont','Salaberry-de-Valleyfield','Ste-Therese','St-Jerome','Sainte-Therese','Saint-Jerome']

def norm(s):
    return unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode().lower()

addr_re = re.compile(r'\d{2,5}[,]?\s+[A-ZÀ-Ü][A-Za-zÀ-ÿ\'\-\. ]{3,40}')

for it in items:
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
    addrs = addr_re.findall(extrait)
    if addrs:
        print(it['id'], prix, addrs[:2], '|', it['url'])
