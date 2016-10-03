import numpy
cimport numpy

cpdef numpy.ndarray[numpy.int16_t, ndim=1] mandelbrot_set(
        height, width, threshold, divergence_criteria):
    cdef numpy.ndarray[numpy.double_t, ndim=1] c_complex, c_real
    c_complex = numpy.ogrid[-1.4:1.4:height*1j]
    c_real = numpy.ogrid[-2:0.8:width*1j]
    cdef numpy.ndarray[numpy.complex128_t, ndim=2] c
    c = numpy.array([c_real + 1j*c_complex])
    cdef numpy.ndarray[numpy.complex128_t, ndim=2] z
    z = numpy.zeros_like(c)
    cdef numpy.ndarray[numpy.int16_t, ndim=2] divergence_steps
    divergence_steps = numpy.zeros([width, height], dtype=numpy.int16)
    cdef int i, j

    for i in range(threshold):
        for j in range(width):
            if z[0][j]*numpy.conj(z[0][j]) <= divergence_criteria:
                z[0][j] = z[0][j]**2 + c[0][j]
                divergence_steps[0][j] += 1

    return divergence_steps
