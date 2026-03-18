import random
Arpakuutiot = int(input("Anna arpakuutiouden lukumäärä: "))

summa = 0

for i in range(Arpakuutiot):
    luku = random.randint(1, 6)
    summa += luku

print(summa)