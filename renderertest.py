# Test Renderer functionality. Test images may be deleted afterwards as desired.

import unittest
import os.path
import struct
import Renderer
import Arguer

class RendererTest(unittest.TestCase):
    # Tests if png was created and if output and input dimensions match
    def testFile(self): # 3 test cases: small, medium, and large images
        filenames = {"test1.png":"300x300", "test2.png":"50x50", "test3.png":"1000x1000"}
        for current in filenames:
            args = Arguer.Argue(['julia', current, '--dim', filenames[current]])
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
        return width == int(twidth) & height == int(theight)

if __name__ == "__main__":
    unittest.main()
