import csv, json

with open('marketplace-raw.json') as f:
    mp = {it['url']: it.get('image', '') for it in json.load(f)['items']}

with open('annonces.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)

filled = 0
for r in rows:
    if not r['photo'].strip() and r['lien'] in mp and mp[r['lien']]:
        r['photo'] = mp[r['lien']]
        filled += 1

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

print(f"{filled} photos remplies depuis marketplace-raw.json")
