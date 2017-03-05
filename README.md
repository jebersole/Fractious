# Fractious

This is the world's best fractal generator. Fully unit-tested, with an MVC architecture.
Currently, the Mandelbrot and Julia sets have been implemented.

![Mandelbrot](assets/mandelbrot.png?raw=true)
![Julia](assets/julia.png?raw=true)

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

So far, tests have been implemented for Complex.py, Julia.py, Mandelbrot.py and Renderer.py. To test them, use `python -m unittest discover -v -s tests`
from the root project directory. To measure test coverage, install `python-coverage` and run `python -m coverage run -m unittest discover -v -s tests`
followed by something like `python -m coverage report --omit='/usr' -rm` or just `--omit='png.py'`

Current coverage output:
```
Name                      Stmts   Miss  Cover
---------------------------------------------
Arguer.py                    13      0   100%
Complex.py                   17      0   100%
Julia.py                     24      0   100%
Mandelbrot.py                22      0   100%
Renderer.py                  33      0   100%
tests\testcomplex.py         66      0   100%
tests\testjulia.py           25      0   100%
tests\testmandelbrot.py      25      0   100%
tests\testrenderer.py        32      0   100%
---------------------------------------------
TOTAL                       257      0   100%
```
