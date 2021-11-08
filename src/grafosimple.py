class GrafoSimple:
    def __init__(self):
        self._cantidadNodos = 0
        self._cantidadArcos = 0
        self._listaAlias = dict()
        self._arcosDesdeOrigen = []

    def cantidadNodos(self):
        return self._cantidadNodos

    def cantidadArcos(self):
        return self._cantidadArcos

    def insertarArcoConAlias(self, aliasOrigen, aliasDestino, peso):
        desde = self.idDeNodoAlias(aliasOrigen, crear=True)
        hasta = self.idDeNodoAlias(aliasDestino, crear=True)
        arco = (hasta, peso)
        self._arcosDesdeOrigen[desde].append(arco)
        self._cantidadArcos += 1

    def idDeNodoAlias(self, aliasNodo, crear=False):
        """Devuelve el id del nodo asociado al alias.
        Si no existe lo crea (si crear=True) o eleva una excepción."""
        if aliasNodo in self._listaAlias:
            return self._listaAlias[aliasNodo]

        else:
            if not crear:
                raise Exception("No existe el alias del nodo")
            nuevoId = self._cantidadNodos
            self._cantidadNodos += 1
            self._listaAlias[aliasNodo] = nuevoId
            self._arcosDesdeOrigen.append([])
            return nuevoId

    def arcoDesdeNodoId(self, idOrigen):
        if (idOrigen <0) or (idOrigen >= self.cantidadNodos()):
            raise Exception("El id de origen del nodo no existe")
        return (arco for arco in self._arcosDesdeOrigen[idOrigen])

    def arcos(self):
        return ( (desde,hasta,peso)
                for desde in range(self.cantidadNodos())
                for (hasta,peso) in self._arcosDesdeOrigen[desde] )

    def modificarPesos(self,fnW_WUV):
        self._arcosDesdeOrigen = [
                [  (v, fnW_WUV(w,u,v))  for (v,w) in self._arcosDesdeOrigen[u] ]
                for u in range(self.cantidadNodos()) ]

    def alias(self,id=None):
        lista = self._listaAlias
        if None is id:
            return (alias for alias in lista)
        else:
            return [key for key in lista.keys() if lista[key] == id][0]
        