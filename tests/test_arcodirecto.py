import unittest
import types
from src.arcodirecto import ArcoDirecto

class TestArcoDirecto(unittest.TestCase):
    def test_capacidad_recien_creado(self):
        arco1 = ArcoDirecto(3)
        arco2 = ArcoDirecto(34)

        self.assertEqual(arco1.capacidad(),3)
        self.assertEqual(arco2.capacidad(),34)

    def test_valor_recien_creado(self):
        arco1 = ArcoDirecto(7)
        arco2 = ArcoDirecto(8,flujo=2)

        self.assertEqual(arco1.valor(),7)
        self.assertEqual(arco2.valor(),6)
        self.assertEqual(arco2.capacidad(),8)

    def test_valor_recien_creado_supera_capacidad(self):
        self.assertRaises(Exception,ArcoDirecto,10,11)

    def test_valor_recien_creado_iguala_capacidad(self):
        arco = ArcoDirecto(10,10)
        self.assertEqual(arco.capacidad(),10)
        self.assertEqual(arco.valor(),0)
        
    def test_inverso_recien_creado(self):
        arco1 = ArcoDirecto(4)
        arco2 = ArcoDirecto(5)
        inverso1 = arco1.inverso()
        inverso2 = arco2.inverso()

        self.assertIsNotNone(inverso1)
        self.assertIsNotNone(inverso2)
        self.assertIsNot(inverso1, arco1)
        self.assertIsNot(inverso2, arco2)
        self.assertIsNot(inverso1, inverso2)

    def test_inverso_recreado_es_el_mismo(self):
        arco = ArcoDirecto(4)
        inverso1 = arco.inverso()
        inverso2 = arco.inverso()
        self.assertIs(inverso1, inverso2)

    def test_capacidad_inverso_recien_creado(self):
        inverso1 = ArcoDirecto(3)
        inverso2 = ArcoDirecto(34)

        self.assertEqual(inverso1.capacidad(),3)
        self.assertEqual(inverso2.capacidad(),34)

    def test_valor_inverso_recien_creado(self):
        inverso1 = ArcoDirecto(7).inverso()
        inverso2 = ArcoDirecto(9,flujo=2).inverso()
        self.assertEqual(inverso1.valor(),0)
        self.assertEqual(inverso2.valor(),2)
        self.assertEqual(inverso2.capacidad(),9)

    def test_aumentar_recien_creado_sin_flujo(self):
        arco = ArcoDirecto(6)
        inverso = arco.inverso()
        arco.aumentar(5)
        self.assertEqual(arco.valor(),1)
        self.assertEqual(inverso.valor(),5)
        self.assertEqual(arco.capacidad(),6)
        self.assertEqual(inverso.capacidad(),6)

    def test_aumentar_recien_creado_con_flujo(self):
        arco = ArcoDirecto(13,flujo=2)
        inverso = arco.inverso()
        arco.aumentar(10)
        self.assertEqual(arco.valor(),1)
        self.assertEqual(inverso.valor(),12)
        self.assertEqual(arco.capacidad(),13)
        self.assertEqual(inverso.capacidad(),13)

    def test_aumentar_recien_creado_al_limite(self):
        arco = ArcoDirecto(11,flujo=2)
        inverso = arco.inverso()
        arco.aumentar(9)
        self.assertEqual(arco.valor(),0)
        self.assertEqual(inverso.valor(),11)
        self.assertEqual(arco.capacidad(),11)
        self.assertEqual(inverso.capacidad(),11)

    def test_aumentar_recien_creado_pasando_limite(self):
        arco = ArcoDirecto(11,flujo=2)
        inverso = arco.inverso()
        self.assertRaises(Exception,arco.aumentar,10)

    def test_aumentar_ya_aumentado_al_limite(self):
        arco = ArcoDirecto(14,flujo=3)
        inverso = arco.inverso()
        arco.aumentar(4)
        arco.aumentar(7)
        self.assertEqual(arco.valor(),0)
        self.assertEqual(inverso.valor(),14)
        self.assertEqual(arco.capacidad(),14)
        self.assertEqual(inverso.capacidad(),14)

    def test_aumentar_ya_aumentado_pasando_limite(self):
        arco = ArcoDirecto(10,flujo=3)
        inverso = arco.inverso()
        arco.aumentar(4)
        self.assertRaises(Exception,arco.aumentar,4)

    def test_aumentar_inverso_recien_creado_sin_flujo(self):
        arco = ArcoDirecto(6)
        inverso = arco.inverso()
        self.assertRaises(Exception,inverso.aumentar,1)

    def test_aumentar_inverso_recien_creado_con_flujo(self):
        arco = ArcoDirecto(13,flujo=9)
        inverso = arco.inverso()
        inverso.aumentar(8)
        self.assertEqual(arco.valor(),12)
        self.assertEqual(inverso.valor(),1)

    def test_aumentar_inverso_recien_creado_al_limite(self):
        arco = ArcoDirecto(11,flujo=2)
        inverso = arco.inverso()
        inverso.aumentar(2)
        self.assertEqual(arco.valor(),11)
        self.assertEqual(inverso.valor(),0)
        self.assertEqual(arco.capacidad(),11)
        self.assertEqual(inverso.capacidad(),11)

    def test_aumentar_inverso_ya_aumentado_al_limite(self):
        arco = ArcoDirecto(14,flujo=11)
        inverso = arco.inverso()
        inverso.aumentar(4)
        inverso.aumentar(7)
        self.assertEqual(arco.valor(),14)
        self.assertEqual(inverso.valor(),0)
        self.assertEqual(arco.capacidad(),14)
        self.assertEqual(inverso.capacidad(),14)

    def test_aumentar_inverso_ya_aumentado_pasando_limite(self):
        arco = ArcoDirecto(10,flujo=7)
        inverso = arco.inverso()
        inverso.aumentar(4)
        self.assertRaises(Exception,inverso.aumentar,4)

    def test_aumentar_negativo_sin_pasar_limite(self):
        arco = ArcoDirecto(10,flujo=7)
        arco.aumentar(-7)
        self.assertEqual(arco.valor(),10)
        self.assertEqual(arco.inverso().valor(),0)
        self.assertEqual(arco.capacidad(),10)

if __name__ == '__main__':
    unittest.main()
