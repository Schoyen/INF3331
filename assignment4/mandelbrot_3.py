from mandelbrot import mandelbrot_set

height = 10
width = 10
threshold = 10
divergence_criteria = 2
print (mandelbrot_set(height, width, threshold, divergence_criteria).shape)
