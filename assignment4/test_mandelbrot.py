from unittest import TestCase, main
from mandelbrot import compute_mandelbrot, MandelbrotPython, MandelbrotNumpy, MandelbrotCython
from numpy import all as npall

class TestMandelbrot(TestCase):
    """Class for testing the Mandelbrot implementations.

    This class makes use of the unittest module and tests the compute_mandelbrot function for
    some "bad" region values.
    """
    def setUp(self):
        """Constructor for class TestMandelbrot.

        This constructor stores the Mandelbrot classes in a list for use in iteration.
        """
        self.functions = [MandelbrotPython, MandelbrotNumpy, MandelbrotCython]

    def test_area_outside(self):
        """Function testing compute_mandelbrot for a region outside the Mandelbrot set."""
        args = [3, 4, 3, 4, 100, 100] # [xmin, xmax, ymin, ymax, Nx, Ny]
        max_iterations=10
        tol = 1e-14
        for func in self.functions:
            msg = "Class: %s: For x in [%g, %g] and y in [%g, %g] we expected instant divergence, i.e., all matrix elements equal to 1" % (func.__name__,
                    args[0], args[1], args[2], args[3])
            assert npall((compute_mandelbrot(*args, max_escape_time=max_iterations, mandelbrot_class=func) - 1.0) < tol), msg

    def test_area_inside(self):
        """Function testing compute_mandelbrot for a region completely inside the Mandelbrot set."""
        args = [0.0, 0.1, -0.1, 0.1, 100, 100] # [xmin, xmax, ymin, ymax, Nx, Ny]
        max_iterations=10
        tol = 1e-14
        for func in self.functions:
            msg = "Class: %s: For x in [%g, %g] and y in [%g, %g] we expected instant divergence, i.e., all matrix elements equal to %g" % (func.__name__,
                    args[0], args[1], args[2], args[3], max_iterations)
            assert npall((compute_mandelbrot(*args, max_escape_time=max_iterations, mandelbrot_class=func) - max_iterations) < tol), msg

if __name__ == '__main__':
    main()
