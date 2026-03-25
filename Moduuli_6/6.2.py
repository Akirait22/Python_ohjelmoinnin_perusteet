import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

#pääohjelma

maksimi = int(input("Montako tahkoa nopassa on? "))
tulos = 0

while tulos != maksimi:
    tulos = heita_noppaa(maksimi)
    print(tulos)

