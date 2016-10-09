from .mandelbrot_cython import mandelbrot_set_cython

class MandelbrotCython:
    """Class used to call on Cython-implementation.

    This class contains a calling function for calling on the Cython function
    mandelbrot_set_cython with the correct parameters.
    """

    def __init__(self, xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, divergence_criteria=2):
        """Constructor for class MandelbrotCython.

        Args:
            xmin:                   Start coordinate for the real axis.
            xmax:                   Stop coordinate for the real axis.
            ymin:                   Start coordinate for the complex axis.
            ymax:                   Stop coordinate for the complex axis.
            Nx:                     The number of steps along the real axis.
            Ny:                     The number of steps along the complex axis.
            max_escape_time:        The maxmimum amount of iterations in determining if a point has converged.
            divergence_criteria:    A float used to determine if a point in the complex plane has diverged.
        """

        self.args = [xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time, divergence_criteria]

    def __call__(self):
        """Calling function for class MandelbrotCython.

        This function returns the Mandelbrot set from the Cython function mandelbrot_set_cython.

        Returns:
            np.ndarray:             A 2-dimensional matrix with the number of iterations needed
                                    before a point in the complex plane diverged.
        """
        return mandelbrot_set_cython(*self.args)
