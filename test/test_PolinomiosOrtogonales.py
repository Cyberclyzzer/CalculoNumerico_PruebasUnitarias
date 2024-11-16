import numpy as np
import pytest
from scipy.special import legendre
import Exceptions as error  

def calcular_polinomios_legendre(n, x):
    """
    Calcula los primeros n polinomios de Legendre para un rango de valores x.

    Args:
        n: Número de polinomios de Legendre a calcular (debe ser un número positivo).
        x: Array de valores en los que calcular los polinomios (debe ser un ndarray).

    Returns:
        Una lista de arrays, donde cada array contiene los valores del polinomio de Legendre correspondiente.

    Raises:
        InputInvalidoError: Si 'n' no es un número entero positivo o 'x' no es un ndarray.
        Ajustarpolinomioerror: Si ocurre un error al calcular los polinomios.
    """
    # Validación de entrada
    if not isinstance(x, np.ndarray):
        raise error.InputInvalidoError(f"El valor de x debe ser un ndarray, pero se recibió {type(x)}.")
    
    if not isinstance(n, int) or n <= 0:
        raise error.InputInvalidoError(f"El valor de n debe ser un entero positivo, pero se recibió {n}.")
    
    polinomios = []
    try:
        # Cálculo de los polinomios de Legendre
        for i in range(n):
            Pn = legendre(i)
            polinomios.append(Pn(x))
    except Exception as e:
        raise error.Ajustarpolinomioerror(f"Error al calcular los polinomios de Legendre: {e}")
    
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

# Ejecutar las pruebas
if __name__ == "__main__":
    pytest.main()
