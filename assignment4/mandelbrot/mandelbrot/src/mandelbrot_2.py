from numpy import ogrid, zeros, conj, less, complex64, uint8


class MandelbrotNumpy:

    def __init__(self, xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time=1000, divergence_criteria=2):
        self.xmin = xmin; self.xmax = xmax; self.Nx = Nx
        self.ymin = ymin; self.ymax = ymax; self.Ny = Ny
        self.max_escape_time = max_escape_time
        self.divergence_criteria = divergence_criteria

    def __call__(self):
        c_complex, c_real = ogrid[self.ymin:self.ymax:self.Ny*1j, self.xmin:self.xmax:self.Nx*1j]
        c = c_real + 1j*c_complex
        z = zeros(c.shape, dtype=complex64)
        divergence_steps = zeros(z.shape, dtype=uint8)
        div = self.divergence_criteria**2
        for i in range(1, self.max_escape_time + 1):
            indices = less(z.real*z.real + z.imag*z.imag, div)
            z[indices] = z[indices]**2 + c[indices]
            divergence_steps[indices] = i
        return divergence_steps
