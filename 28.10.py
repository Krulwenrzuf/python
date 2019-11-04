# Zadanie 1
"""a1 = int(input('podaj pierwszy wyraz'))
a2 = int(input('podaj drugi wyraz'))
N = int(input('podaj ilość wyrazów'))
ptl = 0
li = [a1, a2]
d = a2 - a1
while ptl < N:
    x = max(li) + d
    print(x)
    li.append(x)
    ptl += 1
print(li)"""
# Zadanie 2
"""a1 = int(input("podaj pierwszy wyraz ciągu"))
q = int(input("podaj q"))
n = int(input("podaj który wyraz ciągu chcesz obliczyć"))
an = a1 * q ** (n - 1)
print(an)"""
# Zadanie 3
import random
li = []
ptl = 0
wyst = []
while ptl < 100:
    li.append(random.randrange(1, 100))
    ptl += 1
N = int(input("podaj N"))
for x in li:
    if li[x] == N:
        wyst.append(x)
print(wyst)