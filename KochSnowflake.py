class set:
    def __init__(self, size):
        self.frange = size
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        self.panX = -2.0
        self.panY = -2.0
        self.coloradj = {'base': 0.95, 'multiplier': 5}
        triPoints = [size/3, size/3, 2*size/3, 2*size/3, 3*size/3, size/3]
        self.generate(triPoints)

    def isMember(self, x, y):
        # self.frange should be useful
        smoothColor = 1
        if (self.matrix[x][y]):
            return True, smoothColor
        else:
            return False, None

    def generate(self, triPoints):
        self.drawLine(triPoints[0], triPoints[1], triPoints[2], triPoints[3])
        self.drawLine(triPoints[2], triPoints[3], triPoints[4], triPoints[5])
        self.drawLine(triPoints[4], triPoints[5], triPoints[0], triPoints[1])


    def drawLine(self, startX, startY, endX, endY):
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
                self.setPixel(x, y)
        else: # slope >= 1
            for x in range(startX,endX):
                y = int(round(startX + slope * (x - startX)))
                self.setPixel(x, y)

    def drawVerticalLine(self,startX, startY, endY):
        if endY < startY:
            step = -1
        else:
            step = 1
        for y in range(startY,endY, step):
                self.setPixel(startX, y)

    def setPixel(self,x,y):
        self.matrix[x][y] = 1