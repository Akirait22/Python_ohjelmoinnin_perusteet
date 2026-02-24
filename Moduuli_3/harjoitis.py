vuosi = int(input("Anna vuosiluku: "))

if vuosi % 4 == 0:
    else:
    print("Se ei ole karkausvuosi.")
    if vuosi % 100 == 0:
        else:
        print("Se on karkausvuosi.")
        if vuosi % 400 == 0:
            print("Se on karkausvuosi.")
        else:
            print("Se ei ole karkausvuosi.")

