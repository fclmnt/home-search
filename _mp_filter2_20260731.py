import json, re

c = json.load(open('_mp_candidates_20260731.json'))

include_keywords = [
    'hochelaga', 'maisonneuve', 'préfontaine', 'joliette', 'pie-ix', 'pie ix',
    'rosemont', 'petite-patrie', 'petite patrie', 'petite-italie', 'petite italie',
    'beaubien', 'jean-talon', 'jean talon', 'plateau', 'mont-royal', 'mont royal',
    'laurier', 'sherbrooke', 'villeray', 'jarry', 'de castelnau', 'castelnau',
    'H1V', 'H1W', 'H1X', 'H1Y', 'H1Z', 'H2G', 'H2H', 'H2J', 'H2K', 'H2L', 'H2M',
    'H2N', 'H2R', 'H2S', 'H2T', 'H2V', 'H2W', 'H2X'
]
exclude_keywords = [
    'lachine', 'lasalle', 'la salle', 'verdun', 'laval', 'longueuil', 'brossard',
    'rive-sud', 'rive sud', 'pointe-claire', 'pointe claire', 'repentigny',
    'chateauguay', 'terrebonne', 'saint-lambert', 'boucherville', 'dorval',
    'beaconsfield', 'dollard', 'kirkland', "l'île", 'ile-perrot', 'vaudreuil',
    'cote-st-luc', 'côte-st-luc', 'cote saint-luc', 'nun\'s island', 'ile-des-soeurs',
    'westmount', 'outremont', 'ahuntsic', 'cartierville', 'saint-michel',
    'saint michel', 'montreal-nord', 'montréal-nord', 'anjou', 'saint-leonard',
    'saint-léonard', 'rivière-des-prairies', 'pointe-aux-trembles', 'mercier',
    'viau', 'assomption', 'cadillac', 'langelier', 'radisson', 'honoré-beaugrand',
    'honore-beaugrand', 'ndg', 'notre-dame-de-grace', 'côte-des-neiges',
    'cote-des-neiges', 'ville-marie', 'centre-ville', 'downtown', 'griffintown',
    'saint-henri', 'pointe-saint-charles', 'sud-ouest', 'lachute', 'H8', 'H9',
    'H4', 'H3E', 'H3J', 'H3K', 'H3H', 'H3G', 'H3A', 'H3B', 'H3C',
]

kept = []
dropped_no_info = []
dropped_excluded = []
for it in c:
    text = (it['extrait'] + ' ' + ' '.join(it['carte'])).lower()
    has_exclude = any(k.lower() in text for k in exclude_keywords)
    has_include = any(k.lower() in text for k in include_keywords)
    if has_exclude and not has_include:
        dropped_excluded.append(it)
        continue
    if has_include:
        kept.append(it)
    else:
        dropped_no_info.append(it)

print('kept:', len(kept))
print('dropped_excluded:', len(dropped_excluded))
print('dropped_no_info (unknown area):', len(dropped_no_info))
json.dump(kept, open('_mp_kept_20260731.json', 'w'), ensure_ascii=False, indent=1)
json.dump(dropped_no_info, open('_mp_noinfo_20260731.json', 'w'), ensure_ascii=False, indent=1)
