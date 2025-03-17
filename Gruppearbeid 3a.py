import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 2*x**2 - 3*x + 1

# x- verdiene
x = np.linspace(-100, 100, 1000)
# y- verdiene
y = f(x)

# Så plotter vi
plt.plot(x, y, label=r'$y=2x^2 - 3x + 1$', color='blue')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Navn på første- og andreaksen
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = 2x² - 3x + 1')

# Vise grafen
plt.grid()
plt.legend()
plt.show()

