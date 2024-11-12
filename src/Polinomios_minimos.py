import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Datos de ejemplo
data = pd.read_csv("src/minimos.csv")  

def Calcular_poli_minimos(x,y):
    coeficientes = np.polyfit(x, y, 2)
    polinomio = np.poly1d(coeficientes)
    return polinomio 

# Extraer las columnas x e y del DataFrame
x = data['x'].values
y = data['y'].values

# Generar valores para la gráfica
x_vals = np.linspace(0, 4, 100)
polinomio = Calcular_poli_minimos(x,y) 
y_fit = polinomio(x_vals)

# Graficar los datos 
plt.scatter(x, y, label='Datos')
plt.plot(x_vals, y_fit, label='Ajuste polinómico', color='red')
plt.legend()
plt.show()
