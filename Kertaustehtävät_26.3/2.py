luvut = []

while True:
    luku = int(input("Anna uusi luku: "))
    if luku == 0:
        break

    luvut.append(luku)
    print(f" lista nyt:", luvut)
    print(f" Lista järjestyksessä:", sorted(luvut))
