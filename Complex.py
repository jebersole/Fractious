from math import sqrt

class Number:
    def __init__(self,real,imaginary):
        self.r = real
        self.i = imaginary

    def add(self, comp):
        outr = self.r + comp.r
        outi = self.i + comp.i
        return Number(outr,outi)

    def multiply(self, comp):
        outr = (self.r * comp.r) - (self.i * comp.i)
        outi = (self.r * comp.i) + (self.i * comp.r)
        return Number(outr,outi)

    def squared(self):
        return self.multiply(self)

    def magnitude(self):
        return sqrt(self.r * self.r + self.i * self.i)
