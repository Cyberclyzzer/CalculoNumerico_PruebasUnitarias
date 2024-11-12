import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Definir el rango de valores x
x = np.linspace(-1, 1, 400)

# Calcular y graficar los primeros 5 polinomios de Legendre
for n in range(5):
    Pn = legendre(n)
    plt.plot(x, Pn(x), label=f'P_{n}(x)')

plt.xlabel('x')
plt.ylabel('P_n(x)')
plt.title('Polinomios de Legendre')
plt.legend()
plt.grid(True)
plt.show()
