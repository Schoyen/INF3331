
class MandelbrotPython:

    def __init__(self, xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, divergence_criteria=2):
        self.xmin = xmin; self.xmax = xmax; self.Nx = Nx
        self.ymin = ymin; self.ymax = ymax; self.Ny = Ny
        self.max_escape_time = max_escape_time
        self.divergence_criteria = divergence_criteria

        self.mandelbrot_set = [[0 for i in range(self.Nx)] for j in range(self.Ny)]
        self.dx = (self.xmax - self.xmin)/float(self.Nx - 1)
        self.dy = (self.ymax - self.ymin)/float(self.Ny - 1)

    def __call__(self):
        for j in range(self.Ny):
            for i in range(self.Nx):
                x = c_real = self.xmin + i*self.dx
                y = c_imag = self.ymin + j*self.dy
                abs_z_squared = x*x + y*y
                while self.mandelbrot_set[j][i] < self.max_escape_time and abs_z_squared < self.divergence_criteria**2:
                    self.mandelbrot_set[j][i] += 1
                    x, y = (x*x - y*y + c_real, 2*x*y + c_imag)
                    abs_z_squared = x*x + y*y
        return self.mandelbrot_set

if __name__ == '__main__':
    from matplotlib.pylab import imshow, show
    mp = MandelbrotPython(-2, 0.5, -1, 1, 100, 200)
    imshow(mp())
    show()
