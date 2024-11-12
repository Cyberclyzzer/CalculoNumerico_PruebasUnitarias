import numpy as np
import pandas as pd
from scipy.linalg import solve
import pytest

data = pd.read_csv("src/resolucion.csv")
# Matriz de rigidez (ejemplo simplificado)
def resolver_sistema(data):
    """Resuelve un sistema de ecuaciones lineales a partir de un DataFrame.

    Args:
        data: DataFrame con las columnas 'x', 'y', 'z' y 'b'.

    Returns:
        Un array con la solución del sistema, o None si la matriz es singular.
    """

    x = data["x"].values
    y = data["y"].values
    z = data["z"].values
    b = data["b"].values

    A = np.array([[x[0], y[0], z[0]],
                 [x[1], y[1], z[1]],
                 [x[2], y[2], z[2]]])

    if A.shape[0] != A.shape[1] or A.shape[0] != b.shape[0]:
        raise ValueError("La matriz A debe ser cuadrada y tener las mismas filas que b")

    try:
        return solve(A, b)
    except np.linalg.LinAlgError:
        print("La matriz A es singular. No se puede resolver el sistema.")
        return None
x = resolver_sistema(data)
