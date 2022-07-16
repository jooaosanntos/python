import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global balanco
        undertest = __import__(module)
        balanco = getattr(undertest, 'balanco', None)

    def test_exemplo(self):
        d1 = {"manteiga": 10, "biscoito": 20, "chocolate": 30}
        d2 = {"manteiga": 10, "gelatina": 40}
        assert balanco(d1, d2) == {"manteiga": 20, "biscoito": 20, "chocolate": 30, "gelatina": 40}
        assert d1 == {"manteiga": 10, "biscoito": 20, "chocolate": 30}
        assert d2 == {"manteiga": 10, "gelatina": 40}

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
