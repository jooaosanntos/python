import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global decifra
        undertest = __import__(module)
        decifra = getattr(undertest, 'decifra', None)

    def test_1(self):
        chave1={'@':'V','a':'v','n':'o','l':'i','#':' ','4':'a','+':'u'}
        assert decifra( chave1, '+a4') == 'uva'
        assert decifra(chave1, '@nan#al+#4#+a4') == 'Vovo viu a uva'

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
