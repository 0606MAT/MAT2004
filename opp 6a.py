def minste_faktor(n):
    if tall < 2:
        print("Tallet må være større enn 1")
    else:
        for i in range(2, n + 1):
             if n % i == 0:
                 print("Den minste faktoren er", i)
             break


# Eksempel på bruk
tall = int(input("Skriv inn et tall: "))

minste_faktor(tall)