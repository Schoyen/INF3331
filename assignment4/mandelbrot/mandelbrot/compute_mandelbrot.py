from . import MandelbrotNumpy
from matplotlib.pylab import imshow, savefig
from time import time

def compute_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, plot_filename=None,
        mandelbrot_class=MandelbrotNumpy, divergence_criteria=2):
    mc = mandelbrot_class(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=max_escape_time, divergence_criteria=divergence_criteria)
    t0 = time()
    escape_matrix = mc()
    t1 = time()
    print ("{0}: {1:.4} s".format(mc.__class__.__name__, t1 - t0))
    if plot_filename:
        imshow(escape_matrix)
        savefig(plot_filename)
    print (escape_matrix)
    return escape_matrix
