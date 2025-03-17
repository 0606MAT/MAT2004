import numpy as np

oddetall=np.zeros(100)
oddetall[0]=1

for i in range(1,100):
    oddetall[i]=oddetall[i-1]+2

print(oddetall)