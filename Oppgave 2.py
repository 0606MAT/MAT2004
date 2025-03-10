
#Lag et program som tar et tall som input og avgjør om 3 er en faktor i det.



# Be brukeren om å skrive inn et tall
tall = int(input("Skriv inn et tall: "))

# Sjekk om tallet er delelig med 3
if tall % 3 == 0:
    print(tall, "er delelig med 3.")
else:
    print(tall, "er ikke delelig med 3.")