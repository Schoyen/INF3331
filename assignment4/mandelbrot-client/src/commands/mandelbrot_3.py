from mandelbrot import mandelbrot_set
from matplotlib.pylab import imshow, show

height = 100
width = 100
threshold = 100
divergence_criteria = 2
imshow(mandelbrot_set(height, width, threshold, divergence_criteria))
show()
