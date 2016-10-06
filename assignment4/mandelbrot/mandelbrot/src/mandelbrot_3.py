from mandelbrot import mandelbrot_set
from matplotlib.pylab import imshow, show

height = 100
width = 100
threshold = 100
divergence_criteria = 2
imshow(mandelbrot_set(-2, 0.5, -1, 1, 100, 200))
show()
