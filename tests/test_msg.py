import unittest
from pyPackageEx import manSetGen as msg
from numpy import linspace, meshgrid, ndarray

class test_set_generation(unittest.TestCase):

    def setUp(self):
        X = linspace(-2,2,4)
        x, y = meshgrid(X, X)
        self.z = x + 1j*y

    def test_mandelbrot(self):
        self.assertIsInstance(msg.mandelbrot(self.z), ndarray)

    def test_f(self):
        self.assertIsInstance(msg.func(0j, self.z), ndarray)

if __name__ == "__main__":
    unittest.main()
