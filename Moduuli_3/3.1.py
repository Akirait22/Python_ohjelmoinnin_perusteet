import math
Kuha = float(input("Anna kuhan pituus: "))
if Kuha <=37:
    print("Päästä kuha veteen.")
if Kuha >=37:
    print("Kuha ei ole alimittainen")

Alamitta = 37 - Kuha

if Kuha <=37:
    print(37 - Kuha)
    print(f"Kuha on {Alamitta} cm, alamittainen")
