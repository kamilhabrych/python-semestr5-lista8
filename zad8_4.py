f = open('p.txt','r')

czytaj = f.read()

print(czytaj)

licznik = 0

for litera in czytaj:
    if litera == 'a':
        licznik += 1

print(licznik)

f.close()