# Create a Mandelbrot set
from math import log
import Complex

class set:
    # define max iterations, increment per iteration to complex component,
    # fractal range, default camera pan values and color adjustments
    def __init__(self):
        self.frange = 2.0
        self.panX = -1.5
        self.panY = -1.0
        self.iters = 100
        self.incr = 0.0001
        self.coloradj = {'base': 0.95, 'multiplier': 20}

    # returns True and provides coloring if point does not run away
    def isMember(self, point):
        currentIter = 0
        c = Complex.Number(point.r, point.i + self.incr)
        z = Complex.Number(0, 0)
        while ((z.magnitude() < 2.0) and (currentIter < self.iters)):
            z = z.squared().add(c)
            currentIter += 1
        if currentIter < self.iters:
            return False, None
        else:
            return True, self.color(currentIter, z.magnitude())

    # smooth colors
    def color(self, currentIter, mag):
        return currentIter + 1 - abs( log(mag) / log(2) ) / self.iters
