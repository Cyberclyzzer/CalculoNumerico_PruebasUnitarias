import pytest
import numpy as np
import pandas as pd
from src.Polinomios_minimos import Calcular_poli_minimos
import Exceptions as error

def test_Calcular_poli_minimos():
    try:
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
        if not np.allclose(polinomio.coefficients, coeficientes_esperados):
            raise error.CoeficienteError(coeficientes_esperados, polinomio.coefficients)
        
    except error.InputInvalidoError as e:
        pytest.fail(f"Error de entrada: {e}")
    except error.Ajustarpolinomioerror as e:
        pytest.fail(f"Error al ajustar el polinomio: {e}")
    except error.CoeficienteError as e:
        pytest.fail(f"Error de coeficientes: {e}")
    except Exception as e:
        pytest.fail(f"Error inesperado: {e}")

if __name__ == "__main__":
    pytest.main()
