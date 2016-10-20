import Complex

class set:
    def __init__(self,comp):
        self.c = comp

    def nextIteration(self,z):
# this is defined to do the iteration step z=z²+c
# Before it was doing the calculations manually,
# but that turns out not to be much of an optimisation,
# so why make things harder?
        return z.squared().add(self.c)
    
    def isMember(self,z,steps=255):
# This function puts the number z through a few iterations to see if
# it stays stable or runs away.
        outOfBounds = steps
        for i in xrange(steps):
            z = z.squared().add(self.c)
#            print z.magnitude()
            if (z.magnitude() > 10)|(z.magnitude()==0):
                outOfBounds = i
                break

# If we exceeded the bounds, then outOfBounds was set to the step when
# it happened, so check that and return
        if outOfBounds < steps:
            return False
        else:
            return True

# This returns an int between 0 and 250 suitable for colouring
# a greyscale image. Should probably be refactored and made more general
    def memberness(self,z,steps=25):
        outOfBounds = steps
        for i in xrange(steps):
            z = self.nextIteration(z)
            if (z.i**2 + z.r**2 > 9):
                outOfBounds = i
                break

        return outOfBounds*10
