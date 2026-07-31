import csv, re

with open('annonces.csv') as f:
    r = csv.DictReader(f)
    rows = list(r)

ids = set()
for row in rows:
    if row['site'] == 'Marketplace':
        link = row['lien']
        m = re.search(r'/item/(\d+)', link)
        if m:
            ids.add(m.group(1))

print(len(ids))
with open('/tmp/existing_ids.txt', 'w') as f:
    f.write('\n'.join(sorted(ids)))
