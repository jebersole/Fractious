import unittest
import Complex
import Mandelbrot
import math

class MandelbrotSet(unittest.TestCase):
    # isMember now returns an array, with a boolean in [0] and color data in [1]
    def testBounds(self):
        m = Mandelbrot.set()
        one = Complex.Number(1, 0)
        minusTwo = Complex.Number(-2, 0)
        self.assertFalse(m.isMember(one)[0])
        self.assertFalse(m.isMember(minusTwo)[0])

    def testPointTwo(self):
        m = Mandelbrot.set()
        positive = Complex.Number(0.2, 0.5)
        negative = Complex.Number(-0.2, -0.5)
        self.assertTrue(m.isMember(positive)[0])
        self.assertTrue(m.isMember(negative)[0])

    def testInBounds(self):
        m = Mandelbrot.set()
        zero = Complex.Number(0, 0)
        zeroX = Complex.Number(0.0, -0.3)
        minusOne = Complex.Number(-1.0, 0.0)
        self.assertTrue(m.isMember(zero)[0])
        self.assertTrue(m.isMember(zeroX)[0])
        self.assertTrue(m.isMember(minusOne)[0])

if __name__ == "__main__": # pragma: no cover
    unittest.main()
