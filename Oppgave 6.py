
#Lag en funksjon som finner den minste faktoren i et tall


def minste_faktor(n):

         for i in range(2, n + 1):
          if n % i == 0:
            return i  # Returnerer den første (minste) faktoren funnet


# Eksempel på bruk
tall = int(input("Skriv inn et tall: "))
if tall < 2:
    print("Tallet må være større enn 1")
else:
    print("Den minste faktoren til", tall, "er", minste_faktor(tall))
