from unittest import TestCase, main
from mandelbrot import compute_mandelbrot
from numpy import all as npall

class TestMandelbrot(TestCase):

    def test_area_outside(self):
        args = [3, 4, 3, 4, 100, 100] # [xmin, xmax, ymin, ymax, Nx, Ny]
        max_iterations=10
        tol = 1e-14
        msg = "For x in [%g, %g] and y in [%g, %g] we expected instant divergence, i.e., all matrix elements equal to 1" % (args[0], args[1],
                args[2], args[3])
        assert npall((compute_mandelbrot(*args, max_escape_time=max_iterations) - 1.0) < tol), msg

    def test_area_inside(self):
        args = [0.0, 0.1, -0.1, 0.1, 100, 100] # [xmin, xmax, ymin, ymax, Nx, Ny]
        max_iterations=10
        tol = 1e-14
        msg = "For x in [%g, %g] and y in [%g, %g] we expected no divergence, i.e., all matrix elements equal to %g" % (args[0], args[1],
                args[2], args[3], max_iterations)
        assert npall((compute_mandelbrot(*args, max_escape_time=max_iterations) - 10.0) < tol), msg


if __name__ == '__main__':
    main()
