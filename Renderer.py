# Drawing class to create a fractal png

import png
import Complex
import Julia
import Mandelbrot
import KochSnowflake
import colorsys

# Initialize fractal class and png writer
class Render:
    def __init__(self, args):
        # Assign parameters from user-provided arguments
        # only Julia currently requires a complex init
        '''
        if args.fractal.lower() == 'julia':
            xcom = float(args.com[1: args.com.index(',')])
            ycom = float(args.com[args.com.index(',') + 1: -1])
            self.frac = Julia.set(Complex.Number(xcom, ycom))
        else:
            self.frac = Mandelbrot.set()
        '''
        self.xpix = int(args.dim[: args.dim.index('x')])
        self.ypix = int(args.dim[args.dim.index('x') + 1:])
        self.frac = KochSnowflake.set(self.xpix)
        if args.zoom != 'default': self.frac.frange /= float(args.zoom)
        if args.pan == 'default':
            self.panX = self.frac.panX
            self.panY = self.frac.panY
        else:
            self.panX = float(args.pan[1: args.pan.index(',')])
            self.panY = float(args.pan[args.pan.index(',') + 1: -1])
        if args.iters != 'default': self.frac.iters = int(args.iters)
        self.f = open(args.file, 'wb')
        self.w = png.Writer(self.xpix, self.ypix)
        self.pic = [[] for x in xrange(self.ypix)]

    # Draw fractal with vertical and horizontal pixel values
    def draw(self):
        for vert in range(self.xpix):
            for horiz in range(self.ypix):
                #c = Complex.Number( (self.frac.frange/self.xpix) * horiz + self.panX,
                #    (self.frac.frange/self.xpix) * vert + self.panY )
                # if isMember returns True, point is inSet and color values provided
                inSet, smoothColor = self.frac.isMember(horiz, vert)
                if inSet:
                    # additional color adjustment
                    colors = colorsys.hsv_to_rgb((self.frac.coloradj['base'] +
                        (self.frac.coloradj['multiplier'] * smoothColor)), 1.0, 1.0)
                    colors = [int(i*255) for i in colors]
                    self.pic[vert].extend(colors)
                else:
                    self.pic[vert].extend([0,0,0]) # black
        self.w.write(self.f, self.pic)
        self.f.close()
