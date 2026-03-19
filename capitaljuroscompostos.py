import matplotlib.pyplot as plt
capital = 1000
taxa = 0.02
meses = 24
valores = []
for m in range(meses):
    capital = capital * (1 + taxa)
    valores.append(capital)
plt.plot(valores)
plt.title("Crescimento do investimento")
plt.xlabel("Meses")
plt.ylabel("Capital (R$)")
plt.show()