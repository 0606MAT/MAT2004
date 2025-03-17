import matplotlib.pyplot as plt

X=[1, 2, 3, 4, 5, 6]
Y1=[5, 3, 4, 6, 5, 1]
Y2=[1, 4, 5, 3, 4, 3]
plt.plot(X, Y1, label="Klasse A")
plt.plot(X, Y2, label="Klasse B")
plt.xlabel("Karakterer")
plt.ylabel("antall")
plt.title("Karakterfordelingen til to klasser")
plt.ylim(0, 6) #Vil ha y-verdiene fra 0 til 6
plt.grid()
plt.legend()
plt.show()
