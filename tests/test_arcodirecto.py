import unittest
import types
from src.arcodirecto import ArcoDirecto

class TestArcoDirecto(unittest.TestCase):
    def test_capacidad_recien_creado(self):
        arco = ArcoDirecto(3)
        self.assertEqual(arco.capacidad(),3)

if __name__ == '__main__':
    unittest.main()
