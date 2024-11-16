import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
# Leer el CSV
data = pd.read_csv('src/Cubico.csv')


def trazador_cubico_sujeto(x, y):
    trazado = sp.interpolate.CubicSpline(x,y)
    return trazado

x = data["x"].values
y = data["y"].values

f = trazador_cubico_sujeto(x, y)
x_vals = np.linspace(0, 5, 100)
y_eval = f(x_vals)

# Visualizar la curva
#plt.plot(x, y, 'o', label='Puntos de control')
#plt.plot(x_vals, y_eval, label='Trazador cúbico')
#plt.legend()
#plt.show()