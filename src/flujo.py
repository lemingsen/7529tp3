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
        return [desde, hasta]