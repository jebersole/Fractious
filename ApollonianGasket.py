import math
import Complex
#from ApollonianGasket import circle
class set:
    def __init__(self, size):
        self.panX = -2.0
        self.panY = -2.0
        self.coloradj = {'base': 0.95, 'multiplier': 5}
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        size = size/3
        # draw three kissing circles of equal radius
        c1 = circle(170 - size/2, 170, size/2, "blue")
        c2 = circle(170 + size/2, 170, size/2, "blue")
        c3y = self.getY(170 + size/2, 170, 170, size/2, size/2)
        c3 = circle(170, c3y, size/2, "blue")
        for item in [c1, c2, c3]: self.drawCircle(item)
        # smaller circle between the three
        k = 1.0/c3.r
        r = int(round(1.0/(self.getK(k, k, k, True))))
        innerCoords = self.getXY(c1.z.r, c1.z.i, c2.z.r, c2.z.i, c3.z.r, c3.z.i, c3.r, -r)
        inner = circle(innerCoords[0], innerCoords[1], r, "blue")
        self.drawCircle(inner)
        # outer, largest circle
        k2 = self.getK(k,k,k,False)
        outer = circle(inner.z.r, inner.z.i, -int(round(1.0/k2)), "blue")
        self.drawCircle(outer)
        # medium-sized circle between biggest circle and two of original 3 kissing circles
        k3 = self.getK(k,k,k2,True)
        mediumCoords = self.getXY(c1.z.r, c1.z.i, c3.z.r, c3.z.i, outer.z.r, outer.z.i, outer.z.r, int(round(1.0/k3)))
        medium = circle(mediumCoords[0], mediumCoords[1], int(round(1.0/k3)), "blue")
        self.drawCircle(medium)

    def getY(self, x1, y1, x2, r1, r2):
        y2 = math.sqrt((r1 + r2)**2 - (x1 - x2)**2) - y1
        y2 = int(round(y2 * -1))
        return y2

    def getXY(self, sX1, sY1, sX2, sY2, bX, bY, bR, newR):
        # this function will return x,y coordinates for
        # the centre of a circle which is located between
        # two smaller circles and the edge of a larger one
        # s* are the centres of the smaller circles
        # b* are the coords and radius of the big one
        # the newR of the circle is calculated elsewhere

        midX = (sX1 + sX2)/2.0 # find the midpoint between the two circles
        midY = (sY1 + sY2)/2.0 # the new centre will lie on the line
                               # between that and the big centre

        deltaX = midX-bX       # find the direction from big centre
        deltaY = midY-bY

        scale = 1/math.sqrt(deltaX**2 + deltaY**2) # normalise that vector

        deltaX = deltaX * scale # make the length one
        deltaY = deltaY * scale # so that we can multiply it later

        distance = bR - newR # how far is the new centre from the big centre?

        newX = bX + (distance * deltaX)
        newY = bY + (distance * deltaY)

        return newX,newY

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
        x0 = circle.z.r
        y0 = circle.z.i
        r = circle.r
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
    def __init__(self, x, y, r, color):
        self.z = Complex.Number(x, y)
        self.r = r
        self.color = color
