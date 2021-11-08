import unittest
import types
from src.grafosimple import GrafoSimple

class TestGrafoSimple(unittest.TestCase):
    def test_vacio(self):
        grafo = GrafoSimple()
        self.assertEqual(0,grafo.cantidadNodos())
        self.assertEqual(0,grafo.cantidadArcos())
        self.assertEqual(0,len(list(grafo.arcos())))

    def test_AB10_cantidad(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",10)
        self.assertEqual(2,grafo.cantidadNodos())
        self.assertEqual(1,grafo.cantidadArcos())
        self.assertEqual(1,len(list(grafo.arcos())))

    def test_AB10_nodos(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",10)
        self.assertEqual(grafo.idDeNodoAlias("A"),0)
        self.assertEqual(grafo.idDeNodoAlias("B"),1)

    def test_AB10_arcos(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",10)
        self.assertEqual(list(grafo.arcos()),[(0,1,10)])

    def test_idDeNodoAliasNoExistente(self):
        grafo = GrafoSimple()
        self.assertRaises(Exception,grafo.idDeNodoAlias,"A")
        self.assertEqual(grafo.idDeNodoAlias("A",crear=True),0)

    def test_AB10_adyctentes(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",10)
        self.assertEqual(list(grafo.arcoDesdeNodoId(0)), [(1,10)])
        self.assertEqual(list(grafo.arcoDesdeNodoId(1)), [])
        self.assertRaises(Exception, grafo.arcoDesdeNodoId, 2)
        self.assertRaises(Exception, grafo.arcoDesdeNodoId, -1)

    def test_arcoDesdeNodoId_es_generador(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",10)
        adyacentes = grafo.arcoDesdeNodoId(0)
        self.assertTrue(isinstance(adyacentes, types.GeneratorType))

    def test_arcos_es_generador(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",10)
        arcos = grafo.arcos()
        self.assertTrue(isinstance(arcos, types.GeneratorType))

    def test_BA5(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("B","A",5)
        self.assertEqual(2,grafo.cantidadNodos())
        self.assertEqual(1,grafo.cantidadArcos())
        self.assertEqual(grafo.idDeNodoAlias("B"),0)
        self.assertEqual(grafo.idDeNodoAlias("A"),1)
        self.assertEqual(list(grafo.arcoDesdeNodoId(0)), [(1,5)])
        self.assertEqual(list(grafo.arcoDesdeNodoId(1)), [])
        self.assertEqual(list(grafo.arcos()),[(0,1,5)])

    def test_AB9BA5(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",9)
        grafo.insertarArcoConAlias("B","A",5)
        self.assertEqual(2,grafo.cantidadNodos())
        self.assertEqual(2,grafo.cantidadArcos())
        self.assertEqual(grafo.idDeNodoAlias("A"),0)
        self.assertEqual(grafo.idDeNodoAlias("B"),1)
        self.assertEqual(list(grafo.arcoDesdeNodoId(0)), [(1,9)])
        self.assertEqual(list(grafo.arcoDesdeNodoId(1)), [(0,5)])
        self.assertEqual(list(grafo.arcos()),[(0,1,9),(1,0,5)])

    def test_Ax10xA20_siendo_x_objeto(self):
        grafo = GrafoSimple()
        x = object()
        grafo.insertarArcoConAlias("A",x,10)
        grafo.insertarArcoConAlias(x,"A",20)
        self.assertEqual(2,grafo.cantidadNodos())
        self.assertEqual(2,grafo.cantidadArcos())
        self.assertEqual(grafo.idDeNodoAlias("A"),0)
        self.assertEqual(grafo.idDeNodoAlias(x),1)
        self.assertEqual(list(grafo.arcoDesdeNodoId(0)), [(1,10)])
        self.assertEqual(list(grafo.arcoDesdeNodoId(1)), [(0,20)])
        self.assertEqual(list(grafo.arcos()),[(0,1,10),(1,0,20)])

    def test_modificar_pesos_a_0(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",-2)
        grafo.insertarArcoConAlias("C","D",-2)
        grafo.insertarArcoConAlias("A","D",-1)
        grafo.insertarArcoConAlias("B","C",5)
        grafo.insertarArcoConAlias("D","B",-3)
        grafo.modificarPesos( lambda w,u,v: 0 )
        self.assertEqual(list(grafo.arcoDesdeNodoId(0)), [(1,0), (3,0)])
        self.assertEqual(list(grafo.arcoDesdeNodoId(1)), [(2,0)])
        self.assertEqual(list(grafo.arcoDesdeNodoId(2)), [(3,0)])
        self.assertEqual(list(grafo.arcoDesdeNodoId(3)), [(1,0)])

    def test_modificar_pesos_a_formula(self):
        grafo = GrafoSimple()
        grafo.insertarArcoConAlias("A","B",-2)
        grafo.insertarArcoConAlias("C","D",-2)
        grafo.insertarArcoConAlias("A","D",-1)
        grafo.insertarArcoConAlias("B","C",5)
        grafo.insertarArcoConAlias("D","B",-3)
        grafo.modificarPesos( lambda w,u,v: 100+w+100*u+20*v )
        self.assertEqual(list(grafo.arcoDesdeNodoId(0)), [(1,118), (3,159)])
        self.assertEqual(list(grafo.arcoDesdeNodoId(1)), [(2,245)])
        self.assertEqual(list(grafo.arcoDesdeNodoId(2)), [(3,358)])
        self.assertEqual(list(grafo.arcoDesdeNodoId(3)), [(1,417)])

    def test_alias(self):
        grafo = GrafoSimple()
        x = object()
        grafo.insertarArcoConAlias("A","B",-2)
        grafo.insertarArcoConAlias(-1,3,-1)
        grafo.insertarArcoConAlias(x,"Un texto largo",0)
        alias = grafo.alias()
        self.assertTrue(isinstance(alias, types.GeneratorType))
        self.assertEqual(list(alias), ["A","B",-1,3,x,"Un texto largo"])
        self.assertEqual(grafo.alias(id=0),"A")
        self.assertEqual(grafo.alias(id=1),"B")
        self.assertEqual(grafo.alias(id=2),-1)
        self.assertEqual(grafo.alias(id=3),3)
        self.assertEqual(grafo.alias(id=4),x)
        self.assertEqual(grafo.alias(id=5),"Un texto largo")
        with self.assertRaises(Exception) as contexto:
            grafo.alias(id=6)
        with self.assertRaises(Exception) as contexto:
            grafo.alias(id=-1)

if __name__ == '__main__':
    unittest.main()