import sys

class Vuelos:
    def __init__(self,args):
        if 1 != len(args):
            self.imprimirAyuda()

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

if "__main__" == __name__:
    Vuelos(sys.argv[1:])