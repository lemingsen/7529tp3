import unittest
import types
from src.arcodirecto import ArcoDirecto

class TestArcoDirecto(unittest.TestCase):
    def test_capacidad_recien_creado(self):
        arco1 = ArcoDirecto(3)
        arco2 = ArcoDirecto(34)

        self.assertEqual(arco1.capacidad(),3)
        self.assertEqual(arco2.capacidad(),34)

if __name__ == '__main__':
    unittest.main()