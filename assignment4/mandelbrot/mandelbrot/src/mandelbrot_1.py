
class MandelbrotPython:
    """Class implementing a solver for the Mandelbrot set.

    This class contains a calling function for solving the Mandelbrot set in a
    specified region.
    """

    def __init__(self, xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, divergence_criteria=2):
        """Constructor for class MandelbrotPython.

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

        This function calculates the Mandelbrot set using nothing but native Python.

        Returns:
            mandelbrot_set:         A 2-dimensional list with the number of iterations needed
                                    before a point in the complex plane diverged.
        """
        self.mandelbrot_set = [[0 for i in range(self.Nx)] for j in range(self.Ny)]
        self.dx = (self.xmax - self.xmin)/float(self.Nx - 1)
        self.dy = (self.ymax - self.ymin)/float(self.Ny - 1)
        div = self.divergence_criteria**2
        for i in range(self.Nx):
            c_real = self.xmin + i*self.dx
            for j in range(self.Ny):
                c_imag = self.ymin + j*self.dy
                z_real = z_imag = 0.0
                for k in range(1, self.max_escape_time + 1):
                    z_real, z_imag = (z_real*z_real - z_imag*z_imag + c_real, 2*z_real*z_imag + c_imag)
                    if (z_real*z_real + z_imag*z_imag) > div:
                        break
                    self.mandelbrot_set[j][i] = k
        return self.mandelbrot_set
