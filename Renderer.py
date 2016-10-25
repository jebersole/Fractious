# Drawing class to create a fractal png

import png
import Complex
import Julia

# Initialize fractal class and png writer
class render:
    def __init__(self, args):
        # Assign parameters from user-provided arguments
        self.xpix = int(args.dimensions[: args.dimensions.index('x')])
        self.ypix = int(args.dimensions[args.dimensions.index('x') + 1:])
        self.xcom = float(args.complex[1: args.complex.index(',')])
        self.ycom = float(args.complex[args.complex.index(',') + 1: -1])

        self.f = open(args.file, 'wb')
        self.c = Complex.Number(self.xcom, self.ycom)
        self.fr = args.fractal.lower()
        self.w = png.Writer(self.xpix, self.ypix, greyscale=True)
        self.pic = [[] for x in xrange(self.ypix)]

    def draw(self):
        # Draw fractal with vertical and horizontal values
        ranges = {'julia': 4.0, 'something': 2.6}
        FRACTAL_RANGE = ranges[self.fr]
        self.fr = eval(self.fr.title()).set(self.c)
        for vert in range(self.xpix):
            for horiz in range(self.ypix):
                c = Complex.Number(((FRACTAL_RANGE/self.xpix) * horiz) - FRACTAL_RANGE/2,
                    ((FRACTAL_RANGE/self.xpix) * vert) - FRACTAL_RANGE/2)
                if self.fr.isMember(c):
                    self.pic[vert].append(255) # white
                else:
                    self.pic[vert].append(0) # black

        self.w.write(self.f, self.pic)
        self.f.close()
