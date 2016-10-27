# Test Renderer functionality. Test images may be deleted afterwards as desired.

import unittest
import os.path
import struct
import argparse
import Renderer

class RendererTest(unittest.TestCase):
    # Tests if png was created and if output and input dimensions match
    def testFile(self): # 3 test cases: small, medium, and large images
        filenames = {"test1.png":"300x300", "test2.png":"50x50", "test3.png":"1000x1000"}
        for current in filenames:
            args = self.getArgs(['julia', current, '--dimensions', filenames[current]])
            r = Renderer.render(args).draw()
            self.assertTrue(os.path.isfile(current))
            self.assertTrue(self.checkDims(filenames[current][: filenames[current].index('x')],
                filenames[current][filenames[current].index('x') + 1:], current))

    def getArgs(self, argsin):
        parser = argparse.ArgumentParser(description='Create a fractal.')
        parser.add_argument('fractal', metavar='Fr', type=str,
                            help='fractal to be created, e.g. julia')
        parser.add_argument('file', metavar='F', type=str,
                            help='filename for desired png image, e.g. file.png')
        parser.add_argument('--dimensions', metavar='D', type=str, default='300x300',
                            help='dimensions of image, e.g. widthxheight: 400x400')
        parser.add_argument('--complex', metavar='C', type=str, default='[0,0.8]',
                            help='complex number with which to draw fractal, e.g. [0,0.8]')
        args = parser.parse_args(argsin)
        return args

    def checkDims(self, twidth, theight, filename): # test input width and height
        f = open(filename, 'rb')
        data = f.read()
        w, h = struct.unpack('>LL', data[16:24])
        width = int(w) # output width and height
        height = int(h)
        return width == int(twidth) & height == int(theight)

if __name__ == "__main__":
    unittest.main()
