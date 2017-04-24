import math
import Complex
import cmath
import random

class set:
    def __init__(self, size):
        self.panX = -2.0
        self.panY = -2.0
        self.colors = {0: "red", 1: "orange", 2: "yellow", 3: "green", 4: "blue", 5: "indigo", 6: "violet"}
        self.coloradj = {'base': 0.5, 'multiplier': 5}
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        size = size/4
        sizeAdj = size*2.0
        initShift = size/2.0
        # draw three kissing circles of equal radius
        c1 = circle(complex(sizeAdj - initShift, sizeAdj - initShift/2), initShift)
        c2 = circle(complex(sizeAdj + initShift, sizeAdj - initShift/2), initShift)
        c3 = circle(complex(sizeAdj, sizeAdj - initShift/2 + size * math.sqrt(3.0)/2.0), initShift)
        for item in [c1, c2, c3]: self.drawCircle(item)
        # recursively draw circles, starting with a smaller circle between, or a large, bounding circle
        self.generate(c1, c2, c3, 0)

    def generate(self, c1, c2, c3, level):
        if (level < 7):
            inni, outi = self.apollonianCircles(c1,c2,c3)
            self.drawCircle(inni)
            self.drawCircle(outi)
            self.generate(inni, c1, c2, level + 1)
            self.generate(inni, c1, c3, level + 1)
            self.generate(inni, c2, c3, level + 1)
            self.generate(outi, c1, c2, level + 1)
            self.generate(outi, c1, c3, level + 1)
            self.generate(outi, c2, c3, level + 1)

    def zk(self, circle):
        # this convenience function returns the complex coordinate multiplied by the
        # curvature for the circle
        return circle.z * circle.K()

    def apollonianCircles(self, c1,c2,c3):
        # this function uses Descartes' Complex Theorem to
        # return the two Apollonian circles for three mutually-tangential
        # circles. We don't check that the circles actually are mutually-tangential
        k4 = self.getK(c1.K(),c2.K(),c3.K(), True)
        k5 = self.getK(c1.K(),c2.K(),c3.K(), False)

        zkc1 = self.zk(c1)
        zkc2 = self.zk(c2)
        zkc3 = self.zk(c3)

        base = zkc1 + zkc2 + zkc3
        delta = 2.0 * cmath.sqrt(zkc1*zkc2 + zkc2*zkc3 + zkc3*zkc1)

        circle4 = circle((base + delta)/k4, 1.0/k4)
        circle5 = circle((base - delta)/k5, 1.0/k5)

        return circle4, circle5

    def isMember(self, x, y):
        if (self.matrix[x][y]):
            return True, self.matrix[x][y]
        else:
            return False, None

    def setPixel(self, x, y, color):
        x = int(x)
        y = int(y)
        self.matrix[x][y] = color

    # Modified from https://en.wikipedia.org/wiki/Midpoint_circle_algorithm
    def drawCircle(self, circle):
        x0 = circle.z.real
        y0 = circle.z.imag
        r = abs(circle.r)
        x = r
        y = 0.0
        err = 0.0
        rand = random.randint(0, 6)
        color = self.colors[rand]
        while (x >= y):
            self.setPixel(x0 + x, y0 + y, color)
            self.setPixel(x0 + y, y0 + x, color)
            self.setPixel(x0 - y, y0 + x, color)
            self.setPixel(x0 - x, y0 + y, color)
            self.setPixel(x0 - x, y0 - y, color)
            self.setPixel(x0 - y, y0 - x, color)
            self.setPixel(x0 + y, y0 - x, color)
            self.setPixel(x0 + x, y0 - y, color)

            if (err <= 0):
                y += 1.0
                err += 2.0*y + 1.0
            if (err > 0):
                x -= 1.0
                err -= 2.0*x + 1.0

    def getK(self, k1, k2, k3, plus):
        if (plus):
            return k1 + k2 + k3 + 2.0*math.sqrt(k1*k2 + k2*k3 + k3*k1)
        else:
            return k1 + k2 + k3 - 2.0*math.sqrt(k1*k2 + k2*k3 + k3*k1)

class circle:
    def __init__(self, z, r):
        self.z = z
        self.r = r

    def K(self): # I hope this terrible one-letter function name is OK
        return 1.0/self.r # in context
