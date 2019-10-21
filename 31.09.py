import random
# Zadanie 1
val = {'a': random.randrange(1, 20), 'b': random.randrange(1, 20)}
for x in val:
    print(x, "=", val[x])
print("największa liczba to", max(val, key=val.get), "=", max(val.values()))
# Zadanie 2
'''x = 0
while x < 20:
    print(random.randrange(-10, 10))
    x += 1
# Zadanie 3
lista = [1, 5, 2, 67, 2, 7, 34, 46, 213, 45]
x = 2
while x <= 5:
    print(lista[x])
    x += 1
# Zadanie 4
cos = {'autor': "Michaił Bułhakow",
       'tytuł': "Mistrz i Małgorzata",
       'rok wydania': "1966",
       'typ utworu': "powieść",
       'Język oryginału': "rosyjski"
       }
for x in cos:
    print(x, "-", cos.get(x))'''