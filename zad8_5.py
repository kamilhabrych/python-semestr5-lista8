f = open('p.txt','r')

slowo = input("Podaj słowo które chcesz sprawdzić:")

czytaj = f.readlines()

for i in czytaj:
    if slowo in i:
        print(i)

f.close()