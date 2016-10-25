import unittest
import os.path
import struct
import argparse
import Renderer

class RendererTest(unittest.TestCase):

    def testFile(self):
        args = self.getArgs(['julia', 'test.png'])
        r = Renderer.render(args).draw()
        self.assertTrue(os.path.isfile("test.png"))
        self.assertTrue(self.checkDims(300, 300))

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

    def checkDims(self, twidth, theight):
        f = open('test.png', 'rb')
        data = f.read()
        w, h = struct.unpack('>LL', data[16:24])
        width = int(w)
        height = int(h)
        return width == twidth & height == theight

if __name__ == "__main__":
    unittest.main()
