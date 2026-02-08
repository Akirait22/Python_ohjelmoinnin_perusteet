import math

Leiviskat = float(input("Anna leiviskät: "))
Naulat = float(input("Anna naulat: "))
Luodit = float(input("Anna luodit: "))

luoti_paino = 13.3
naula_paino = 32 * 13.3
Leiviska_paino = 20 * naula_paino

Kokonaispaino = (Leiviskat * Leiviska_paino) + (Luodit * luoti_paino) + (Naulat * naula_paino)

Paino_kiloina = Kokonaispaino // 1000
Grammat = Kokonaispaino % 1000

print("Massa nykymittojen mukaan: ")
print(f"{Paino_kiloina}, {Grammat:3.2f}")