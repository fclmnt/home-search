import json, re

d = json.load(open('marketplace-raw.json'))
items = {it['url']: it for it in d['items']}

urls = """https://www.facebook.com/marketplace/item/1297601101786789
https://www.facebook.com/marketplace/item/1706776653705703
https://www.facebook.com/marketplace/item/1309508257615155
https://www.facebook.com/marketplace/item/970016458942788
https://www.facebook.com/marketplace/item/1011098805074500
https://www.facebook.com/marketplace/item/1367445445365243
https://www.facebook.com/marketplace/item/2840488989653913
https://www.facebook.com/marketplace/item/3241653845973788
https://www.facebook.com/marketplace/item/3499781920185594
https://www.facebook.com/marketplace/item/2239254116867198
https://www.facebook.com/marketplace/item/1017986564365819
https://www.facebook.com/marketplace/item/1549217026901361
https://www.facebook.com/marketplace/item/1727360391925373
https://www.facebook.com/marketplace/item/1397749988923509
https://www.facebook.com/marketplace/item/1874572703196950
https://www.facebook.com/marketplace/item/1379078317684196
https://www.facebook.com/marketplace/item/1532425805211347
https://www.facebook.com/marketplace/item/1337767638442701
https://www.facebook.com/marketplace/item/1053610007209528
https://www.facebook.com/marketplace/item/27423498327275001
https://www.facebook.com/marketplace/item/1554281676482438
https://www.facebook.com/marketplace/item/1292817129693989
https://www.facebook.com/marketplace/item/1492650335981877
https://www.facebook.com/marketplace/item/1662017041523552
https://www.facebook.com/marketplace/item/28398408193099428
https://www.facebook.com/marketplace/item/1968708320488677
https://www.facebook.com/marketplace/item/858400400676445
https://www.facebook.com/marketplace/item/1542829830212191
https://www.facebook.com/marketplace/item/27636839122593080
https://www.facebook.com/marketplace/item/1515167730107247
https://www.facebook.com/marketplace/item/27014796691457534
https://www.facebook.com/marketplace/item/4803436719883674
https://www.facebook.com/marketplace/item/2854332748266008
https://www.facebook.com/marketplace/item/1266042608798816
https://www.facebook.com/marketplace/item/820719171008330
https://www.facebook.com/marketplace/item/1609330077224598
https://www.facebook.com/marketplace/item/983761451289211
https://www.facebook.com/marketplace/item/1342414611146666
https://www.facebook.com/marketplace/item/994319949845546
https://www.facebook.com/marketplace/item/1425093529446372
https://www.facebook.com/marketplace/item/1000967902380806
https://www.facebook.com/marketplace/item/1733162454373825
https://www.facebook.com/marketplace/item/834310439300902
https://www.facebook.com/marketplace/item/1523602402432168
https://www.facebook.com/marketplace/item/1797932827858417""".split()

for url in urls:
    it = items.get(url)
    if not it:
        print(url, "MISSING")
        continue
    ex = it.get('extrait', '')
    # try to get address line (usually line 3 after price and "Rentals")
    lines = [l.strip() for l in ex.split('\n') if l.strip()]
    addr = lines[2] if len(lines) > 2 else 'n/d'
    sqft_m = re.search(r'([\d,]+)\s*square feet', ex)
    sqft = sqft_m.group(1) if sqft_m else 'n/d'
    beds_m = re.search(r'(\d+)\s*beds?', ex, re.I)
    print(url)
    print('  addr:', addr, '| sqft:', sqft)
