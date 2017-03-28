import math
import cmath

class set:
    def __init__(self, size):
        self.frange = size
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        self.panX = -2.0
        self.panY = -2.0
        self.coloradj = {'base': 0.95, 'multiplier': 5}
        size = size - 20
        iterations = 7
        triPoints = [complex(size/3, size/3), complex(2*size/3, 2*size/3), complex(3*size/3, size/3)]
        triPoints[1] = self.findThirdPoint(triPoints[0],triPoints[2])
        self.generate(triPoints, iterations)

    def isMember(self, x, y):
        # self.frange should be useful
        smoothColor = 1
        if (self.matrix[x][y]):
            return True, smoothColor
        else:
            return False, None

    def generate(self, triPoints, iterations):
        for x in range(0,len(triPoints)):
            self.iterativeKoch(triPoints[x],triPoints[(x+1)%len(triPoints)],iterations)
            
    def iterativeKoch(self,start,end,iters):
        if iters < 1 :
            self.drawLine(start,end,False)
        else:
            iters = iters - 1
            A,B,C = self.crinkle(start, end)
            points = [start, A, B, C, end] # this shape: __/\__
            for n in range(0,len(points)-1): # for each sub-line in it
                self.iterativeKoch(points[n],points[n+1],iters)

    def distance(self,A,B):
        return abs(A-B)

# take coordinates for the line A______B, return coordinates for the middle of  __/\__
    def crinkle(self, A, B):
        
        middleNear = A + (B - A)/3
        middleFar = A + 2 * (B - A)/3
        peak = self.findThirdPoint(middleNear,middleFar)
        
        return middleNear, peak, middleFar

# Use a 2D complex rotation to determine the third point from A and B, rotating anticlockwise by 60 degrees
    def findThirdPoint(self, A, B):
        return self.rotateLine(A,B,60)

# Take start and end coordinates of a complex line, return new end point if you rotate that line widdershins around the start point by $angle in degrees
    def rotateLine(self, A, B, angleDeg):
        angleRad = math.pi*angleDeg/180

        delta = (B - A) * cmath.exp(1j * angleRad)
        
        C = A + delta
        
        return C
                
    def drawLine(self, start, end, remove):
        # In case we pass in non-integral pixels
        startX=int(start.real)
        startY=int(start.imag)
        endX=int(end.real)
        endY=int(end.imag)
        if endX==startX:
            self.drawVerticalLine(startX, startY, endY)
            return

        if endX < startX:
            startX, endX = endX,startX
            startY, endY = endY, startY

        slope = (endY * 1.0 - startY)/(endX * 1.0 - startX)

        if slope > 1:
            if endY < startY:
                step = -1
            else:
                step = 1
            for y in range(startY,endY, step):
                x = int(round(startX + (y - startY)/slope))
                if (remove):
                    self.setPixel(x, y, True)
                else:
                    self.setPixel(x, y, False)
        else: # slope >= 1
            for x in range(startX,endX):
                y = int(round(startY + slope * (x - startX)))
                if (remove):
                    self.setPixel(x, y, True)
                else:
                    self.setPixel(x, y, False)

    def drawVerticalLine(self,startX, startY, endY):
        if endY < startY:
            step = -1
        else:
            step = 1
        for y in range(startY,endY, step):
            self.setPixel(startX, y, False)

    def setPixel(self,x,y, remove):
        if (remove):
            self.matrix[x][y] = 0
        else:
            self.matrix[x][y] = 1
