import matplotlib.pyplot as plt

a=(1,20)
b=(1,20)
plt.plot(a,b)
plt.ylabel(u"Alguns numeros no lado de cima a esquerda")#texto y
plt.xlabel(u"Alguns numeros no lado de baixo ")#texto x
plt.title(u"titulo")#bruh
plt.plot(a, b, 'r', linestyle="--", marker="o")
plt.axis((0,6,0,20))
plt.grid(True)
plt.show()#por ultimo

