import pandas as pd
from scipy.linalg import solve
import pytest
import numpy as np
from src.Resolver_Sistema import resolver_sistema  # Importar la función desde el módulo correcto

def test_resolver_sistema():
    # Caso 1: Sistema resoluble
    data1 = pd.DataFrame({
        'x': [2, -1, 0],
        'y': [1, 3, -1],
        'z': [1, -2, 1],
        'b': [3, 9, -4]
    })
    resultado1 = resolver_sistema(data1)
    assert np.allclose(resultado1, [1.25, 2.25, -1.75]), f"Esperado [1, 2, -1], pero obtuvo {resultado1}"

if __name__ == "__main__":
    pytest.main()

