import pytest
import numpy as np
import pandas as pd
import os
import sys 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from Polinomios_minimos import Calcular_poli_minimos

def test_Calcular_poli_minimos():
    # Datos de prueba
    data = pd.DataFrame({
        'x': [0, 1, 2, 3, 4],
        'y': [1, 3, 7, 13, 21]
    })
    
    # Coeficientes esperados (del polinomio cuadrático)
    coeficientes_esperados = np.polyfit(data['x'].values, data['y'].values, 2)
    
    # Usar la función para obtener el polinomio ajustado
    polinomio = Calcular_poli_minimos(data['x'].values, data['y'].values)
    
    # Verificar que los coeficientes del polinomio son los esperados
    assert np.allclose(polinomio.coefficients, coeficientes_esperados), \
        f"Esperado {coeficientes_esperados}, pero obtuvo {polinomio.coefficients}"

if __name__ == "__main__":
    pytest.main()
