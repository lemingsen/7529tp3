class ArcoDirecto:
    def __init__(self,capacidad,flujo=0):
        if(flujo>capacidad):
            raise Exception("El flujo supera a la capacidad")
        self._capacidad = capacidad
        self._flujo = flujo
        self._inverso = {capacidad:0}

    def capacidad(self):
        return self._capacidad

    def inverso(self):
        return self._inverso

    def valor(self):
        """En caso de un arco directo, el valor disponible es el residuo (capacidad - flujo)"""
        return self._capacidad - self._flujo