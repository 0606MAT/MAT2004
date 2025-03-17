from sympy import symbols, solve
x, y=symbols("x, y")
u1=2*x-y-3
u2=x+y-7

D=solve([u1, u2])
print(D)