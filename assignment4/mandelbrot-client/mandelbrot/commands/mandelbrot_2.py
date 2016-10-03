from numpy import ogrid, zeros, conj
from matplotlib.pylab import imshow, show, savefig
from tqdm import tqdm


class MandelbrotVec:

    def __init__(self, height, width, threshold=100):
        self.height = height
        self.width = width
        self.threshold = threshold

    def __call__(self, divergence_criteria=2):
        c_complex, c_real = ogrid[-1.4:1.4:self.height*1j, -2:0.8:self.width*1j]
        c = c_real + 1j*c_complex
        z = zeros(c.shape, dtype=complex)
        divergence_steps = zeros(z.shape, dtype=int)
        for i in tqdm(range(self.threshold)):
            indices = z*conj(z) <= divergence_criteria
            z[indices] = z[indices]**2 + c[indices]
            divergence_steps[indices] += 1
        return divergence_steps


if __name__ == '__main__':
    mv = MandelbrotVec(1000, 1000, threshold=100)
    imshow(mv(divergence_criteria=2))
    savefig("dat/mandelbrot_numpy.pdf")
    show()
