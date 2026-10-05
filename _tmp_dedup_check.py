import csv
with open('annonces.csv') as f:
    r = list(csv.DictReader(f))
links = set(x['lien'] for x in r)
candidates = [
 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/cession-de-bail-5-hochelaga-maisonneuve-2-195-mois/1743109801',
 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-4-1-2-a-louer-dans-homa-1er-novembre-2026/1743689005',
 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/grand-6-1-2-renove-4-chambres-homa/1743249113',
 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/condo-2-etages-a-louer-villeray/1742950979',
 'https://www.kijiji.ca/v-apartments-condos/ville-de-montreal/appartement-a-louer-en-plein-coeur-de-villeray/1742759946',
 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/28295258',
 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/9228674',
 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/16985529',
 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/16060283',
 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/16826763',
 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/20929421',
 'https://www.centris.ca/fr/condo-appartement~a-louer~montreal-mercier-hochelaga-maisonneuve/11033449',
 'https://centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/21279677',
 'https://centris.ca/fr/condo-appartement~a-louer~montreal-rosemont-la-petite-patrie/25641381',
]
for c in candidates:
    found = any(c.split('/')[-1] in l for l in links)
    print(found, c)
