import io
import re
import os
import subprocess
import sys
import unittest
from math import inf

from src.vuelos import Vuelos

class TestVuelos(unittest.TestCase):
        ################################ AUXILIARES ################################
    def pathArchivo(self, rutaRelativa):
        return os.path.realpath(os.path.join(os.path.dirname(__file__), rutaRelativa))

    def ejecutar(self,argumentos,guardar=True,charset='windows-1252'):
        args = [sys.executable, "-m", "src.vuelos",*argumentos]
        cwd = self.pathArchivo("../")
        self._primera = None
        self._ultima = None

        with subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=None,shell=False,cwd=cwd) as proc:
            primera = proc.stdout.readline().decode(charset)
            if (1 == guardar) or (True is guardar):
                self._primera = primera
            yield primera

            ultima = primera
            while ultima:
                ultima = proc.stdout.readline().decode(charset)
                if not ultima:
                    return
                if (-1 == guardar) or (True is guardar):
                    self._ultima = ultima
                yield ultima

    def lineaCumple(self, lineas, fnTextoEnLinea, verbose=True):
        cumple = any(fnTextoEnLinea(linea) for linea in lineas)
        if verbose and not cumple:
            if self._primera:
                print("Primera: ", self._primera)
            if self._ultima:
                print("Última: ", self._primera)
        return cumple

    def setUp(self):
        self._python = "python"


    ################################ TESTS ################################
    def test_sin_argumentos(self):
        out = self.ejecutar([])

        self.assertTrue(self.lineaCumple(out, lambda txt: ("nombre" in txt) and ("archivo" in txt)))

    def test_inexistente(self):
        rutaArchivo = self.pathArchivo("entradas/nombre_de_archivo_inexistente.txt")
        out = self.ejecutar([rutaArchivo])
        self.assertTrue(self.lineaCumple(out, lambda txt: ("No such" in txt) or ("inexistente" in txt)))


if __name__ == '__main__':
    unittest.main()
