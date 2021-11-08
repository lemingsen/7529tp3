from src.grafosimple import GrafoSimple

class Lector:
    def __init__(self, nombreArchivo,verbose=False):
        self._verbose = verbose
        with open(nombreArchivo, "r") as archivo:
            if self._verbose:
                print("\nArchivo: ",nombreArchivo)
            self.desde = Lector.lineaANombre(archivo.readline(), "origen", 1)
            self.hasta = Lector.lineaANombre(archivo.readline(), "destino", 1)

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
