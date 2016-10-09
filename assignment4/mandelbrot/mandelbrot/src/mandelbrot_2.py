from numpy import ogrid, zeros, conj, complex64, uint8


class MandelbrotNumpy:
    """Class calculating the Mandelbrot set using Python with Numpy.

    This class contains a calling function for solving the Mandelbrot set in a
    specified region.
    """

    def __init__(self, xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, divergence_criteria=2):
        """Constructor for class MandelbrotNumpy.

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
        self.xmin = xmin; self.xmax = xmax; self.Nx = Nx
        self.ymin = ymin; self.ymax = ymax; self.Ny = Ny
        self.max_escape_time = max_escape_time
        self.divergence_criteria = divergence_criteria

    def __call__(self):
        """Calling function for class MandelbrotPython.

        This function calculates the Mandelbrot set using Python and Numpy.

        Returns:
            divergence_steps:       A 2-dimensional matrix with the number of iterations needed
                                    before a point in the complex plane diverged.
        """
        c_complex, c_real = ogrid[self.ymin:self.ymax:self.Ny*1j, self.xmin:self.xmax:self.Nx*1j]
        c = c_real + 1j*c_complex
        c = c.astype(complex64)
        z = zeros(c.shape, dtype=complex64)
        divergence_steps = zeros(z.shape, dtype=uint8)
        div = self.divergence_criteria**2
        for i in range(1, self.max_escape_time + 1):
            indices = (z.real*z.real + z.imag*z.imag) <= div # Create mask
            z[indices] = z[indices]**2 + c[indices]
            divergence_steps[indices] = i
        return divergence_steps
