class ArcoDirecto:
    def __init__(self,capacidad,flujo=0):
        self._capacidad = capacidad
        self._flujo = flujo

    def capacidad(self):
        return self._capacidad

    def valor(self):
        return self._flujo