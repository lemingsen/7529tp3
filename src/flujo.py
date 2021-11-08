class Flujo:
    def __init(self):
        pass

    @staticmethod
    def convertir(grafo):
        inversos = []
        def transformar(desde,hasta,peso):
            inversos.append( (hasta,desde,peso) )
            return peso

        grafo.modificarPesos(transformar)
        for (desde,hasta,arco_inverso) in inversos:
            grafo.insertarArcoConAlias("B","A",arco_inverso)
        pass