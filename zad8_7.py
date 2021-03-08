f = open('p.txt', 'r')
f1 = open('p2.txt','w')

plik = f.read()

for litera in plik:
    if litera == ' ':
        f1.write('*')
    else:
        f1.write(litera.upper())

f.close()
f1.close()