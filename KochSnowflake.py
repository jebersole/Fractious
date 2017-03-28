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
        self.generate(triPoints, 1)

    def isMember(self, x, y):
        # self.frange should be useful
        smoothColor = 1
        if (self.matrix[x][y]):
            return True, smoothColor
        else:
            return False, None
    def generate(self, triPoints, level):
        self.iterativeKoch(triPoints[0],triPoints[1],triPoints[2],triPoints[3])
        self.iterativeKoch(triPoints[2],triPoints[3],triPoints[4],triPoints[5])
        self.iterativeKoch(triPoints[4],triPoints[5],triPoints[0],triPoints[1])
        
    def Ngenerate(self, triPoints, level): #divide size by 3 each time, send to checkthird
        if (level < 3):
            print(level)
            points1 = self.replaceLine(triPoints[0],triPoints[1],triPoints[2],triPoints[3])
            points2 = self.replaceLine(triPoints[4],triPoints[5],triPoints[0],triPoints[1])
            points3 = self.replaceLine(triPoints[2],triPoints[3],triPoints[4],triPoints[5])

            points4 = self.replaceLine(triPoints[0],triPoints[1], points1[2],points1[3])
            points5 = self.replaceLine(points2[4],points2[5], triPoints[0],triPoints[1])
            points6 = self.replaceLine(triPoints[4],triPoints[5], points2[2],points2[3])
            points7 = self.replaceLine(points3[4],points3[5], triPoints[4],triPoints[5])
            points8 = self.replaceLine(triPoints[2], triPoints[3], points3[2], points3[3])
            points9 = self.replaceLine(points1[4], points1[5], triPoints[2], triPoints[3])

            points10 = self.replaceLine(points1[0],points1[1], points1[4],points1[5])
            points11 = self.replaceLine(points1[2],points1[3], points1[0],points1[1])
            points12 = self.replaceLine(points2[0],points2[1], points2[4],points2[5])
            points13 = self.replaceLine(points2[2],points2[3], points2[0],points2[1])
            points14 = self.replaceLine(points3[0],points3[1], points3[4],points3[5])
            points15 = self.replaceLine(points3[2],points3[3], points3[0],points3[1])

            newPoints = [points1, points2, points3, points4, points5, points6, points7, points8, points9, points10,
                points11, points12, points13, points14, points15]
            for x in range(len(newPoints)):
                peak1 = newPoints[x][0]
                peak2 = newPoints[x][1]
                newPoints[x][0] = newPoints[x][2]
                newPoints[x][1] = newPoints[x][3]
                newPoints[x][2] = peak1
                newPoints[x][3] = peak2
                self.generate(newPoints[x], level + 1)


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

        return [peak[0], peak[1], middle[0], middle[1], middle[2], middle[3]]

    def iterativeKoch(self,startX,startY,endX,endY):
        if (startX-endX)**2 + (startY-endY)**2 < 36:
            self.drawLine(startX,endX,startY,endY,False)
        else:
            Ax,Ay,Bx,By,Cx, Cy = self.crinkle(startX,startY,endX,endY)
            self.iterativeKoch(startX,startY,Ax,Ay)
            self.iterativeKoch(Ax,Ay,Bx,By)
            self.iterativeKoch(Bx,By,Cx,Cy)
            self.iterativeKoch(Cx,Cy,endX,endY)

    def crinkle(self, Ax, Ay, Bx, By):

        # takes coordinates for ______, returns coordinates for __/\__
        middle = range(4)
        peak = range(2)

        middle [0] = Ax + (Bx-Ax)/3
        middle [1] = Ay + (By-Ay)/3
        middle [2] = Ax + 2*(Bx-Ax)/3
        middle [3] = Ay + 2*(By-Ay)/3

        peak[0],peak[1] = self.findThirdPoint(middle[0],middle[1],middle[2],middle[3])
        
        return middle[0], middle[1], peak[0], peak[1], middle[2], middle[3]

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
    
    def rotateLine(self, Ax, Ay, Bx, By, angle):
        cosine = math.cos(2*math.pi*angle/360)
        sine = math.sin(2*math.pi*angle/360)

        deltaX = (Bx - Ax) * cosine + (Ay - By) * sine
        deltaY = (Bx - Ax) * sine + (By - Ay) * cosine

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
