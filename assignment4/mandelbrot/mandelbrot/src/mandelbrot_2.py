from numpy import ogrid, zeros, conj


class MandelbrotNumpy:

    def __init__(self, xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, divergence_criteria=2):
        self.xmin = xmin; self.xmax = xmax; self.Nx = Nx
        self.ymin = ymin; self.ymax = ymax; self.Ny = Ny
        self.max_escape_time = max_escape_time
        self.divergence_criteria = divergence_criteria

    def __call__(self):
        c_complex, c_real = ogrid[self.ymin:self.ymax:self.Ny*1j, self.xmin:self.xmax:self.Nx*1j]
        c = c_real + 1j*c_complex
        z = zeros(c.shape, dtype=complex)
        divergence_steps = zeros(z.shape, dtype=int)
        for i in range(self.max_escape_time):
            indices = z*conj(z) <= self.divergence_criteria**2 # Creating mask
            z[indices] = z[indices]**2 + c[indices]
            divergence_steps[indices] += 1
        return divergence_steps


if __name__ == '__main__':
    from matplotlib.pylab import imshow, show, savefig
    mv = MandelbrotNumpy(-2, 0.5, -1, 1, 1000, 1000)
    imshow(mv())
    show()
