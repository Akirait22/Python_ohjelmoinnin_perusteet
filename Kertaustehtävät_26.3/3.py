sanat = ["wwwwww", "wwwww", "wwwwwwww","yggggg", "Ö"]

laskuri = 0

for sana in sanat:
    if len(sana) > 5:
        laskuri += 1

print(f" Yli 5 kirjainta sisältävät sanat: {laskuri} kpl")