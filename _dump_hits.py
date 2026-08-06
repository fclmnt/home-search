import json
candidates = json.load(open('_mp_candidates_20260806.json'))
targets = {
 'https://www.facebook.com/marketplace/item/1349864256977031',
 'https://www.facebook.com/marketplace/item/1042995701648256',
 'https://www.facebook.com/marketplace/item/1549744883437861',
 'https://www.facebook.com/marketplace/item/3728416487365904',
 'https://www.facebook.com/marketplace/item/1688054132479076',
}
for c in candidates:
    if c['url'] in targets:
        print('=' * 80)
        print(c['url'])
        print('carte:', c['carte'])
        print('extrait:')
        print(c['extrait'])
