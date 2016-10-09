from mandelbrot import MandelbrotPython, MandelbrotNumpy, MandelbrotCython
from matplotlib.pylab import imshow, show
from time import time

function_map = [MandelbrotPython, MandelbrotNumpy, MandelbrotCython]
args = [-3, 3, -3, 3, 1000, 1000] # [xmin, xmax, ymin, ymax, Nx, Ny]
max_iterations = 1000
divergence = 2
time_list = []

for func in function_map:
    mp = func(*args, max_escape_time=max_iterations)
    t0 = time()
    mat = mp()
    t1 = time()
    time_list.append(t1 - t0)
    imshow(mat)
    show()

print (time_list)
