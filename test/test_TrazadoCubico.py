import pytest
import numpy as np
from scipy.interpolate import CubicSpline
import os 
import sys 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from Trazado_Cubico import trazador_cubico_sujeto  

def test_trazador_cubico_sujeto():
    # Datos de prueba
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([0, 1, 0, 1, 0])
    
    # Crear el trazador cúbico esperado
    trazado_esperado = CubicSpline(x, y)
    
    # Usar la función para obtener el trazador cúbico
    trazado_obtenido = trazador_cubico_sujeto(x, y)
    
    # Verificar que ambos objetos CubicSpline son equivalentes en los nodos
    assert np.allclose(trazado_obtenido(x), trazado_esperado(x), atol=1e-8), \
        f"Esperado {trazado_esperado(x)}, pero obtuvo {trazado_obtenido(x)}"
    
    # Verificar que las derivadas son equivalentes
    assert np.allclose(trazado_obtenido(x, 1), trazado_esperado(x, 1), atol=1e-8), \
        f"Esperado {trazado_esperado(x, 1)}, pero obtuvo {trazado_obtenido(x, 1)}"
    

if __name__ == "__main__":
    pytest.main()
