
#Lag et program som tar et tall som input og avgjør om tallet er et oddetall.


# Be brukeren om å skrive inn et tall
tall = int(input("Skriv inn et tall: "))

# Sjekk om tallet er et oddetall
if tall % 2 != 0:
    print(tall, "er et oddetall.")
else:
    print(tall, "er et partall.")