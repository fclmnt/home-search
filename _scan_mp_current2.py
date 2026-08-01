import json, re
with open('marketplace-raw.json') as f:
    d = json.load(f)
items = d['items']

def parse_price(it):
    m = re.search(r'CA\$([\d,]+)', it.get('prix','') or '')
    if not m:
        for c in it.get('carte',[]):
            m = re.search(r'CA\$([\d,]+)', c)
            if m: break
    if m:
        return int(m.group(1).replace(',',''))
    return None

KEYWORDS = ['Hochelaga','Maisonneuve','Rosemont','Petite-Patrie','Petite Patrie','Plateau',
            'Villeray','Préfontaine','Prefontaine','Joliette','Pie-IX','Pie IX','Beaubien',
            'Jean-Talon','Jarry','Mont-Royal','Laurier','Sherbrooke','de Castelnau','Castelnau',
            'Rosemont','Masson','Ontario','Sainte-Catherine','Ste-Catherine']

EXCLUDE_KEYWORDS = ['Anjou','Laval','Boucherville','Longueuil','Brossard','Saint-Laurent',
                     'Ahuntsic','Mercier','Viau','Assomption','Cadillac','Langelier','Radisson',
                     'Honoré-Beaugrand','Honore-Beaugrand','LaSalle','Verdun','Lachine',
                     'Pointe-aux-Trembles','Rivière-des-Prairies','Montréal-Nord','Montreal-Nord',
                     'Saint-Léonard','St-Leonard','Saint-Michel','Côte-des-Neiges',
                     'Notre-Dame-de-Grâce', 'NDG','Dorval','Pierrefonds']

kept = []
for it in items:
    price = parse_price(it)
    if price is None: continue
    if price < 1900 or price > 2400: continue
    extrait = it.get('extrait','') or ''
    carte_text = ' '.join(it.get('carte',[]))
    if 'Montr' not in carte_text and 'Montr' not in extrait:
        continue
    hay = extrait
    matched = [k for k in KEYWORDS if k.lower() in hay.lower()]
    excluded = [k for k in EXCLUDE_KEYWORDS if k.lower() in hay.lower()]
    if excluded:
        continue
    if not matched:
        continue
    kept.append((price, it, matched))

print('kept count:', len(kept))
for price, it, matched in kept:
    print('====', price, it.get('url'), matched)
