import numpy
cimport numpy

cpdef numpy.ndarray[numpy.int16_t, ndim=2] mandelbrot_set_cython(
        xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time, divergence_criteria):
    cdef numpy.ndarray[numpy.complex128_t, ndim=1] c_complex
    cdef numpy.ndarray[numpy.double_t, ndim=1] c_real
    c_imag = 1j*numpy.linspace(ymin, ymax, Ny)
    c_real = numpy.linspace(xmin, xmax, Nx)
    cdef numpy.ndarray[numpy.complex128_t, ndim=2] c, cv, vc
    cv, vc = numpy.meshgrid(c_real, c_imag)
    c = cv + vc
    cdef numpy.ndarray[numpy.complex128_t, ndim=2] z
    z = numpy.zeros_like(c)
    cdef numpy.ndarray[numpy.int16_t, ndim=2] divergence_steps
    divergence_steps = numpy.zeros([Nx, Ny], dtype=numpy.int16)
    cdef int i, j, k
    cdef float divergence
    divergence = divergence_criteria**2

    for i in range(max_escape_time):
        for k in range(Nx):
            for j in range(Ny):
                if z[k][j]*numpy.conj(z[k][j]) <= divergence:
                    z[k][j] = z[k][j]**2 + c[k][j]
                    divergence_steps[k][j] += 1

    return divergence_steps
