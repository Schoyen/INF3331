from mandelbrot import MandelbrotPython, MandelbrotNumpy, MandelbrotCython
from matplotlib.pylab import imshow, show
from time import time

function_map = [MandelbrotPython, MandelbrotNumpy, MandelbrotCython]
args = [-3, 3, -3, 3, 1000, 1000] # [xmin, xmax, ymin, ymax, Nx, Ny]
max_iterations = 1000
divergence = 2
time_list = []


for func in function_map:
    time_list.append([])
    for i in range(5):
        mp = func(*args, max_escape_time=max_iterations)
        t0 = time()
        mat = mp()
        t1 = time()
        time_list[-1].append(t1 - t0)
        print ("%s: %d %g sec" % (mp.__class__.__name__, i, time_list[-1][-1]))
        imshow(mat)
        show()


python_avg = sum(time_list[0])/5.0
numpy_avg = sum(time_list[1])/5.0
cython_avg = sum(time_list[2])/5.0

print ("Running time for Python: {:.4}".format(python_avg))
print ("Running time for Numpy: {:.4}".format(numpy_avg))
print ("Running time for Cython: {:.4}".format(cython_avg))

print ("Normalized running times")
print ("""
Python: {0:.4}
Numpy:  {1:.4}
Cython: {2:.4}
""".format(python_avg/float(python_avg), numpy_avg/float(python_avg), cython_avg/float(python_avg)))
