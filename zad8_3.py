f = open('p.txt','a')
x = input("Podaj pierwszą linijkę:")
y = input("Podaj drugą linijkę:")

f.write('\n')
f.write(x)
f.write('\n')
f.write(y)

f.close()