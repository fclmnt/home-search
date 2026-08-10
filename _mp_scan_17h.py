import json, re

d = json.load(open('marketplace-raw.json'))
items = {it['id']: it for it in d['items']}

def get_price(it):
    m = re.search(r'CA?\$([\d,]+)', it.get('prix',''))
    if m:
        try:
            return int(m.group(1).replace(',',''))
        except: return None
    return None

existing = set()
import csv
with open('annonces.csv', newline='', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        existing.add(row['lien'])

cand_ids = []
for it in items.values():
    if it['url'] in existing:
        continue
    price = get_price(it)
    if price is None or not (1900 <= price <= 2400):
        continue
    carte = ' | '.join(it.get('carte', []))
    if 'Montréal' not in carte and 'Montreal' not in carte:
        continue
    cand_ids.append(it['id'])

def extract_addr(extrait):
    lines = extrait.split('\n')
    for l in lines[:6]:
        if re.search(r'\d{2,5}\s+[A-Za-zÀ-ÿ\-\' .]+,\s*(Montréal|Montreal|Longueuil|Laval|Brossard|Verdun|LaSalle|Lachine|Pointe|Ville-Marie|Sud-Ouest|Anjou|Saint-Léonard|St-Léonard)', l):
            return l.strip()
    return None

target_kw = ['Hochelaga','Maisonneuve','Rosemont','Petite-Patrie','Villeray','Plateau','Mont-Royal','Saint-Denis','Papineau','Beaubien','Jarry','Jean-Talon','Prefontaine','Préfontaine','Joliette','Pie-IX','Laurier','Sherbrooke','Masson','Iberville','Fabre','Colomb','Marquette','Lorimier','Boyer','Chabot','Garnier','Cartier','Roche','Saint-Hubert','Drolet','Julien','Rivard','Resther','Gilford','Marie-Anne','Gauthier','Adam','Ontario','Sainte-Catherine','Chambord','Louis-Hebert','St-Hubert','St-Denis']

exclude_kw = ['Mercier','Viau','Assomption','Cadillac','Langelier','Radisson','Honore-Beaugrand','Honoré-Beaugrand','Ahuntsic','Saint-Michel','St-Michel','Anjou','Montreal-Nord','Montréal-Nord','LaSalle','Lachine','Verdun','Cote-des-Neiges','Côte-des-Neiges','NDG','Notre-Dame-de-Grace','Outremont','Riviere-des-Prairies','Rivière-des-Prairies','Pointe-aux-Trembles','Saint-Leonard','Saint-Léonard']

out = []
for iid in cand_ids:
    it = items[iid]
    extrait = it.get('extrait','')
    addr = extract_addr(extrait)
    hit = None
    excl = None
    haystack = (addr or '') + ' ' + extrait[:400]
    for kw in target_kw:
        if kw.lower() in haystack.lower():
            hit = kw
            break
    for kw in exclude_kw:
        if kw.lower() in haystack.lower():
            excl = kw
            break
    price = get_price(it)
    carte = it.get('carte', [])
    out.append((iid, price, addr, hit, excl, carte))

print(f"total candidats bruts: {len(cand_ids)}")
print()
for iid, price, addr, hit, excl, carte in out:
    if excl:
        continue
    if not hit:
        continue
    print(iid, price, '|', addr, '|', hit, '|', carte[1] if len(carte)>1 else '')
