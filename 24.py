tall=int(input("skriv et tall: "))
faktorer=0

for divisor in range(2, tall+1):
    if tall%divisor==0:
        faktorer=faktorer+1

if faktorer==1:
        print(f"{tall} er et primtall")

else:
        print(f"{tall} er ikke et primtall")
