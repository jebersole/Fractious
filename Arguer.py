import argparse

def Argue(param):
    # Command line arguments
    parser = argparse.ArgumentParser(description='Create a fractal.')
    parser.add_argument('fractal', metavar='Fr', type=str,
                        help='fractal to be created, e.g. julia')
    parser.add_argument('file', metavar='F', type=str,
                        help='filename for desired png image, e.g. file.png')
    parser.add_argument('--dim', metavar='D', type=str, default='300x300',
                        help='dimensions of image, e.g. widthxheight: 400x400')
    parser.add_argument('--com', metavar='C', type=str, default='[0,0.8]',
                        help='complex number with which to draw fractal, e.g. [0,0.8]'),
    parser.add_argument('--zoom', metavar='Z', type=str, default='1',
                        help='zoom factor, e.g. 2')
    parser.add_argument('--pan', metavar='P', type=str, default='0',
                        help='pan left or right, e.g. 1.5')
    parser.add_argument('--iters', metavar='I', type=str, default='0',
                        help='number of fractal iterations, e.g. 20')
    if param != "command_line":
        args = parser.parse_args(param)
    else:
        args = parser.parse_args()
    return args
