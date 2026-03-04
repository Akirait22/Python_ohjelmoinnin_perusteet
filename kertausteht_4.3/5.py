while True:
    print("Valitse komento: 1 (yhteenlasku), 2 (kertolasku), 3 (jakolasku), 4 (vähennyslasku), 5 (lopetus)")
    lasku = int(input("laskutapa:" ))

    if lasku == 5:
        print("Lopetetaan.")
        break


    luku1 = float(input("Anna ensimmäinen luku: "))
    luku2 = float(input("Anna toinen luku: "))

    if lasku == 1:
        print("Tulos:", luku1 + luku2)
    elif lasku == 2:
        print("Tulos:", luku1 * luku2)
    elif lasku == 3:
        print("Tulos:", luku1 / luku2)
    elif lasku == 4:
        print("Tulos:", luku1 - luku2)



