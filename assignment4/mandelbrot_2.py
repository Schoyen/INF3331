from numpy import linspace, array, zeros, sqrt

n = 1000
threshold = 1000
c = array([linspace(-2, 0.5, n), linspace(-1, 1, n)])
z = zeros((n, n))
counter = 0

while counter < threshold:
    z[sqrt(z[0]**2 + z[1]**2) <= 2] = array([z[0]**2 - z[1]**2 + c[0], 2*z[0]*z[1] + c[1]])
