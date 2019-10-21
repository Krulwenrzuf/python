# zadanie1
"""y = 0
z = 0
a = [int(x) for x in input().split()] # wczytanie kilku liczb i wpisanie ich do zbioru
for x in a:
    if x % 2 == 0:
        y += 1
    else:
        z += 1
print('jest', y,  'liczb parzystych, i', z, 'liczb nieparzystych')
"""
# zadanie2
"""x = str(input('podaj liczbe binarną'))
print(x[len(x) - 1]) # wypisanie ostatniej liczby z zbioru
if int(x[len(x) - 1]) == 0:
    print('jest to liczba parzysta')
else:
    print('liczba jest nieparzysta')
"""
# Zadanie 3
"""x = 1
while x < 100:
    if x % 7 == 0 and x % 8 == 0:
        print(x, "spełnia wymagania")
        x += 1
    else:
        x += 1
"""
# zadanie 4
# nie wiem o co panu dokładnie chodziło ale możliwe że o to
"""x = int(input("podaj pierwszą liczbę"))
y = int(input("podaj drugą liczbę"))
h = 0
l = 0
if x < y:
    hi = y
    lo = x
else:
    lo = y
    hi = x
suma = 0
ptl = lo
zbior = []
while ptl <= hi:
    suma += ptl
    zbior.append(ptl) # dodanie liczby do zbioru
    ptl += 1
print("liczby to:", zbior, "a ich suma to", suma)
"""
# Zadanie 5
"""import random
zb = []
ptl = 0
while ptl < 10:
    x = random.randrange(1, 1000)
    if x % 5 == 0:
        zb.append(x)
        ptl += 1
print(zb)"""
#  Zadanie 6
"""import random
N = random.randrange(1, 100)
A = 0
# pomoc naukowa print(N)
while A != N: # nie równa
    A = int(input("podaj liczbe"))
    if A < N: print("za mała")
    elif A > N: print("za duża")
print("wygrałeś!!!")
"""