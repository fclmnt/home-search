import csv
with open('annonces.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.reader(f))
header, data = rows[0], rows[1:]
imgs = {
    'https://www.facebook.com/marketplace/item/1034425322444723': 'https://scontent-yyz1-1.xx.fbcdn.net/v/t39.84726-6/724174498_986451427362791_2354216600396771595_n.jpg?stp=c0.87.526.526a_dst-jpg_p526x395_tt6&_nc_cat=107&ccb=1-7&_nc_sid=92e707&_nc_ohc=A7xuOojioacQ7kNvwEpBjv9&_nc_oc=Adp07rVyCTSdvON_GHUkgtkbTVkyXryWHFnSLtzm7jCgBnHmQa3GYTKbU62tjAqaTFA&_nc_zt=14&_nc_ht=scontent-yyz1-1.xx&_nc_gid=l2iYorXZG5uQ4C0wfNm3Rw&_nc_ss=7f2a8&oh=00_AQF7T5L1qjiWhL38C_g4OheBaQVDpLTl7mmaK7veeJmoDg&oe=6A965E70',
    'https://www.facebook.com/marketplace/item/2129210164276639': 'https://scontent-yyz1-1.xx.fbcdn.net/v/t39.84726-6/598654016_1589371882248064_7696909030407170199_n.jpg?stp=c89.0.540.540a_dst-jpg_p180x540_tt6&_nc_cat=106&ccb=1-7&_nc_sid=92e707&_nc_ohc=N7m7nUpE6yMQ7kNvwEavU5f&_nc_oc=AdoffqWsvOkDQufR2l4pvvs8I99wUIXqF-oRgpMOgZIXjIPtOiBQxSSfc9hbuhLkhtM&_nc_zt=14&_nc_ht=scontent-yyz1-1.xx&_nc_gid=XHazkfFuptT2M_pPSTeS4Q&_nc_ss=7f2a8&oh=00_AQFmBd7yIIHbAZt0cYChuyEoJmxi7lgNayPM_0n-aenWnQ&oe=6A9664A6',
}
n = 0
for row in data:
    if row[13] in imgs:
        row[16] = imgs[row[13]]
        n += 1
with open('annonces.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow(header)
    w.writerows(data)
print('updated', n)
