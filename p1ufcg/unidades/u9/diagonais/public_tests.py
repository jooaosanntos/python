import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
diagonais = getattr(undertest, 'diagonais', None)

class PublicTests(unittest.TestCase):

    def test_1(self):
        M = [[1,2,3], [4,5,6], [7,8,9]]
        assert diagonais(M) == [[1,5,9],[3,5,7]]
   
    
    def test_2(self):
        M = [[]]
        assert diagonais(M) == [[],[]]


    def test_3(self):
        M = [[1]]
        assert diagonais(M) == [[1],[1]]

    
    def test_4(self):
        M = [[1,2], [3,4]]
        assert diagonais(M) == [[1,4],[2,3]]


    def test_5(self):
        M = [[1,1,1], [1,1,1], [1,1,1]]
        assert diagonais(M) == [[1,1,1],[1,1,1]]


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
