# zadanie1
"""y = 0
z = 0
a = [int(x) for x in input().split()]
for x in a:
    if x % 2 == 0:
        y += 1
    else:
        z += 1
print('jest', y,  'liczb parzystych, i', z, 'liczb nieparzystych')"""
# zadanie2
x = str(input('podaj liczbe binarną'))
print(x[len(x) - 1])
if x[len(x)] == 0:
    print('jest to liczba parzysta')
else:
    print('liczba jest nieparzysta')