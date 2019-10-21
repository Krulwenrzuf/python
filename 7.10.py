import random
# zadanie 1
"""n = random.randint(2, 100)
x = 1
d = 0
while x < 100:
    y = n % x
    if y == 0:
        d += 1
    x += 1

if d == 2:
    print(n, "to liczba pierwsza")
else:
    print(n, "nie jest liczbą pierwszą")
"""
# zadanie 2
"""x = 0
y = 0
while x < 100:
    y += random.randint(1, 100)
    x += 1
print(y / 100)
"""
# zadanie 3
"""suma = random.randrange(1, 10) + random.randrange(1, 10) + random.randrange(1, 10)
print ('suma to', suma)
if suma > 20 :
    print("ich suma jest większa od 20")
else :
    print("ich suma nie jest większa od 20")
    """
# Zadanie 4
"""lista = []
while len(lista) < 10:
    x = random.randrange(1, 10)
    lista.append(x)
n = random.randrange(1, 10)
print(lista)
print(n)
if n in lista:
    print('n jest w liście')
else:
    print('nie ma n w liście')"""
# zadanie 5
"""s = str(input("podaj string: "))
z = input("podaj znak: ")
print("znak wystąpił", s.count(z), "razy")"""
# zadanie 6
a = int(input("podaj długość podstawy: "))
h = int(input("podaj długość wysokości: "))
P = (a*h)/2
print("pole to {}cm^2".format(P))
