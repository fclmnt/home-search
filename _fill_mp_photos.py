import json, csv

with open('marketplace-raw.json') as f:
    d = json.load(f)
images = {it['url']: it['image'] for it in d['items']}

path = 'annonces.csv'
with open(path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

updated = 0
for r in rows:
    if r['lien'] in images and not r['photo']:
        r['photo'] = images[r['lien']]
        updated += 1

with open(path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Updated {updated} photo fields")
