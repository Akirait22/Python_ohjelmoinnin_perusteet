tuntipalkka = float(input("Anna tuntipalkka: "))
tunnit = float(input("Anna tunnit: "))
viikonpaiva = input("Anna viikonpäivä: ")

if viikonpaiva != "sunnuntai":
    paivapalkka = tuntipalkka * tunnit
else:
    paivapalkka = (tuntipalkka * 2) * tunnit

print("Päiväpalkka: ", paivapalkka, "euroa")