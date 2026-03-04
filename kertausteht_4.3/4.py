tarina = ""
edellinen_sana = ""

while True:
    sana = input("Anna sana:")
    if sana == "loppu":
        break
    if sana == edellinen_sana:
        break

    tarina += sana + " "

print(tarina)
