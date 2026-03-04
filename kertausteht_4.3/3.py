while True:
    Kokonaisluvut = int(input("Anna kokonaisluku: "))

    if Kokonaisluvut < 0:
        print("Virheellinen numero. ")
    if Kokonaisluvut > 0:
        from math import sqrt
        print(sqrt(Kokonaisluvut))
    if Kokonaisluvut == 0:
        print("Exiting....")
        break

