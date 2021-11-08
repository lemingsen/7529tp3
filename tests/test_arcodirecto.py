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

        self.assertEqual(arco1.valor(),0)
        self.assertEqual(arco2.valor(),2)

    def test_valor_recien_creado_supera_capacidad(self):
        self.assertRaises(Exception,ArcoDirecto,10,11)

if __name__ == '__main__':
    unittest.main()
