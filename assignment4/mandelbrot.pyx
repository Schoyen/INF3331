import numpy
cimport numpy

cpdef numpy.ndarray[numpy.int16_t, ndim=2] mandelbrot_set(
        height, width, threshold, divergence_criteria):
    cdef numpy.ndarray[numpy.double_t, ndim=1] c_complex, c_real
    c_complex = numpy.ogrid[-1.4:1.4:height*1j]
    c_real = numpy.ogrid[-2:0.8:width*1j]
    cdef numpy.ndarray[numpy.complex_t, ndim=1] c
    c = c_real + 1j*c_complex
    cdef numpy.ndarray[numpy.complex_t, ndim=1] z
    z = numpy.zeros([10, 0], dtype=numpy.complex_t)
