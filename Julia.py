import Complex

class set:
    def __init__(self,comp):
        self.c = comp

    def isMember(self,z,steps=1000):
        outOfBounds = steps
        for i in xrange(steps):
            z = z.squared().add(self.c)
            print z.magnitude()
            if (z.magnitude() > 1000)|(z.magnitude()==0):
                outOfBounds = i
                break

        if outOfBounds < steps:
            return False
        else:
            return True

