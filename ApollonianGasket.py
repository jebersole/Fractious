import math
import Complex

class set:
    def __init__(self, size):
        self.panX = -2.0
        self.panY = -2.0
        self.coloradj = {'base': 0.95, 'multiplier': 5}
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        size = size/3
        self.drawCircle(150,150,size,"blue")
        self.drawCircle(150 - size/2, 150, size/2,"blue")
        self.drawCircle(150 + size/2, 150, size/2,"blue")
        thirdR = int(round((1/(2/(math.sqrt(size/2))))**2))
        print(thirdR)
        self.drawCircle(150, 150 + 3*thirdR, thirdR,"blue")

    def isMember(self, x, y):
        # self.frange should be useful
        smoothColor = 1
        if (self.matrix[x][y]):
            return True, smoothColor
        else:
            return False, None

    def Circle(self, x, y, r, color):
        return Complex.Number(x, y)

    # From https://en.wikipedia.org/wiki/Midpoint_circle_algorithm
    def drawCircle(self, x0, y0, r, color):
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

    def setPixel(self, x, y):
            self.matrix[x][y] = 1
