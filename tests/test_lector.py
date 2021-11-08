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

        self.assertEqual(lector.desde, "A")
        self.assertEqual(lector.hasta, "B")

if __name__ == '__main__':
    unittest.main()
