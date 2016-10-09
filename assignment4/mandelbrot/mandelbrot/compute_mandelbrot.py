from . import MandelbrotCython # Include a "standard" (the fastest ZOMG!)
from matplotlib.pylab import imshow, savefig

def compute_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, plot_filename=None,
        mandelbrot_class=MandelbrotCython, divergence_criteria=2):
    """Function used as a package for inclusion in other programs.

    Args:
        xmin:                   Start coordinate for the real axis.
        xmax:                   Stop coordinate for the real axis.
        ymin:                   Start coordinate for the complex axis.
        ymax:                   Stop coordinate for the complex axis.
        Nx:                     The number of steps along the real axis.
        Ny:                     The number of steps along the complex axis.
        max_escape_time:        The maxmimum amount of iterations in determining if a point has converged.
        divergence_criteria:    A float used to determine if a point in the complex plane has diverged.
        plot_filename:          A filename for storing the image of the Mandelbrot set.
        mandelbrot_class:       The desired class for computing the Mandelbrot set.
    """
    mc = mandelbrot_class(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=max_escape_time, divergence_criteria=divergence_criteria)
    escape_matrix = mc() # Calculate the Mandelbrot set
    if plot_filename: # If the user specified a filename
        imshow(escape_matrix)
        savefig(plot_filename)
    return escape_matrix
