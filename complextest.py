import unittest
import Complex

# Run these tests with: python complextest.py -v
# Before implementing any new functionality in Complex.py,
# first create a test.  Function name must start with "test"
class ComplexArithmetic(unittest.TestCase):
    def testSimpleCreation(self):
        real = 1
        comp = Complex.Number(1,0)
        self.assertEqual(comp.r,real)

    def testSimpleAddition(self):
        real = 1
        expected = real + real
        comp = Complex.Number(real,0)
        output = comp.add(comp)
        self.assertEqual(output.r, expected)
        
    def testSimpleMultiplication(self):
        real = 2
        expected = real*real
        comp = Complex.Number(real,0)
        output = comp.multiply(comp)
        self.assertEqual(output.r, expected)

    def testFractionalAddition(self):
        real = 1.25
        expected = real + real
        comp = Complex.Number(real,0)
        output = comp.add(comp)
        self.assertEqual(output.r, expected)

    def testFractionalMultiplication(self):
        real = 1.5
        expected = real*real
        comp = Complex.Number(real,0)
        output = comp.multiply(comp)
        self.assertEqual(output.r, expected)

    def testComplexAddition(self):
        real = 1
        imag = 1
        expectedr = real + real
        expectedi = imag + imag
        comp = Complex.Number(real,imag)
        output = comp.add(comp)
        self.assertEqual(output.r, expectedr)
        self.assertEqual(output.i, expectedi)
        
    def testComplexMultiplication(self):
        real = 1.5
        imag = 1.5
        expectedr = real*real - imag*imag
        expectedi = real*imag + imag*real
        comp = Complex.Number(real,imag)
        output = comp.multiply(comp)
        self.assertEqual(output.r, -1 * expectedr)
        self.assertEqual(output.i, expectedi)

    def testISquaredIsMinusOne(self):
        expected=-1
        comp = Complex.Number(0,1)
        output = comp.squared()
        self.assertEqual(output.r,expected)

    def testTwoTwoSquared(self):
        real = 2
        imag = 2
        comp = Complex.Number(real,imag)

        expected = Complex.Number(0,8)
        output = comp.squared()

        self.assertEqual(expected.r, output.r)
        self.assertEqual(expected.i, output.i)

    def testMagnitude(self):
        expected = 5
        comp = Complex.Number(3,4)
        self.assertEqual(expected, comp.magnitude())
        
if __name__ == "__main__":
    unittest.main()
