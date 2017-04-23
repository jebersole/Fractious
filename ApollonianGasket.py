import math
#import Complex

class set:
    def __init__(self, size):
        self.panX = -2.0
        self.panY = -2.0
        self.coloradj = {'base': 0.95, 'multiplier': 5}
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        size = size/3
        #y = math.sqrt((size/2 + size/2)**2 - (170 + size/2 - 170)**2) - 170
        #y = int(round(y * -1))
        y = self.getY(170 + size/2, 170, 170, size/2, size/2)
        #self.drawCircle(170,170,size,"blue")
        self.drawCircle(170 - size/2, 170, size/2,"blue")
        self.drawCircle(170 + size/2, 170, size/2,"blue")
        self.drawCircle(170, y, size/2,"blue")
        '''
        thirdR = int(round((1/(2/(math.sqrt(size/2))))**2))
        print(thirdR)
        self.drawCircle(170, 170 + 3*thirdR, thirdR,"blue")
        '''
        print(size, size/2, 1.0/(size/2))
        k = 1.0/(size/2)
        #k4 = 3.0*k + 2.0*(math.sqrt(3.0*(k**2.0))) # or -
        k4 = self.getK(k,k,k,True)
        r = int(round(1.0/k4))
        print(k, k4, r)
        y2 = self.getY(170, y, 170, size/2, r)
        self.drawCircle(170, y2 + size + 2*r, r, "blue")
        #k4 = 3.0*k - 2.0*(math.sqrt(3.0*(k**2.0))) # or -
        k5 = self.getK(k,k,k,False)
        r = int(round(1.0/k5)) * -1
        print(k, k5, r)
        #y3 = self.getY(170, y, 170, size/2, -r)
        y3 = self.getY(170 - size/2, 170, 170, size/2, -r)
        self.drawCircle(170, y3, r, "blue")
        #self.generate
        k4 = self.getK(k,k,k,False)
        k6 = self.getK(k,k,k4,True)
        r = int(round(1.0/k6))
        print(k, k6, r)
        #y4 = self.getY(170 - size/2, 170, 170)
        x = self.getX(size/2, size/2)
        y = self.getY(170 - size/2, 170, x, size/2, r)
        x,y = self.getXY(170-size/2,170,x,size/2,size/2,size/2,size,r)
        self.drawCircle(x, y, r, "a")

    def getX(self, r1, r2):
        #x2 = math.sqrt((r1 + r2)**2 - (y1 + y2)**2) - x1
        #x2 = int(round(x2 * -1))
        x3 = (2*r1*(math.sqrt(r2)))/(math.sqrt(r1) + math.sqrt(r2))
        return int(round(x3)) #* -1

    def getY(self, x1, y1, x2, r1, r2):
        #x2 = x2 * -1.0
        print(x1,y1,x2,r1,r2)
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
        

        
    def getK(self, k1, k2, k3, plus):
        if (plus):
            return k1 + k2 + k3 + 2*math.sqrt(k1*k2 + k2*k3 + k3*k1)
        else:
            return k1 + k2 + k3 - 2*math.sqrt(k1*k2 + k2*k3 + k3*k1)

    def isMember(self, x, y):
        # self.frange should be useful
        smoothColor = 1
        if (self.matrix[x][y]):
            return True, smoothColor
        else:
            return False, None

    #def Circle(self, x, y, r, color):
        #return Complex.Number(x, y)

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
        x = int(x)
        y = int(y)
        self.matrix[x][y] = 1
