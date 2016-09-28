from math import sqrt
from matplotlib.pylab import imshow, figure, show, axis, savefig
from tqdm import tqdm

class MandelbrotSet:

    def __init__(self, c, threshold=100):
        self.a, self.b = self.test_if_list_or_tuple(c, "c")
        self.threshold = threshold

    def __call__(self, z):
        x, y = self.test_if_list_or_tuple(z, "z")
        counter = 0
        x, y = (x**2 - y**2 + self.a, 2*x*y + self.b)
        abs_z = sqrt(x**2 + y**2)
        while counter < self.threshold and abs_z <= 2:
            counter += 1
            x, y = (x**2 - y**2 + self.a, 2*x*y + self.b)
            abs_z = sqrt(x**2 + y**2)
        return abs_z, counter
            
    def test_if_list_or_tuple(self, value, name):
        if type(value) == tuple or type(value) == list:
            return value
        else:
            try:
                return (float(value), 0) # Assuming a real number was sent
            except ValueError:
                raise ValueError("Variable '%s' must be a list, tuple or a real number." % (name))


def create_mandelbrot_set():
    x_start = -2
    y_start = -1
    x_stop = 0.5
    y_stop = 1
    n = 1000
    threshold = 1000
    dx = (x_stop - x_start)/float(n - 1)
    dy = (y_stop - y_start)/float(n - 1)

    # Create a white image to begin with
    A = [[[1, 1, 1] for j in range(n)] for i in range(n)]

    ms = MandelbrotSet((x_start, y_start), threshold=threshold)
    for i in tqdm(range(n)):
        for j in range(n):
            ms.a, ms.b = (x_start + i*dx, y_start + j*dx)
            abs_z, counter = ms(0)
            if abs_z <= 2:
                A[j][i] = [0, 0, 0] # Color pixel black if it is in the mandelbrot set (i.e., abs_z <= 2)
            else:
                A[j][i] = [1 - counter/float(threshold), 1 - counter/float(threshold), 1 - counter/float(threshold)]

    figure(1)
    imshow(A, extent=[x_start, x_stop, y_start, y_stop])
    savefig("mandelbrot.png")
    show()

if __name__ == '__main__':
    create_mandelbrot_set()
