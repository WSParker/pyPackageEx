from pyPackageEx import coords
from numpy import ndarray
import unittest

class test_coordinate_gen(unittest.TestCase):

    def setUp(self):
        self.output = coords.cp(xres=4, yres=4)

    def test_output_type(self):
        self.assertIsInstance(self.output, ndarray)

    def test_if_output_is_complex_array(self):
        self.assertIsInstance(self.output[0,0], complex)

if __name__ == "__main__":
    unittest.main()
