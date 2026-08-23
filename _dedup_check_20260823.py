import csv
urls = [
'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/14054319',
'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/27865855',
'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/12452944',
'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/25169576',
'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/11597359',
'https://www.centris.ca/en/condos-apartments~for-rent~montreal-mercier-hochelaga-maisonneuve/12933805',
'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/26757939',
'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/24494539',
'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/27341599',
'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/15029641',
'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/20126518',
'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/10601252',
'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/23127352',
'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/14338754',
]
existing_links = set()
existing_ids = set()
with open('annonces.csv') as f:
    r = csv.DictReader(f)
    for row in r:
        existing_links.add(row['lien'])
        if 'centris.ca' in row['lien']:
            existing_ids.add(row['lien'].rstrip('/').split('/')[-1])
for u in urls:
    cid = u.rstrip('/').split('/')[-1]
    print(u in existing_links, cid in existing_ids, u)
