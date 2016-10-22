# Create a png fractal

import argparse
import Renderer

# Command line arguments
parser = argparse.ArgumentParser(description='Create a fractal.')
parser.add_argument('fractal', metavar='Fr', type=str,
                    help='fractal to be created, e.g. julia')
parser.add_argument('file', metavar='F', type=str,
                    help='filename for desired png image, e.g. file.png')
parser.add_argument('--dimensions', metavar='D', type=str, default='300x300',
                    help='dimensions of image, e.g. widthxheight: 400x400')
parser.add_argument('--complex', metavar='C', type=str, default='[0,0.8]',
                    help='complex number with which to draw fractal, e.g. [0,0.8]')
args = parser.parse_args()

r = Renderer.render(args)
