viikko = ("ma", "ti", "ke", "to", "pe", "la", "su")

paiva = int(input("Anna viikonpäivän numero (1-7):"))

vkpaiva = viikko[paiva -1]

print(f"{paiva}. päivä on {vkpaiva}.")