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

if __name__ == '__main__':
    unittest.main()
