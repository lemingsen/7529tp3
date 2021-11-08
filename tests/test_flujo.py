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

    def test_AB10_cantidad(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",10)

        Flujo.convertir(grafo)

        self.assertEqual(2,grafo.cantidadNodos())
        self.assertEqual(2,grafo.cantidadArcos())
        self.assertEqual(2,len(list(grafo.arcos())))

    def test_AB2AC3_cantidad_arcos(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",2)
        grafo.insertarArcoConAlias("A","C",3)
        Flujo.convertir(grafo)
        desde0 = list(grafo.arcoDesdeNodoId(0))
        desde1 = list(grafo.arcoDesdeNodoId(1))
        desde2 = list(grafo.arcoDesdeNodoId(2))

        self.assertEqual(len(desde0), 2)
        self.assertEqual(len(desde1), 1)
        self.assertEqual(len(desde2), 1)
        self.assertEqual(4,grafo.cantidadArcos())
        self.assertEqual(3,grafo.cantidadNodos())

    def test_AB2AC3_arcos_orden(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",2)
        grafo.insertarArcoConAlias("A","C",3)
        Flujo.convertir(grafo)
        AB, AC = list(grafo.arcoDesdeNodoId(0))
        BA = list(grafo.arcoDesdeNodoId(1))[0]
        CA = list(grafo.arcoDesdeNodoId(2))[0]
        self.assertEqual(  AB[0], 1 )
        self.assertEqual(  AC[0], 2 )
        self.assertEqual(  BA[0], 0 )
        self.assertEqual(  CA[0], 0 )

    def test_AB2AC3_arcos_inversos(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",2)
        grafo.insertarArcoConAlias("A","C",3)
        Flujo.convertir(grafo)
        AB, AC = list(grafo.arcoDesdeNodoId(0))
        BA = list(grafo.arcoDesdeNodoId(1))[0]
        CA = list(grafo.arcoDesdeNodoId(2))[0]
        self.assertIs(AB[1].inverso(), BA[1])
        self.assertIs(AC[1].inverso(), CA[1])

    def test_AB2AC3CB1_bfs_existentes(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",2)
        grafo.insertarArcoConAlias("A","C",3)
        grafo.insertarArcoConAlias("C","B",1)
        flujo = Flujo(grafo)
        self.assertEqual( flujo.bfs(0,1), [0,1] )
        self.assertEqual( flujo.bfs(0,2), [0,2] )
        self.assertEqual( flujo.bfs(2,1), [2,1] )

    def test_AB2AC3CB1_bfs_inexistentes(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",2)
        grafo.insertarArcoConAlias("A","C",3)
        grafo.insertarArcoConAlias("C","B",1)
        flujo = Flujo(grafo)
        self.assertEqual( flujo.bfs(1,0), [] )
        self.assertEqual( flujo.bfs(1,2), [] )
        self.assertEqual( flujo.bfs(2,0), [] )

if __name__ == '__main__':
    unittest.main()
