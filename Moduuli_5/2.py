luvut = []

while True:
    numerot = (input("Anna lukuja (tyhjä lopettaa): "))
    if numerot == "":
        break

    luku = int(numerot)
    luvut.append(luku)

luvut.sort(reverse=True)

print("luvut")
for luku in luvut[:1]:
    print(luvut[:5])
