from . import MandelbrotCython # Include a "standard" (the fastest ZOMG!)
from matplotlib.pylab import imshow, savefig, xlabel, ylabel, rc, show
from numpy import all as npall, arange

def compute_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, plot_filename=None,
        mandelbrot_class=MandelbrotCython, divergence_criteria=2, show_image=False):
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
        show_image:             A bool determining if the image shall be shown on screen.
    """
    mc = mandelbrot_class(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=max_escape_time, divergence_criteria=divergence_criteria)
    escape_matrix, ok = check_area(xmin, xmax, ymin, ymax, Nx, Ny, divergence_criteria)
    if ok:
        escape_matrix = mc() # Calculate the Mandelbrot set
    if plot_filename or show_image:
        plot_image(plot_filename, show_image, escape_matrix, xmin, xmax, ymin, ymax)
    return escape_matrix

def plot_image(filename, show_image, matrix, xmin, xmax, ymin, ymax):
    """Function used for plotting the Mandelbrot set.

    Args:
        filename:               A filename for storing the image of the Mandelbrot set.
        show_image:             A bool determining if the image shall be shown on screen.
        xmin:                   Start coordinate for the real axis.
        xmax:                   Stop coordinate for the real axis.
        ymin:                   Start coordinate for the complex axis.
        ymax:                   Stop coordinate for the complex axis.
    """
    rc('text', usetex=True)
    imshow(matrix, extent=[xmin, xmax, ymin, ymax], interpolation='none')
    xlabel(r'$\Re$', fontsize=14)
    ylabel(r'$\Im$', fontsize=14)
    if filename:
        savefig(filename, dpi=1000)
    if show_image:
        show()

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
