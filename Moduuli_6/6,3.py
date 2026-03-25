def gallonat_litroina(maara):
    litrat = maara * 3.785
    return litrat

#Pääohjelma

while True:
    gallonat = float(input("Anna bensiinin määrä gallonoina (negatiivinen lopettaa)"))

    if gallonat < 0:
        print("Määrä on negatiivinen")
        break

    litrat = gallonat_litroina(gallonat)
    print(litrat)