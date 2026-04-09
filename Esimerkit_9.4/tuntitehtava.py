hedelmat = {"Appelsiini" : 1,
            "Omena" : 2,
            "Päärynä" : 3}

yhteishinta = 0

while True:
    hedelma = input("Hedelmän nimi (tyhjä lopettaa): ").capitalize()

    if hedelma == "":
        break

    if hedelma in hedelmat:
        print(f"{hedelma}n kilohinta on {hedelmat[hedelma]}")
        yhteishinta += hedelmat[hedelma]
    else:
        print("Meillä ei valitettavasti ole tuota hedelmää varstossa.")
        lisataanko = input("Haluatko lisätä sen(Y/N): ").upper()

        if lisataanko == "Y":
            hinta = float(input(f"Anna hinta {hedelma}lle: "))
            hedelmat[hedelma] = hinta
            print(f"{hedelma} on lisätty kilohinnalla {hinta}.")


print("Yhteishinta tilaukselle on", yhteishinta, "euroa")
for hedelma in hedelmat:
    print(f"Hedelmä: {hedelma}, hinta: {hedelmat[hedelma]}")