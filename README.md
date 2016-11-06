# Fractious

This is the world's best fractal generator. Fully unit-tested, with an MVC architecture. Most Probably.
Currently, the Mandelbrot and Julia sets have been implemented.

![Mandelbrot](mandelbrot.png?raw=true)
![Julia](julia.png?raw=true)

To create a fractal, simply clone and run fracter.py, followed by the desired fractal and filename,
e.g. python fracter.py julia test.png. A variety of optional parameters are also available
(note the lack of spacing after commas within square brackets):

* Image Dimensions, widthxheight, e.g. --dim 400x400
* Zoom multiplier, e.g. --zoom 2
* Camera pan, x and y, e.g. --pan [-1.0,0.5]
* Iterations, e.g. --iters 100
* Complex Number. Only relevant to Julia for now. e.g. --com [0,0.8]

## Testing

So far, tests have been implemented for Complex.py, Julia.py, and Renderer.py. To test them, use `python complextest.py`.
To measure test coverage, install `python-coverage` and run `python-coverage -x complextest.py` followed by `python-coverage -rm -o /usr`.
