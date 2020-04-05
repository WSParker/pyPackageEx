import unittest
import pyPackageEx as ppe
from pyPackageEx import coords

class test_package_structure(unittest.TestCase):

    def test_ppe_has_mandelbrot(self):
        self.assertTrue(hasattr(ppe, "mandelbrot"))

    def test_ppe_has_coords(self):
        self.assertTrue(hasattr(ppe, "coords"))

    def test_ppe_has_msg(self):
        self.assertTrue(hasattr(ppe, "manSetGen"))

    def test_ppe_has_plot(self):
        self.assertFalse(hasattr(ppe, "plot"))

    def test_ppe_has_cp(self):
        self.assertFalse(hasattr(ppe, "cp"))

if __name__ == "__main__":
    unittest.main()
