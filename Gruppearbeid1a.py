import numpy as np
a= np.linspace(0, 10, 100)
b= np.linspace(1, 11, 100)
c= np.zeros(100)
for i in range(100):
    c[i]=a[i]+b[i]

print(c)
