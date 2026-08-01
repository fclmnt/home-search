import json, re
d = json.load(open('marketplace-raw.json'))
items = d['items']

keywords = ['Hochelaga','Maisonneuve','Rosemont','Petite-Patrie','Petite Patrie','Plateau','Villeray',
            'Beaubien','Jean-Talon','Jarry','Castelnau','Préfontaine','Prefontaine','Joliette','Pie-IX','Pie IX',
            'Mont-Royal','Masson','Sherbrooke','Laurier','Fullum','Moreau','Aird','Théodore','Letourneux',
            'Bourbonnière','Davidson','Valois','Chambly','Iberville','Boyer','Marquette','De Lorimier','Papineau',
            'Dandurand','Everett','Holt','Molson','Bellechasse','Saint-Zotique','St-Zotique','de Gaspé','Gaspe',
            'Christophe-Colomb','Colomb','Chabot','Garnier','Cartier','Marie-Anne','Rachel','Gilford',
            'Villeneuve','Berri','St-Denis','Saint-Denis','Drolet','Henri-Julien','métro','metro']

for it in items:
    if it['id'] == '27364351529932787':
        continue
    text = it.get('extrait','') + ' ' + ' '.join(it.get('carte',[]))
    found = [k for k in keywords if k.lower() in text.lower()]
    if found:
        carte = ' | '.join(it.get('carte',[]))
        print(it['id'], '::', carte[:60], '::', found)
