def listan_summa(luvut):
    summa = 0
    for luku in luvut:
        summa = summa + luku
    return summa

#pääohjelma

lista = [5, 10, 15]
yht = listan_summa(lista)
print(yht)