def suurin_arvo(luku1, luku2, luku3):
    return max(luku1, luku2, luku3)

luku1= int(input("Anna luku:"))
luku2= int(input("Anna luku2:"))
luku3= int(input("Anna luku3:"))

print(f"Suurin arvo on: {suurin_arvo(luku1, luku2, luku3)}")