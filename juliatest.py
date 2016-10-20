import unittest
import Complex
import Julia
import math

class JuliaSet(unittest.TestCase):
    def testZero(self):
        zero = Complex.Number(0,0)
        c = Complex.Number(-0.8,0.156)
        j = Julia.set(c)

        self.assertFalse(j.isMember(zero))

    def testPointOne(self):
        pointOne = Complex.Number(0.1,0.1)
        c = Complex.Number(-0.8,0.156)
        j = Julia.set(c)

        self.assertTrue(j.isMember(pointOne,100))

    def testSimpleJulia(self):
        invRootTwo = 1/math.sqrt(2)
        j = Julia.set(Complex.Number(0,0))

        self.assertTrue(j.isMember(Complex.Number(1.0,0)))
        self.assertTrue(j.isMember(Complex.Number(0,1)))
        self.assertTrue(j.isMember(Complex.Number(0,-1)))
        self.assertTrue(j.isMember(Complex.Number(invRootTwo,invRootTwo),50))

if __name__ == "__main__":
    unittest.main()

