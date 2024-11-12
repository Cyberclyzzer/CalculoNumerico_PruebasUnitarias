import numpy as np
import pytest
from scipy.special import legendre

def calcular_polinomios_legendre(n, x):
    """
    Calcula los primeros n polinomios de Legendre para un rango de valores x.

    Args:
        n: Número de polinomios de Legendre a calcular.
        x: Array de valores en los que calcular los polinomios.

    Returns:
        Una lista de arrays, donde cada array contiene los valores del polinomio de Legendre correspondiente.
    """
    polinomios = []
    for i in range(n):
        Pn = legendre(i)
        polinomios.append(Pn(x))
    return polinomios

def test_calcular_polinomios_legendre():
    # Datos de prueba
    x = np.linspace(-1, 1, 5)
    n = 5
    
    # Resultados esperados
    esperado = [
        np.ones_like(x),  # P_0(x) = 1
        x,               # P_1(x) = x
        0.5 * (3*x**2 - 1),  # P_2(x) = 0.5 * (3x^2 - 1)
        0.5 * (5*x**3 - 3*x),  # P_3(x) = 0.5 * (5x^3 - 3x)
        (35*x**4 - 30*x**2 + 3) / 8  # P_4(x) = (35x^4 - 30x^2 + 3) / 8
    ]
    
    # Calcular polinomios utilizando la función
    resultado = calcular_polinomios_legendre(n, x)
    
    # Verificar que los resultados coinciden con los valores esperados
    for i in range(n):
        assert np.allclose(resultado[i], esperado[i]), f"Esperado {esperado[i]}, pero obtuvo {resultado[i]}"

if __name__ == "__main__":
    pytest.main()
