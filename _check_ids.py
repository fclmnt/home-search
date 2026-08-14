ids = ["1741831701","1741822232","1741536135","1741543595","1736891738","1741986530","1741275574","1734803750","1741249365"]
content = open('annonces.csv').read()
for i in ids:
    print(i, "EXISTS" if i in content else "new")
