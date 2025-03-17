L=[]  #Lager en tom liste som vi vil følge på med tall

min=100 #Tallene skal være mellom min
maks=400 #og maks

t=min  #starter med t=min
while t<= maks:
    #sjekker om t er delelig med 7 og ikke delelig med 3:
    if t%7==0 and t%3!=0:
        L.append(t)
    t=t+1

print(L)