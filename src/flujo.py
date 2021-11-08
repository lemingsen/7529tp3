from math import inf
from src.arcodirecto import ArcoDirecto

class ConversorAFlujo:
    def __init__(self,grafo):
        self.inversos = []
        self.grafo = grafo

    def __call__(self,peso,desde,hasta):
        directo = ArcoDirecto(peso)
        arco_inverso = (hasta,desde,directo.inverso())
        self.inversos.append( arco_inverso )
        return directo

    def agregarInversosAGrafo(self):
        for (desde,hasta,inverso) in self.inversos:
            alias_desde = self.grafo.alias(id=desde)
            alias_hasta = self.grafo.alias(id=hasta)
            self.grafo.insertarArcoConAlias(alias_desde,alias_hasta,inverso)

class Flujo:
    def __init__(self,grafo):
        self.grafo = grafo
        Flujo.convertir(grafo)

    @staticmethod
    def convertir(grafo):
        conversor = ConversorAFlujo(grafo)
        grafo.modificarPesos(conversor)
        conversor.agregarInversosAGrafo()
        pass

    def bfs(self,desde,hasta):
        anteriores = self.bfs_datos(desde,hasta)
        if anteriores[hasta] == None:
            return []
        camino = []
        actual = hasta
        while actual != desde:
            camino.insert(0, actual)
            actual = anteriores[actual]
        return camino

    def bfs_datos(self,desde,hasta):
        cantNodos = self.grafo.cantidadNodos()
        anteriores = [None for i in range(cantNodos)]
        siguientes = [desde]
        while len(siguientes) > 0:
            actual = siguientes.pop(0)
            if actual == hasta:
                break
            arcos_gen = self.grafo.arcoDesdeNodoId(actual)
            for u,w in arcos_gen:
                if (anteriores[u] == None) and (w.valor() > 0):
                    anteriores[u] = actual
                    siguientes.append(u)
                    if u == hasta:
                        break

        return anteriores

    def fluir(self,desde,hasta,cantidad):
        arcos=[arco for (u,arco) in self.grafo.arcoDesdeNodoId(desde) if u==hasta]
        return arcos[0].fluir(cantidad)
