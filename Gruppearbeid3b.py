import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.exp2(x)

# x- verdiene
x = np.linspace(-10, 10, 1000)
# y- verdiene
y = f(x)

# Så plotter vi
plt.plot(x, y, label=r'$y=2^x-3$', color='blue')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Navn på første- og andreaksen
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = 2^x -3')

#Vise grafen
plt.grid()
plt.legend()
plt.show()

