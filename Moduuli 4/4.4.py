import random

oikea_luku = random.randint(1, 10)
luku = 0

print("Arvaa arvottu luku väliltä 1-10. ")

while luku != oikea_luku:
    luku = int(input("Anna luku"))

    if luku > oikea_luku:
        print("Liian suuri luku")
    elif luku < oikea_luku:
        print("Liian pieni luku")
    else:
        print("Oikea luku")