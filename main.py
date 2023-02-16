import sys
from mandelbrot_fractal import MandelbrotFractalBW, MandelbrotFractalColor

def draw_fractal(fractal):
    fractal.draw()
    fractal.save()

if __name__ == "__main__":

    if sys.argv[1] == 'colored':
        fractal = MandelbrotFractalColor()
    else:
        fractal = MandelbrotFractalBW()

    draw_fractal(fractal)