import json, re
with open('marketplace-raw.json') as f:
    d = json.load(f)
items = d.get('items', [])

keywords = ['hochelaga', 'maisonneuve', 'rosemont', 'petite-patrie', 'petite patrie',
            'villeray', 'plateau', 'mile-end', 'mile end', 'préfontaine', 'joliette',
            'pie-ix', 'pie ix', 'beaubien', 'jean-talon', 'jean talon', 'laurier',
            'mont-royal', 'mont royal', 'sherbrooke', 'jarry', 'castelnau', 'masson',
            'papineau', 'frontenac', 'l\'assomption', 'viau', 'radisson', 'cadillac',
            'langelier', 'mercier', 'honoré-beaugrand']

for it in items:
    extrait = (it.get('extrait') or '')
    carte = it.get('carte') or []
    text = (str(carte) + ' ' + extrait).lower()
    if any(k in text for k in keywords):
        print('URL:', it.get('url'))
        print('CARTE:', carte)
        print('EXTRAIT:', extrait[:900].replace(chr(10), ' | '))
        print('====')
