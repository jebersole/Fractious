#Create a julia fractal

import png
import Julia
import Complex
import argparse
JULIA_RANGE = 4.0

# command line arguments
parser = argparse.ArgumentParser(description='Create a Julia fractal.')
parser.add_argument('file', metavar='F', type=str,
                    help='filename for png image to be created, e.g. file.png')
parser.add_argument('--dimensions', metavar='D', type=str, default='300x300',
                    help='dimensions of desired image, e.g. widthxheight: 400x400')
parser.add_argument('--complex', metavar='C', type=str, default='[0,0.8]',
                    help='complex number with which to draw Julia, e.g. [0,0.8]')
args = parser.parse_args()
fname = args.file
xpix = int(args.dimensions[: args.dimensions.index('x')])
ypix = int(args.dimensions[args.dimensions.index('x') + 1:])
xcom = float(args.complex[1: args.complex.index(',')])
ycom = float(args.complex[args.complex.index(',') + 1:-1])

#initialize julia and png writer
f = open(fname, 'wb')
c = Complex.Number(xcom, ycom)
j = Julia.set(c)
w = png.Writer(xpix, ypix, greyscale=True)
pic = [[] for x in xrange(ypix)]

#draw julia with vertical and horizontal values
for vert in range(xpix):
    for horiz in range(ypix):
        c = Complex.Number(((JULIA_RANGE/xpix) * horiz) - JULIA_RANGE/2, ((JULIA_RANGE/xpix) * vert) - JULIA_RANGE/2)
        if j.isMember(c, 20): #optimal number of steps for this fractal
            pic[vert].append(255) #white
        else:
            pic[vert].append(0) #black

w.write(f, pic)
f.close()
