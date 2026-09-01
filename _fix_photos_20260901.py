import csv, json

d = json.load(open('marketplace-raw.json'))
items = {it['url']: it['image'] for it in d['items']}

with open('annonces.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
photo_idx = header.index('photo')
lien_idx = header.index('lien')

changed = 0
for r in rows[1:]:
    if r[lien_idx] in items and not r[photo_idx]:
        r[photo_idx] = items[r[lien_idx]]
        changed += 1

with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows(rows)

print("Updated photo for", changed, "rows")
