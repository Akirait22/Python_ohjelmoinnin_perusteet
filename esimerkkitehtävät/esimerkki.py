kuha = int(input("Kuinka suuren kuhan sait (negatiivinen lopettaa)?"))

while kuha > 0:
    if kuha < 37:
        puutos = 37 - kuha
        print("Kuhasi oli", puutos, "senttä liian lyhyt.")
    else:
        print("Hieno kuha.")

    kuha = int(input("Kuinka suuren kuhan sait (negatiivinen lopettaa)? "))

print("Kuhalaskuri lopetetaan")