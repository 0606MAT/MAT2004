

# Lag et program som sammenligner to tall og forteller deg hvilket som er størst (uten bruk av f-strenger)


# Be brukeren om å skrive inn to tall
tall1 = float(input("Skriv inn det første tallet: "))
tall2 = float(input("Skriv inn det andre tallet: "))

# Sammenlign tallene og skriv ut resultatet
if tall1 > tall2:
    print(tall1, "er større enn", tall2)
elif tall1 < tall2:
    print(tall2, "er større enn", tall1)
else:
    print("Tallene er like.")