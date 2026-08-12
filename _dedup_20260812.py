import csv, json, re, unicodedata

def norm(s):
    s = s or ""
    s = unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode()
    s = s.lower()
    s = re.sub(r'[^a-z0-9 ]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

with open('annonces.csv') as f:
    rows = list(csv.DictReader(f))

existing_liens = set(r['lien'].strip() for r in rows)
existing_addr_price = set()
for r in rows:
    a = norm(r['adresse'])
    p = r['prix'].strip()
    existing_addr_price.add((a, p))

cands = json.load(open('_candidates_20260812.json'))

seen_pairs = set()
final = []
dupes = []
for c in cands:
    lien = c['lien'].strip()
    a = norm(c['adresse'])
    p = str(c['prix'])
    key_lien = lien
    key_addr = (a, p)
    if key_lien in existing_liens:
        dupes.append((c, 'lien existant dans CSV'))
        continue
    if key_addr in existing_addr_price:
        dupes.append((c, 'adresse+prix existant dans CSV'))
        continue
    if key_lien in seen_pairs or key_addr in seen_pairs:
        dupes.append((c, 'doublon interne (autre agent)'))
        continue
    seen_pairs.add(key_lien)
    seen_pairs.add(key_addr)
    final.append(c)

print("=== DOUBLONS ELIMINES ===")
for c, reason in dupes:
    print(f"- [{reason}] {c['titre_short']} | {c['adresse']} | {c['prix']}$ | {c['lien']}")

print()
print(f"=== CANDIDATS FINAUX ({len(final)}) ===")
for c in final:
    print(f"- {c['titre_short']} | {c['adresse']} | {c['prix']}$ | {c['superficie']} pi2 | {c['chambres']}ch | {c['site']}")

json.dump(final, open('_final_candidates_20260812.json','w'), ensure_ascii=False, indent=2)
