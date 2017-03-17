import math
class set:
    def __init__(self, size):
        self.frange = size
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        self.panX = -2.0
        self.panY = -2.0
        self.coloradj = {'base': 0.95, 'multiplier': 5}
        triPoints = [size/3, size/3, 2*size/3, 2*size/3, 3*size/3, size/3]
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
        #for tri in range(0, 3):
        deltaX = (triPoints[2] - triPoints[0])/3
        deltaY = (triPoints[3] - triPoints[1])/3
        temp1 = triPoints[0]
        temp2 = triPoints[1]
        triPointsGen = range(6)
        triPointsGen[0] = triPoints[0] + deltaX
        triPointsGen[1] = triPoints[1] + deltaY
        triPointsGen[4] = triPointsGen[0] + deltaX
        triPointsGen[5] = triPointsGen[1] + deltaY
        #triPointsGen[2] = triPointsGen[0] - (triPointsGen[4] - triPointsGen[0])
        #triPointsGen[3] = triPointsGen[1] + (triPointsGen[5] - triPointsGen[1])
        print(triPointsGen)
        #arr = range(2)
        #arr = self.findThirdPoint(triPointsGen[0], triPointsGen[1], triPointsGen[0] + deltaX/2, triPointsGen[1] + deltaX/2, deltaX * 3)
        triPointsGen[2], triPointsGen[3] = self.findThirdPoint(triPointsGen[0], triPointsGen[1], triPointsGen[0] + deltaX/2, triPointsGen[1] + deltaX/2, deltaX)
        #print(arr)
        #triPointsGen[2] = arr[0]
        #triPointsGen[3] = arr[1]
        print(triPointsGen)
        self.drawTriangle(triPointsGen)
        self.removeLine(temp1 + deltaX, temp2 + deltaY, temp1 + 2*deltaX, temp2 + 2*deltaY)
        deltaX = (triPoints[4] - triPoints[0])/3
        deltaY = (triPoints[5] - triPoints[1])/3
        triPointsGen = range(6)
        triPointsGen[0] = triPoints[0] + deltaX
        triPointsGen[1] = triPoints[1]
        triPointsGen[4] = triPointsGen[0] + deltaX
        triPointsGen[5] = triPointsGen[1]
        triPointsGen[2] = triPointsGen[0] + deltaX/2#(triPointsGen[4] - triPointsGen[0])
        triPointsGen[3] = triPointsGen[1] - deltaX#(triPointsGen[5] - triPointsGen[1])
        print(triPointsGen)
        self.drawTriangle(triPointsGen)
        self.removeLine(temp1 + deltaX, temp2 + deltaY, temp1 + 2*deltaX, temp2 + 2*deltaY)
        deltaX = (triPoints[4] - triPoints[2])/3
        deltaY = abs((triPoints[5] - triPoints[3])/3)
        triPointsGen = range(6)
        triPointsGen[0] = triPoints[2] + deltaX
        triPointsGen[1] = triPoints[3] - deltaY
        triPointsGen[4] = triPointsGen[0] + deltaX
        triPointsGen[5] = triPointsGen[1] - deltaY
        triPointsGen[2] = triPointsGen[0] + deltaX/2#(triPointsGen[4] - triPointsGen[0])/2
        triPointsGen[3] = triPointsGen[1] + deltaY/2#abs((triPointsGen[5] - triPointsGen[1]))/2
        print(triPointsGen)
        self.drawTriangle(triPointsGen)
        self.removeLine(temp1 + deltaX, temp2 + deltaY, temp1 + 2*deltaX, temp2 + 2*deltaY)


    def findThirdPoint(self, firstX, firstY, secondX, secondY, size):
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                if (math.sqrt((x - secondX)**2 + (y - secondY)**2 + (x - firstX)**2 + (y - firstY)**2) > size * 0.99 and
                    math.sqrt((x - secondX)**2 + (y - secondY)**2 + (x - firstX)**2 + (y - firstY)**2) < size * 1.001 ):
                    #print(size, math.sqrt((x - secondX)**2 + (y - secondY)**2 + (x - firstX)**2 + (y - firstY)**2))
                #if ((x - secondX)**2 + (y - secondY)**2 + (x - firstX)**2 + (y - firstY)**2 > size): return [1,2]
                #if (math.sqrt((x - secondX)**2 + (y - secondY)**2 + (x - firstX)**2 + (y - firstY)**2) == size):
                    return [x, y]

    def removeLine(self, x1, y1, x2, y2):
        self.drawLine(x1, y1, x2, y2, True)

    def drawTriangle(self, triPoints):
        self.drawLine(triPoints[0], triPoints[1], triPoints[2], triPoints[3], False)
        self.drawLine(triPoints[2], triPoints[3], triPoints[4], triPoints[5], False)
        self.drawLine(triPoints[4], triPoints[5], triPoints[0], triPoints[1], False)

    def drawLine(self, startX, startY, endX, endY, remove):
        # TODO: actually implement drawVerticalLine
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
