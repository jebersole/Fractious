import Complex
from math import exp

class set:
    # define max iterations, increment per iteration to complex component,
    # fractal range, default camera pan values and color adjustments
    def __init__(self,comp):
        self.frange = 4.0
        self.panX = -2.0
        self.panY = -2.0
        self.iters = 20
        self.coloradj = {'base': 0.95, 'multiplier': 5}
        self.c = comp

    def nextIteration(self,z):
# this is defined to do the iteration step z=z^2+c
# Before it was doing the calculations manually,
# but that turns out not to be much of an optimisation,
# so why make things harder?
        return z.squared().add(self.c)

    def isMember(self,z):
# This function puts the number z through a few iterations to see if
# it stays stable or runs away.
        outOfBounds = self.iters
        smoothColor = exp(-z.r) # piggy-back a smooth coloring algorithm
        for i in xrange(self.iters):
            z = self.nextIteration(z)
            smoothColor += exp(-z.magnitude())
            if (z.magnitude() > 100)|(z.magnitude()==0):
                outOfBounds = i
                break

# If we exceeded the bounds, then outOfBounds was set to the step when
# it happened, so check that and return
        if outOfBounds < self.iters:
            return False, None
        else:
            return True, smoothColor/outOfBounds

# This returns an int between 0 and 250 suitable for colouring
# a greyscale image. Should probably be refactored and made more general
    def memberness(self,z,iters=25):
        outOfBounds = self.iters
        for i in xrange(iters):
            z = self.nextIteration(z)
            if (z.i**2 + z.r**2 > 9):
                outOfBounds = i
                break

        return outOfBounds*10
