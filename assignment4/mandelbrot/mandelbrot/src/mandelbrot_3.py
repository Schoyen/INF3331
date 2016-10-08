from .mandelbrot_cython import mandelbrot_set_cython
from time import time

class MandelbrotCython:

    def __init__(self, xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, divergence_criteria=2):
        self.args = [xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time, divergence_criteria]

    def __call__(self):
        t0 = time()
        m_set = mandelbrot_set_cython(*self.args)
        t1 = time()
        print ("Cython-time: {:.4} s".format(t1 - t0))
        return m_set
