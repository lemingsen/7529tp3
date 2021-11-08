import unittest
import types
from src.grafosimple import GrafoSimple
from src.flujo import Flujo

class TestGrafoSimple(unittest.TestCase):
    def test_vacio(self):
        grafo = GrafoSimple()
        Flujo.convertir(grafo)
        self.assertEqual(0,grafo.cantidadNodos())
        self.assertEqual(0,grafo.cantidadArcos())
        self.assertEqual(0,len(list(grafo.arcos())))

if __name__ == '__main__':
    unittest.main()
