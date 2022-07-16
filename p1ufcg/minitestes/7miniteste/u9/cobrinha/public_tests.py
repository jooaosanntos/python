import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global cobrinha
        undertest = __import__(module)
        cobrinha = getattr(undertest, 'cobrinha', None)

    def test_simples(self):
        M = [[1,2,3],[4,5,6],[7,8,9]]
        assert cobrinha(M) == [1, 3, 5, 7, 9]

        M = [[1,4],[3,1],[2,7],[0,9]]
        assert cobrinha(M) == [1, 1, 3, 7, 9]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
