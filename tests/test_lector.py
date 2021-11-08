import os
import unittest

from src.lector import Lector

class TestLector(unittest.TestCase):
    def pathArchivo(self, rutaRelativa):
        return os.path.join(os.path.dirname(__file__), rutaRelativa)

    def test_inexistente(self):
        rutaArchivo = self.pathArchivo("entradas/nombre_de_archivo_inexistente.txt")
        self.assertRaises(Exception,Lector,rutaArchivo)

    def test_vacio(self):
        rutaArchivo = self.pathArchivo("entradas/archivo_vacio.txt")
        self.assertRaises(Exception,Lector,rutaArchivo)

    def test_1linea_mala(self):
        rutaArchivo = self.pathArchivo("entradas/test_1linea_mala.txt")
        self.assertRaises(Exception,Lector,rutaArchivo)

    def test_1linea_bien(self):
        rutaArchivo = self.pathArchivo("entradas/test_1linea_bien.txt")
        self.assertRaises(Exception,Lector,rutaArchivo)

    def test_1linea_mala(self):
        rutaArchivo = self.pathArchivo("entradas/test_2linea_mala.txt")
        self.assertRaises(Exception,Lector,rutaArchivo)

    def test_1linea_bien(self):
        rutaArchivo = self.pathArchivo("entradas/test_2linea_bien.txt")
        self.assertRaises(Exception,Lector,rutaArchivo)

    def test_AB10_AB(self):
        rutaArchivo = self.pathArchivo("entradas/test_AB10_AB.txt")
        lector = Lector(rutaArchivo)
        grafo = lector.grafo

        self.assertEqual(lector.desde, "A")
        self.assertEqual(lector.hasta, "B")
        self.assertEqual(2,grafo.cantidadNodos())
        self.assertEqual(1,grafo.cantidadArcos())
        self.assertEqual(1,len(list(grafo.arcos())))
        self.assertEqual(grafo.idDeNodoAlias("A"),0)
        self.assertEqual(grafo.idDeNodoAlias("B"),1)
        self.assertEqual(list(grafo.arcos()),[(0,1,10)])

    def test_AB5_BA(self):
        rutaArchivo = self.pathArchivo("entradas/test_AB5_BA.txt")
        lector = Lector(rutaArchivo)
        grafo = lector.grafo

        self.assertEqual(lector.desde, "B")
        self.assertEqual(lector.hasta, "A")
        self.assertEqual(2,grafo.cantidadNodos())
        self.assertEqual(1,grafo.cantidadArcos())
        self.assertEqual(1,len(list(grafo.arcos())))
        self.assertEqual(grafo.idDeNodoAlias("A"),0)
        self.assertEqual(grafo.idDeNodoAlias("B"),1)
        self.assertEqual(list(grafo.arcos()),[(0,1,5)])

def test_BA_menos5(self):
        rutaArchivo = self.pathArchivo("entradas/test_BA_menos5.txt")
        grafo = Lector(rutaArchivo).grafo

        self.assertEqual(grafo.idDeNodoAlias("B"),0)
        self.assertEqual(grafo.idDeNodoAlias("A"),1)
        self.assertEqual(list(grafo.arcos()),[(0,1,-5)])

if __name__ == '__main__':
    unittest.main()
