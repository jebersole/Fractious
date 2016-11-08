# Test Renderer functionality. Test images may be deleted afterwards as desired.
# Warning: this test is very time-consuming.

import unittest
import os.path
import struct
import Renderer
import Arguer

class RendererTest(unittest.TestCase):
    # Tests if png was created and if output and input dimensions match
    def testFile(self): # 3 test cases: small, medium, and large images
        self.checkFile('julia')
        self.checkFile('mandelbrot')

    # Tests various optional parameters
    def testParams(self):
        self.checkParams('julia')
        self.checkParams('mandelbrot')

    def checkParams(self, fractal):
        filenames = {"test1.png":"200x300", "test2.png":"20x20"}
        for current in filenames:
            args = Arguer.Argue([fractal, current, '--dim', filenames[current], '--zoom', '2',
                '--pan', '[-1.0,1.0]', '--iters', '50', '--com', '[-0.75,0.11]'])
            r = Renderer.Render(args).draw()
            args = Arguer.Argue([fractal, current, '--dim', filenames[current], '--zoom', '5',
                '--pan', '[2.5,-0.5]', '--iters', '13'])
            r = Renderer.Render(args).draw()
            self.assertTrue(os.path.isfile(current))
            self.assertTrue(self.checkDims(filenames[current][: filenames[current].index('x')],
                filenames[current][filenames[current].index('x') + 1:], current))

    def checkFile(self, fractal):
        filenames = {"test1.png":"300x300", "test2.png":"50x50", "test3.png":"1000x1000"}
        for current in filenames:
            args = Arguer.Argue([fractal, current, '--dim', filenames[current]])
            r = Renderer.Render(args).draw()
            self.assertTrue(os.path.isfile(current))
            self.assertTrue(self.checkDims(filenames[current][: filenames[current].index('x')],
                filenames[current][filenames[current].index('x') + 1:], current))

    def checkDims(self, twidth, theight, filename): # test input width and height
        f = open(filename, 'rb')
        data = f.read()
        w, h = struct.unpack('>LL', data[16:24])
        width = int(w) # output width and height
        height = int(h)
        return (width == int(twidth)) and (height == int(theight))

if __name__ == "__main__":
    unittest.main()
