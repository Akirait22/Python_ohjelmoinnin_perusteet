while True:
    tuumat = float(input("Anna tuumat (negatiivinen lopettaa)"))
    if tuumat < 0:
        print("Negatiivinen luku, lopetetaan ohjelma.")
        break

    senttimetrit = tuumat * 2.54
    print("senttimetrit:", senttimetrit)