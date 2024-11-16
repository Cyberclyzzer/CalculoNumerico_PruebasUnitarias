# exceptions.py

class Ajustarpolinomioerror(Exception):
    def __init__(self, mensaje="Error al calcular el polinomio ajustado"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class InputInvalidoError(Exception):
    def __init__(self, mensaje="Los datos de entrada son inválidos o están mal formateados"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class CoeficienteError(Exception):
    def __init__(self, esperado, actual, mensaje="Los coeficientes calculados no coinciden"):
        self.esperado = esperado
        self.actual = actual
        self.mensaje = mensaje
        super().__init__(f"{self.mensaje}: Esperado {self.esperado}, pero obtuvo {self.actual}")
