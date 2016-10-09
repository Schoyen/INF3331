
class MandelbrotPython:

    def __init__(self, xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, divergence_criteria=2):
        self.xmin = xmin; self.xmax = xmax; self.Nx = Nx
        self.ymin = ymin; self.ymax = ymax; self.Ny = Ny
        self.max_escape_time = max_escape_time
        self.divergence_criteria = divergence_criteria

    def __call__(self):
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

if __name__ == '__main__':
    from matplotlib.pylab import imshow, show
    mp = MandelbrotPython(-2, 0.5, -1, 1, 100, 200)
    imshow(mp())
    show()
