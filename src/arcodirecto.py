class ArcoInverso:
    def __init__(self,directo):
        self._directo = directo

    def capacidad(self):
        return self._directo.capacidad()

    def valor(self):
        """En caso de un arco inverso, el valor disponible es el flujo (capacidad - valor directo)"""
        return self._directo.capacidad() - self._directo.valor()

    def aumentar(self,cantidad):
        if 0 == self.valor():
            raise Exception()
        self._directo.aumentar(-cantidad)

class ArcoDirecto:
    def __init__(self,capacidad,flujo=0):
        if(flujo>capacidad):
            raise Exception("El flujo supera a la capacidad")
        self._capacidad = capacidad
        self._flujo = flujo
        self._inverso = ArcoInverso(self)

    def aumentar(self,cantidad):
        if(cantidad > self.valor()):
            raise Exception("No se puede superar la capacidad")
        self._flujo += cantidad

    def capacidad(self):
        return self._capacidad

    def inverso(self):
        return self._inverso

    def valor(self):
        """En caso de un arco directo, el valor disponible es el residuo (capacidad - flujo)"""
        return self._capacidad - self._flujo