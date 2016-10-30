# Drawing class to create a fractal png

import png
import Complex
import Julia

# Initialize fractal class and png writer
class Render:
    def __init__(self, args):
        # Assign parameters from user-provided arguments
        self.fr = args.fractal.lower()
        self.zoom = float(args.zoom)
        ranges = {'julia': 4.0, 'something': 2.6}
        iters = {'julia': 20, 'something': 50}
        self.range = ranges[self.fr] / self.zoom
        self.xpix = int(args.dim[: args.dim.index('x')])
        self.ypix = int(args.dim[args.dim.index('x') + 1:])
        self.xcom = float(args.com[1: args.com.index(',')])
        self.ycom = float(args.com[args.com.index(',') + 1: -1])
        # default values are indicated with 0s
        self.pan = -self.range / 2 if float(args.pan) == 0 else float(args.pan)
        self.iters = iters[self.fr] if int(args.iters) == 0 else int(args.iters)
        self.f = open(args.file, 'wb')
        self.c = Complex.Number(self.xcom, self.ycom)
        self.w = png.Writer(self.xpix, self.ypix, greyscale=False)
        self.pic = [[] for x in xrange(self.ypix)]

    def draw(self):
        # Draw fractal with vertical and horizontal values
        self.fr = eval(self.fr.title()).set(self.c)
        for vert in range(self.xpix):
            for horiz in range(self.ypix):
                c = Complex.Number(((self.range/self.xpix) * horiz) + self.pan,
                    ((self.range/self.xpix) * vert) + self.pan)
                if self.fr.isMember(c, self.iters):
                    self.pic[vert].append(0) # R
                    self.pic[vert].append(0) # G
                    self.pic[vert].append(255) # B
                else:
                    self.pic[vert].append(0) # R
                    self.pic[vert].append(0) # G
                    self.pic[vert].append(0) # B
        self.w.write(self.f, self.pic)
        self.f.close()
