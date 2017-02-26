class set:
    def __init__(self, size):
        self.frange = size
        #self.panX = -2.0
        #self.panY = -2.0
        self.coloradj = {'base': 0.95, 'multiplier': 5}

    def isMember(self, x, y):
        # self.frange should be useful
        smoothColor = 1
        if (condition):
            return True, smoothColor
        else:
            return False, None


    def drawLine(self, startX, startY, endX, endY):

        # TODO: actually implement drawVerticalLine
        if endX==startX:
            drawVerticalLine(startX, startY, endY)

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
                x = Math.round(startX + (y - startY)/slope)
                setPixel(x, y)
        else: # slope >= 1
            for x in range(startX,endX):
                y = Math.round(startX + slope * (x - startX))
                setPixel(x, y)
            
    def drawVerticalLine(self,startX, startY, endY):
        if endY < startY:
            step = -1
        else:
            step = 1
        for y in range(startY,endY, step):
                setPixel(startX, y)

    def setPixel(self,x,y):
        self.matrix[x][y] = 1

        
