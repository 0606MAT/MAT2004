startfangst=187000
vekstfaktor=0.85
for år in range(0, -11, -1):
    fangst=startfangst*vekstfaktor**år
    print(år, fangst)
    
