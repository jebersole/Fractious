# Fractious

This is the world's best fractal generator. Fully unit-tested, with an MVC architecture.
Currently, the Mandelbrot and Julia sets have been implemented.

![Mandelbrot](mandelbrot.png?raw=true)
![Julia](julia.png?raw=true)

This program uses Python and pypng to create png images. Pypng can be installed in Linux with
the command `pip install pypng`, or via https://github.com/drj11/pypng.
In Windows, Python must first be installed from the python.org website. The easiest way to install
pypng on that OS is to clone the raw pypng file from https://raw.githubusercontent.com/drj11/pypng/master/code/png.py.

To create a fractal, simply clone Fractious and run fracter.py, followed by the desired fractal and filename,
e.g. `python fracter.py julia test.png`. A variety of optional parameters are also available
(note the lack of spacing after commas within square brackets):

* Image Dimensions, widthxheight, e.g. `--dim 400x400`
* Zoom multiplier, e.g. `--zoom 2`
* Camera pan, x and y, e.g. `--pan [-1.0,0.5]`
* Iterations, e.g. `--iters 100`
* Complex Number. Only relevant to Julia for now. e.g. `--com [0,0.8]`

## Testing

So far, tests have been implemented for Complex.py, Julia.py, Mandelbrot.py and Renderer.py. To test them, use `python complextest.py` and similar commands
for other tests. To measure test coverage, install `python-coverage` and run `python-coverage -x complextest.py` followed by `python-coverage -rm -o /usr`,
or something like `python-coverage --omit='/usr/local/lib/python2.7/dist-packages/*' -rm`.

Current coverage output:
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
Arguer              14      1    93%   23
Complex             17      0   100%   
Julia               24      0   100%   
Mandelbrot          22      0   100%   
Renderer            37      0   100%   
juliatest           27      0   100%   
mandelbrottest      27      0   100%   
renderertest        37      0   100%   
----------------------------------------------
TOTAL              205      1    99%   

