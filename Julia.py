import Complex

class set:
    def __init__(self,comp):
        self.c = comp

    def nextIteration(self,z):
        r = z.r
        i = z.i
        return Complex.Number(r*r - i*i + self.c.r, self.c.i  + 2 * r * i)
    
    def isMember(self,z,steps=255):
        outOfBounds = steps
        for i in xrange(steps):
            z = z.squared().add(self.c)
#            print z.magnitude()
            if (z.magnitude() > 10)|(z.magnitude()==0):
                outOfBounds = i
                break

        if outOfBounds < steps:
            return False
        else:
            return True

    def memberness(self,z,steps=25):
        outOfBounds = steps
        for i in xrange(steps):
            z = self.nextIteration(z)
#            z = z.squared().add(self.c)
#            print z.magnitude()
            if (z.i**2 + z.r**2 > 9):
                outOfBounds = i
                break

        return outOfBounds*10
