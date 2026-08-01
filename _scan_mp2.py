import json, re
d = json.load(open('marketplace-raw.json'))
items = d['items']

keywords = ['Hochelaga','Maisonneuve','Rosemont','Petite-Patrie','Petite Patrie','Plateau','Villeray',
            'Beaubien','Jean-Talon','Jarry','Castelnau','Préfontaine','Prefontaine','Joliette','Pie-IX','Pie IX',
            'Mont-Royal','Masson','Ontario','Sherbrooke','Laurier','Fullum','Moreau','Aird','Théodore','Letourneux',
            'Bourbonnière','Davidson','Valois','Chambly','Iberville','Boyer','Marquette','De Lorimier','Papineau',
            'Dandurand','Everett','Holt','Molson','Bellechasse','Saint-Zotique','St-Zotique','de Gaspé','Gaspe',
            'Christophe-Colomb','Colomb','Chabot','Garnier','Cartier','Marie-Anne','Rachel','Gilford','Marquette',
            'Villeneuve','Berri','St-Denis','Saint-Denis','Drolet','Henri-Julien']

for it in items:
    if it['id'] == '27364351529932787':
        continue
    extrait = it.get('extrait','')
    found = [k for k in keywords if k.lower() in extrait.lower()]
    if found:
        # try to grab address-like line and sqft
        m_addr = re.search(r'\n(\d+[^\n]{0,70}(?:Avenue|Rue|Boulevard|Blvd|Chemin|Place)[^\n]{0,40})\n', extrait)
        m_sqft = re.search(r'([\d,]+)\s*square feet', extrait)
        carte = ' | '.join(it.get('carte',[]))
        print(it['id'], '::', carte[:50], '::', found, '::', m_addr.group(1) if m_addr else 'no-addr', '::', m_sqft.group(1) if m_sqft else 'no-sqft')
