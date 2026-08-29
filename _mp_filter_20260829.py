import json, re
d = json.load(open('marketplace-raw.json'))
items = d.get('items', [])

mtl_keywords = ['Montréal', 'Montreal', 'Hochelaga', 'Maisonneuve', 'Rosemont', 'Petite-Patrie', 'Plateau', 'Villeray', 'Mile-End', 'Mile End', 'Centre-Sud', 'Ville-Marie']
exclude_keywords = ['Laval', 'Longueuil', 'Terrebonne', 'Beauharnois', 'La Prairie', 'Brossard', 'Repentigny', 'Boucherville']

candidates = []
for it in items:
    carte = it.get('carte') or []
    extrait = it.get('extrait') or ''
    loc = carte[2] if len(carte) > 2 else ''
    text = ' '.join(carte) + ' ' + extrait
    m = re.search(r'(\d+)\s*[Bb]eds?', text) or re.search(r'(\d+)\s*chambres?', text)
    beds = int(m.group(1)) if m else None
    m2 = re.search(r'([\d,]+)\s*square feet', text)
    sqft = int(m2.group(1).replace(',','')) if m2 else None
    price = it.get('prix','')
    text_lower = text.lower()
    is_mtl = any(k.lower() in text_lower for k in mtl_keywords) and not any(ex.lower() in text_lower for ex in exclude_keywords)
    if beds and beds >= 2 and is_mtl:
        candidates.append({'url': it['url'], 'price': price, 'beds': beds, 'sqft': sqft, 'loc': loc, 'extrait': extrait[:300]})

print(len(candidates))
for c in candidates:
    print('---')
    print(c['url'], c['price'], 'beds:', c['beds'], 'sqft:', c['sqft'], 'loc:', c['loc'])
    print(c['extrait'])
