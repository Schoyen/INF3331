from mandelbrot import MandelbrotPython, MandelbrotNumpy, MandelbrotCython
from cProfile import Profile
from pstats import Stats
from matplotlib.pylab import imshow, show

function_map = [MandelbrotPython, MandelbrotNumpy, MandelbrotCython]
args = [-3, 3, -3, 3, 1000, 1000] # [xmin, xmax, ymin, ymax, Nx, Ny]
max_iterations = 1000
mp = MandelbrotPython(*args, max_escape_time=max_iterations)

profile = Profile()
profile.enable()
#profile.run('mp()')
mat = mp()
profile.disable()
profile.dump_stats('test.prof')
stats = Stats('test.prof')
stats.sort_stats('time')
stats.print_stats(3)

imshow(mat)
show()
