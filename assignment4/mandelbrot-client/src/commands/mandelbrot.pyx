import numpy
cimport numpy

cpdef numpy.ndarray[numpy.int16_t, ndim=2] mandelbrot_set(
        height, width, threshold, divergence_criteria):
    cdef numpy.ndarray[numpy.complex128_t, ndim=1] c_complex
    cdef numpy.ndarray[numpy.double_t, ndim=1] c_real
    c_complex = 1j*numpy.linspace(-1.4, 1.4, height)
    c_real = numpy.linspace(-2, 0.8, width)
    cv, vc = numpy.meshgrid(c_real, c_complex)
    cdef numpy.ndarray[numpy.complex128_t, ndim=2] c
    c = cv + vc
    cdef numpy.ndarray[numpy.complex128_t, ndim=2] z
    z = numpy.zeros_like(c)
    cdef numpy.ndarray[numpy.int16_t, ndim=2] divergence_steps
    divergence_steps = numpy.zeros([width, height], dtype=numpy.int16)
    cdef int i, j, k

    for i in range(threshold):
        for k in range(width):
            for j in range(height):
                if z[k][j]*numpy.conj(z[k][j]) <= divergence_criteria:
                    z[k][j] = z[k][j]**2 + c[k][j]
                    divergence_steps[k][j] += 1

    return divergence_steps
