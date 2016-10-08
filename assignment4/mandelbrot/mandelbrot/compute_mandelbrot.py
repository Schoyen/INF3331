from . import MandelbrotNumpy
from matplotlib.pylab import imshow, show, savefig

def compute_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, plot_filename=None, mandelbrot_class=MandelbrotNumpy):
    mc = mandelbrot_class(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=max_escape_time)
    escape_matrix = mc()
    if plot_filename:
        imshow(escape_matrix)
        savefig(plot_filename)
    return escape_matrix
