from .mandelbrot_cython import mandelbrot_set_cython

class MandelbrotCython:

    def __init__(self, xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, divergence_criteria=2):
        self.args = [xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time, divergence_criteria]

    def __call__(self):
        return mandelbrot_set_cython(*self.args)
