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
        self.assertEqual(lector.desde_id, 1)
        self.assertEqual(lector.hasta_id, 0)

    def test_BA_menos5(self):
        rutaArchivo = self.pathArchivo("entradas/test_BA_menos5.txt")
        lector = Lector(rutaArchivo)
        grafo = lector.grafo

        self.assertEqual(grafo.idDeNodoAlias("B"),0)
        self.assertEqual(grafo.idDeNodoAlias("A"),1)
        self.assertEqual(list(grafo.arcos()),[(0,1,-5)])
        self.assertEqual(lector.desde_id, 1)
        self.assertEqual(lector.hasta_id, 0)

    def test_destino_inexistente(self):
        rutaArchivo = self.pathArchivo("entradas/test_destino_inexistente.txt")
        self.assertRaises(Exception,Lector,rutaArchivo)

    def test_origen_inexistente(self):
        rutaArchivo = self.pathArchivo("entradas/test_origen_inexistente.txt")
        self.assertRaises(Exception,Lector,rutaArchivo)

    def test_diapo3(self):
        """De la diapositva nº 3 «Ford Fulkerson, Paso a paso»"""
        rutaArchivo = self.pathArchivo("entradas/test_diapo3.txt")
        lector = Lector(rutaArchivo)
        grafo = lector.grafo

        self.assertEqual(lector.desde, "s")
        self.assertEqual(lector.hasta, "t")
        self.assertEqual(9,grafo.cantidadNodos())
        self.assertEqual(12,grafo.cantidadArcos())
        self.assertEqual(grafo.idDeNodoAlias("a"),0)
        self.assertEqual(grafo.idDeNodoAlias("b"),1)
        self.assertEqual(grafo.idDeNodoAlias("c"),2)
        self.assertEqual(grafo.idDeNodoAlias("d"),3)
        self.assertEqual(grafo.idDeNodoAlias("e"),4)
        self.assertEqual(grafo.idDeNodoAlias("f"),5)
        self.assertEqual(grafo.idDeNodoAlias("g"),6)
        self.assertEqual(list(grafo.arcos()),[
            (0,1, 5), (0,3,10), (1,8,5), (2,1,5), (2,5,8), (3,2, 2),
            (3,4,10), (4,8,10), (5,6,9), (6,8,8), (7,0,5), (7,2,20)])
        self.assertEqual(lector.desde_id, 7)
        self.assertEqual(lector.hasta_id, 8)
        
if __name__ == '__main__':
    unittest.main()
