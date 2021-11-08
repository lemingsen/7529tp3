import sys
from src.lector import Lector
from src.flujo import Flujo

class Vuelos:
    def __init__(self,args):
        if 1 != len(args):
            self.imprimirAyuda()
        try:
            self.procesar(args[0])
            self.imprimir()
        except Exception as ex:
            print("Se produjo un error: "+str(ex))
        return

    def imprimir(self):
        """Imprime el resultado."""
        print("Origen:\t"+self.lector.desde)
        print("Destino:\t"+self.lector.hasta)
        print("Máx. pasajeros:\t"+str(self.pasajeros))
        print("Cant. vuelos:\t"+str(len(self.corte)))
        print("\t"+("DESDE".ljust(15))+"\tHASTA")
        for (desde_id,hasta_id) in self.corte:
            desde = str(self.lector.grafo.alias(id=desde_id)).ljust(15)
            hasta = str(self.lector.grafo.alias(id=hasta_id)).ljust(15)
            print("\t"+desde+"\t"+hasta)
    
    def imprimirAyuda(self):
        margen = "            "
        print("Por favor, ingrese el nombre del archivo a procesar como primer parámetro del script.")
        print("Por ejemplo:")
        print(margen+"python -m src.vuelos tests/entradas/test_diapo3.csv\n\n")
        print("El archivo debe contener:")
        print(" * El nombre de la ruta de origen en la primera línea.")
        print(" * El nombre de la ruta de destino en la segimda línea.")
        print(" * A partir de la tercera línea, una ruta por línea: con origen, destino y costo separados por coma.")
        print("Por ejemplo:\n" + margen+"NQN\n" + margen+"ROS")
        print(margen+"AEP, MDQ, 30\n"+margen+"AEP, COR, 60\n" + margen+"IGR,AEP,120")
        print(margen+"COR,ROS, 30\n" + margen+"MDZ, AEP,70\n" + margen+"NQN,IGR,150")

    def procesar(self,archivo):
        self.lector = Lector(archivo)
        self.flujo = Flujo(self.lector.grafo)
        desde = self.lector.desde_id
        hasta = self.lector.hasta_id
        self.pasajeros = self.flujo.edmonds(desde,hasta)
        A, self.corte, B = self.flujo.corte_actual(desde)
        return

if "__main__" == __name__:
    Vuelos(sys.argv[1:])