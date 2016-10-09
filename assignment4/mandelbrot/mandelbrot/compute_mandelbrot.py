from . import MandelbrotNumpy
from matplotlib.pylab import imshow, savefig

def compute_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, plot_filename=None,
        mandelbrot_class=MandelbrotNumpy, divergence_criteria=2):
    mc = mandelbrot_class(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=max_escape_time, divergence_criteria=divergence_criteria)
    escape_matrix = mc()
    if plot_filename:
        imshow(escape_matrix)
        savefig(plot_filename)
    print (escape_matrix)
    #return escape_matrix
