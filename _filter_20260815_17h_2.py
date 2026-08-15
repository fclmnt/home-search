import json, re

with open('_candidates_20260815_17h.json') as f:
    candidates = json.load(f)

keywords = {
    'hochelaga': 'Hochelaga',
    'maisonneuve': 'Maisonneuve',
    'prefontaine': 'Préfontaine',
    'préfontaine': 'Préfontaine',
    'joliette': 'Joliette',
    'pie-ix': 'Pie-IX',
    'pie ix': 'Pie-IX',
    'rosemont': 'Rosemont',
    'petite-patrie': 'Petite-Patrie',
    'petite patrie': 'Petite-Patrie',
    'beaubien': 'Beaubien',
    'jean-talon': 'Jean-Talon',
    'jean talon': 'Jean-Talon',
    'plateau': 'Plateau',
    'mont-royal': 'Mont-Royal',
    'mont royal': 'Mont-Royal',
    'laurier': 'Laurier',
    'sherbrooke': 'Sherbrooke',
    'villeray': 'Villeray',
    'jarry': 'Jarry',
    'castelnau': 'De Castelnau',
    'masson': 'Masson (Hochelaga/Rosemont)',
    'mile-end': 'Mile-End',
    'mile end': 'Mile-End',
}

exclude_keywords = ['mercier', 'anjou', 'pointe-aux-trembles', 'tetreaultville', 'tétreaultville',
                     'montreal-nord', 'montréal-nord', 'ahuntsic', 'cartierville', 'lasalle',
                     'lachine', 'verdun', 'ndg', 'notre-dame-de-grace', 'côte-des-neiges',
                     'saint-michel', 'st-michel', 'riviere-des-prairies', 'rivière-des-prairies',
                     'longue-pointe', 'viau', 'assomption', 'cadillac', 'langelier', 'radisson',
                     'honore-beaugrand', 'honoré-beaugrand']

results = []
for c in candidates:
    extrait = (c.get('extrait') or '').lower()
    carte_text = ' '.join(c.get('carte', [])).lower()
    full = extrait + ' ' + carte_text
    hits = [label for kw, label in keywords.items() if kw in full]
    exhits = [kw for kw in exclude_keywords if kw in full]
    if hits and not exhits:
        results.append((c, sorted(set(hits))))

print('matches:', len(results))
for c, hits in results:
    print('====')
    print(c['url'])
    print('price:', c['_price'], 'beds:', c['_beds'])
    print('hits:', hits)

with open('_matched_20260815_17h.json', 'w') as f:
    json.dump([{**c, '_hits': hits} for c, hits in results], f, ensure_ascii=False, indent=1)
