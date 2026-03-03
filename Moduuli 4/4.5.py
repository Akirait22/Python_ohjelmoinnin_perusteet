
oikea_tunnus = "python"
oikea_salasana = "rules"

yritykset = 0
maksimiyritykset = 5

while yritykset < maksimiyritykset:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        yritykset += 1
