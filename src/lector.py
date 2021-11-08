from src.grafosimple import GrafoSimple

class Lector:
    def __init__(self, nombreArchivo,verbose=False):
        self._verbose = verbose
        with open(nombreArchivo, "r") as archivo:
            if self._verbose:
                print("\nArchivo: ",nombreArchivo)
            self.desde = Lector.lineaANombre(archivo.readline(), "origen", 1)
            self.hasta = Lector.lineaANombre(archivo.readline(), "destino", 1)
            self.grafo = GrafoSimple()
            self._lineas = 0
            lineas = self._iterLineas(archivo)
            entradas = (self._parsear(linea) for linea in lineas if linea)
            for entrada in entradas:
                if entrada:
                    self.grafo.insertarArcoConAlias(entrada[0], entrada[1], int(entrada[2]))
        if None == self.grafo.idDeNodoAlias(self.desde, crear=False):
            raise Exception("El origen "+str(self.desde)+" no se encuentra en el archivo "+nombreArchivo)
        if None == self.grafo.idDeNodoAlias(self.hasta, crear=False):
            raise Exception("El destino "+str(self.hasta)+" no se encuentra en el archivo "+nombreArchivo)

    def _iterLineas(self,archivo):
        while True:
            leido = archivo.readline()
            self._lineas += 1
            if not leido:
                return
            linea = leido.strip() if leido else None
            if linea:
                if self._verbose:
                    print(" Línea ",self._lineas,": ",linea)
                yield linea
            else:
                if self._verbose:
                    print(" Ignorando leído ",self._lineas,":", leido)

    def _parsear(self,linea):
        campos = linea.split(',')
        cantidad = len(campos) if campos else 0
        if not cantidad:
            if self._verbose:
                print("  Ignorando campos en línea ",self._lineas,": ",linea)
            return None
        if 3 != cantidad:
            raise Exception("La cantidad de campos es incorreta en línea ",self._lineas,", deben ser 3 hay "+str(cantidad))
        entrada = list(map(lambda campo: campo.strip(), campos))

        if self._verbose:
            print("Entrada: ",entrada)
        return entrada

    @staticmethod
    def lineaANombre(texto,campo=None,num_linea=None):
        texto = texto.strip() if texto else texto
        texto_linea = " en la línea "+str(num_linea) if num_linea else ""
        if not texto:
            texto_campo = "un texto" if not campo else campo
            raise Exception("se esperaba "+texto_campo+texto_linea)
        campos = texto.split(',')
        if(len(campos)!=1):
            texto_campo = " para " + campo if campo else ""
            raise Exception("se esperaba un solo campo"+texto_campo+texto_linea)
        return campos[0]
