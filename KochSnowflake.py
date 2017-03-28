import math
class set:
    def __init__(self, size):
        self.frange = size
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        self.panX = -2.0
        self.panY = -2.0
        self.coloradj = {'base': 0.95, 'multiplier': 5}

        iterations = 7
        triPoints = [size/3, size/3, 2*size/3, 2*size/3, 3*size/3, size/3]
        triPoints[2],triPoints[3] = self.findThirdPoint(triPoints[0],triPoints[1],triPoints[4],triPoints[5])
        self.generate(triPoints, iterations)

    def isMember(self, x, y):
        # self.frange should be useful
        smoothColor = 1
        if (self.matrix[x][y]):
            return True, smoothColor
        else:
            return False, None

    def generate(self, triPoints, iterations):
        self.iterativeKoch(triPoints[0],triPoints[1],triPoints[2],triPoints[3],iterations)
        self.iterativeKoch(triPoints[2],triPoints[3],triPoints[4],triPoints[5],iterations)
        self.iterativeKoch(triPoints[4],triPoints[5],triPoints[0],triPoints[1],iterations)
        
    def iterativeKoch(self,startX,startY,endX,endY,iters):
        sx = 1.0 * startX
        sy = 1.0 * startY
        ex = 1.0 * endX
        ey = 1.0 * endY

        if iters < 1 :
            self.drawLine(sx,sy,ex,ey,False)
        else:
            iters = iters - 1
            Ax,Ay,Bx,By,Cx,Cy = self.crinkle(sx,sy,ex,ey)
            self.iterativeKoch(sx,sy,Ax,Ay,iters)
            self.iterativeKoch(Ax,Ay,Bx,By,iters)
            self.iterativeKoch(Bx,By,Cx,Cy,iters)
            self.iterativeKoch(Cx,Cy,ex,ey,iters)


    def distance(self,Ax,Ay,Bx,By):
        return math.sqrt((Ax-Bx)**2 + (Ay-By)**2)

# take coordinates for the line ______, return coordinates for the middle of  __/\__
    def crinkle(self, Ax, Ay, Bx, By):
        
        middleAx = Ax + (Bx-Ax)/3
        middleAy = Ay + (By-Ay)/3
        middleBx = Ax + 2*(Bx-Ax)/3
        middleBy = Ay + 2*(By-Ay)/3

        peakX,peakY = self.findThirdPoint(middleAx,middleAy,middleBx,middleBy)
        
        return middleAx, middleAy, peakX, peakY, middleBx, middleBy

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

# Take start and end coordinates of a line, return new end point if you rotate that line widdershins around the start point by $angle in degrees
    def rotateLine(self, Ax, Ay, Bx, By, angle):
        cosine = math.cos(2*math.pi*angle/360)
        sine = math.sin(2*math.pi*angle/360)

        deltaX = (Bx - Ax) * cosine + (Ay - By) * sine
        deltaY = (Bx - Ax) * sine + (By - Ay) * cosine

        Cx = Ax + deltaX
        Cy = Ay + deltaY

        return [Cx, Cy]
                
    def drawLine(self, startX, startY, endX, endY, remove):
        # In case we pass in non-integral pixels
        startX=int(startX)
        startY=int(startY)
        endX=int(endX)
        endY=int(endY)
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
