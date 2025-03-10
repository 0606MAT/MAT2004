

#Lag et program som sammenligner to tall og forteller deg hvilket som er størst (ved bruk av f-strenger)

a=float(input("Skriv inn et tall:"))
b=float(input("Skriv inn et tall til:"))

if a<b:
    print(f"{b} er det største tallet")
elif a>b:
    print(f"{a}er det største tallet")

else:
    print(f"{b}og {a} er samme tall")


