
sukupuoli = input("sukupuoli: ")

if sukupuoli == "nainen":
    hemoglobiini = int(input("Anna hemoglobiiniarvo: "))
    if(hemoglobiini < 117):
        print("Hemoglobiini on alhainen.")
    elif(hemoglobiini > 175):
        print("Hemoglobiini on korkea.")
    else:
        print("Hemoglobiini on normaali.")

if sukupuoli == "mies":
    hemoglobiini = int(input("Anna hemoglobiiniarvo: "))
    if(hemoglobiini < 134):
        print("Hemoglobiini on alhainen.")
    elif(hemoglobiini > 195):
        print("Hemoglobiini on korkea.")
    else:
        print("Hemoglobiini on normaali.")