import math
class set:
    def __init__(self, size):
        self.frange = size
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        self.panX = -2.0
        self.panY = -2.0
        self.coloradj = {'base': 0.95, 'multiplier': 5}
        triPoints = [size/3, size/3, 2*size/3, 2*size/3, 3*size/3, size/3]
        triPoints[2],triPoints[3] = self.findThirdPoint(triPoints[0],triPoints[1],triPoints[4],triPoints[5])
        self.drawTriangle(triPoints)
        self.generate(triPoints)

    def isMember(self, x, y):
        # self.frange should be useful
        smoothColor = 1
        if (self.matrix[x][y]):
            return True, smoothColor
        else:
            return False, None

    def generate(self, triPoints): #divide size by 3 each time, send to checkthird
        self.replaceLine(triPoints[0],triPoints[1],triPoints[2],triPoints[3])
        self.replaceLine(triPoints[4],triPoints[5],triPoints[0],triPoints[1])
        self.replaceLine(triPoints[2],triPoints[3],triPoints[4],triPoints[5])

    def replaceLine(self, Ax, Ay, Bx, By):

        middle = range(4)
        peak = range(2)
        
        middle [0] = Ax + (Bx-Ax)/3
        middle [1] = Ay + (By-Ay)/3
        middle [2] = Ax + 2*(Bx-Ax)/3
        middle [3] = Ay + 2*(By-Ay)/3

        peak[0],peak[1] = self.findThirdPoint(middle[0],middle[1],middle[2],middle[3])

        self.removeLine(Ax,Ay,Bx,By)

        self.drawLine(Ax,Ay,middle[0],middle[1], False)
        self.drawLine(middle[0],middle[1],peak[0],peak[1],False)
        self.drawLine(middle[2],middle[3],peak[0],peak[1],False)
        self.drawLine(middle[2],middle[3],Bx, By, False)
        
        return middle,peak
    
# Use a 2D rotation matrix to determine the third point from A and B, rotating anticlockwise by 60 degrees
    def findThirdPoint(self, Ax, Ay, Bx, By):
        # We'll not bother with the trig every time
        cosSixty = 0.5
        sinSixty = math.sqrt(3)/2

        deltaX = (Bx - Ax) * cosSixty + (Ay - By) * sinSixty
        deltaY = (Bx - Ax) * sinSixty + (By - Ay) * cosSixty

        Cx = Ax + deltaX
        Cy = Ay + deltaY

        return [Cx, Cy]

    def removeLine(self, x1, y1, x2, y2):
        self.drawLine(x1, y1, x2, y2, True)

    def drawTriangle(self, triPoints):
        self.drawLine(triPoints[0], triPoints[1], triPoints[2], triPoints[3], False)
        self.drawLine(triPoints[2], triPoints[3], triPoints[4], triPoints[5], False)
        self.drawLine(triPoints[4], triPoints[5], triPoints[0], triPoints[1], False)

    def drawLine(self, startX, startY, endX, endY, remove):
        # In case we pass in non-integral pixels
        startX=int(startX)
        startY=int(startY)
        endX=int(endX)
        endY=int(endY)
        if endX==startX:
            self.drawVerticalLine(startX, startY, endY)

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
            self.setPixel(startX, y)

    def setPixel(self,x,y, remove):
        if (remove):
            self.matrix[x][y] = 0
        else:
            self.matrix[x][y] = 1
