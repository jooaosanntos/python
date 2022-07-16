import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global soma_matrizes_esparsas
        undertest = __import__(module)
        soma_matrizes_esparsas = getattr(undertest, 'soma_matrizes_esparsas', None)

    def test_exemplo(self):
        M1 = (120, 200, {(115, 64): -5})
        M2 = (120, 200, {(20, 55): 5})

        SOMA1 = soma_matrizes_esparsas(M1, M2)
        assert SOMA1 == (120, 200, {(115, 64): -5, (20, 55): 5}), SOMA1


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
