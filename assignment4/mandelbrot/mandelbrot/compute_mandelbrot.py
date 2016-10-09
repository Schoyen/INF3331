from . import MandelbrotCython # Include a "standard" (the fastest ZOMG!)
from matplotlib.pylab import imshow, savefig
from numpy import all as npall

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
    escape_matrix, ok = check_area(xmin, xmax, ymin, ymax, Nx, Ny, divergence_criteria)
    if ok:
        escape_matrix = mc() # Calculate the Mandelbrot set
    if plot_filename: # If the user specified a filename
        imshow(escape_matrix)
        savefig(plot_filename)
    return escape_matrix

def check_area(xmin, xmax, ymin, ymax, Nx, Ny, divergence_criteria):
    """Function used for testing if the region is sensible.

    Args:
        xmin:                   Start coordinate for the real axis.
        xmax:                   Stop coordinate for the real axis.
        ymin:                   Start coordinate for the complex axis.
        ymax:                   Stop coordinate for the complex axis.
        Nx:                     The number of steps along the real axis.
        Ny:                     The number of steps along the complex axis.
        divergence_criteria:    A float used to determine if a point in the complex plane has diverged.
    """
    test_outside_escape = 10
    tol = 1e-12
    mc = MandelbrotCython(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=test_outside_escape, divergence_criteria=divergence_criteria)
    mat = mc()
    ok = True
    if npall((mat - 1.0) < tol):
        print ("Warning: The specified region [%g, %g] x [%g, %g] is completely outside the Mandelbrot set" % (xmin, xmax, ymin, ymax))
        ok = False
    elif npall((mat - test_outside_escape) < tol):
        print ("Warning: The specified region [%g, %g] x [%g, %g] is completely inside the Mandelbrot set" % (xmin, xmax, ymin, ymax))
        ok = False

    return mat, ok
