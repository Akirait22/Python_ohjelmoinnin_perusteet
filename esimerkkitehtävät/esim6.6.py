def inventaario(tavarat):
    print("Sinulla on seuraavat tavarat repussa: ")
    for t in tavarat:
        print("- " + t)
        tavarat.clear()
    return

#pääohjelma
reppu = ["taskulamppu", "otsalamppu", "pöytälamppu"]
inventaario(reppu)
reppu.append("eväsleipä")
inventaario(reppu)
