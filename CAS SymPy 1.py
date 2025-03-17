import sympy as sp
x=sp.symbols("x")
L=sp.solveset(x**2-2*x-1, x)
print(L)
