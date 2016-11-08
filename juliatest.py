import unittest
import Complex
import Julia
import math

class JuliaSet(unittest.TestCase):
    # isMember now returns an array, with a boolean in [0] and color data in [1]
    def testZero(self):
        zero = Complex.Number(0,0)
        c = Complex.Number(-0.8,0.156)
        j = Julia.set(c)
        j.iters = 1000
        self.assertFalse(j.isMember(zero)[0])

    def testPointOne(self):
        pointOne = Complex.Number(0.1,0.1)
        c = Complex.Number(-0.8,0.156)
        j = Julia.set(c)
        j.iters = 100
        self.assertTrue(j.isMember(pointOne)[0])

    def testSimpleJulia(self):
        invRootTwo = 1/math.sqrt(2)
        j = Julia.set(Complex.Number(0,0))

        self.assertTrue(j.isMember(Complex.Number(1.0,0))[0])
        self.assertTrue(j.isMember(Complex.Number(0,1))[0])
        self.assertTrue(j.isMember(Complex.Number(0,-1))[0])
        j.iters = 50
        self.assertTrue(j.isMember(Complex.Number(invRootTwo,invRootTwo))[0])

if __name__ == "__main__":
    unittest.main()
