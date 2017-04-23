import math
import Complex
import cmath

#from ApollonianGasket import circle
class set:
    def __init__(self, size):
        self.panX = -2.0
        self.panY = -2.0
        self.coloradj = {'base': 0.95, 'multiplier': 5}
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        size = size/4
        # draw three kissing circles of equal radius
        c1 = circle(complex(170 - size/2, 170), size/2, "blue")
        c2 = circle(complex(170 + size/2, 170), size/2, "blue")
        c3y = self.getY(170 + size/2, 170, 170, size/2, size/2)
        c3 = circle(complex(170, 170 + size * math.sqrt(3)/2.0), size/2, "blue")
        for item in [c1, c2, c3]: self.drawCircle(item)
        # smaller circle between the three
        inni, outi = self.apollonianCircles(c1,c2,c3)
        self.drawCircle(inni)
        self.drawCircle(outi)
        med1,med2 = self.apollonianCircles(c1,c3,outi)
        self.drawCircle(med1)
        self.drawCircle(med2)

        med3, med4 = self.apollonianCircles(c1,c3,inni)
        self.drawCircle(med3)
        self.drawCircle(med4)

        med5, med6 = self.apollonianCircles(med1,c1,outi)
        self.drawCircle(med5)
        self.drawCircle(med6)
        
    def getY(self, x1, y1, x2, r1, r2):
        y2 = math.sqrt((r1 + r2)**2 - (x1 - x2)**2) - y1
        y2 = int(round(y2 * -1))
        return y2

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

        print k4,k5
        
        zkc1 = self.zk(c1)
        zkc2 = self.zk(c2)
        zkc3 = self.zk(c3)
        
        base = zkc1 + zkc2 + zkc3
        delta = 2.0 * cmath.sqrt(zkc1*zkc2 + zkc2*zkc3 + zkc3*zkc1)

        circle4 = circle((base + delta)/k4, 1.0/k4, "blue")
        circle5 = circle((base - delta)/k5, 1.0/k5, "blue")

        return circle4, circle5

    def isMember(self, x, y):
        # self.frange should be useful
        smoothColor = 1
        if (self.matrix[x][y]):
            return True, smoothColor
        else:
            return False, None


    def setPixel(self, x, y):
        x = int(x)
        y = int(y)
        self.matrix[x][y] = 1

    # From https://en.wikipedia.org/wiki/Midpoint_circle_algorithm
    def drawCircle(self, circle):
        x0 = circle.z.real
        y0 = circle.z.imag
        r = abs(circle.r)
        #circle.color...
        x = r
        y = 0
        err = 0

        while (x >= y):
            self.setPixel(x0 + x, y0 + y)
            self.setPixel(x0 + y, y0 + x)
            self.setPixel(x0 - y, y0 + x)
            self.setPixel(x0 - x, y0 + y)
            self.setPixel(x0 - x, y0 - y)
            self.setPixel(x0 - y, y0 - x)
            self.setPixel(x0 + y, y0 - x)
            self.setPixel(x0 + x, y0 - y)

            if (err <= 0):
                y += 1
                err += 2*y + 1
            if (err > 0):
                x -= 1
                err -= 2*x + 1

    def getK(self, k1, k2, k3, plus):
        if (plus):
            return k1 + k2 + k3 + 2*math.sqrt(k1*k2 + k2*k3 + k3*k1)
        else:
            return k1 + k2 + k3 - 2*math.sqrt(k1*k2 + k2*k3 + k3*k1)

class circle:
    def __init__(self, z, r, color):
        self.z = z
        self.r = r
        self.color = color

    def K(self): # I hope this terrible one-letter function name is OK
        return 1.0/self.r # in context

        
