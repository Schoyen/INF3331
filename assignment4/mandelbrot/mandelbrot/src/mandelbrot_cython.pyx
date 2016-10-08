import numpy
cimport numpy

cpdef numpy.ndarray[numpy.int16_t, ndim=2] mandelbrot_set_cython(
        xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time, divergence_criteria):
    cdef double c_real, c_imag, z_real, z_imag, x_start, x_stop, y_start, y_stop, dx, dy
    cdef double z_imag_squared, z_real_squared, abs_z_squared
    cdef int nx, ny, escape, divergence, i, j, k
    cdef numpy.ndarray[numpy.int16_t, ndim=2] divergence_steps
    escape = max_escape_time
    divergence = divergence_criteria**2
    nx = Nx
    ny = Ny
    divergence_steps = numpy.zeros([nx, ny], dtype=numpy.int16)
    x_start = xmin
    x_stop = xmax
    y_start = ymin
    y_stop = ymax
    dx = (x_stop - x_start)/(nx - 1)
    dy = (y_stop - y_start)/(ny - 1)
    for j in range(ny):
        for i in range(nx):
            z_real = c_real = x_start + i*dx
            z_imag = c_imag = y_start + j*dy
            z_real_squared = z_real*z_real
            z_imag_squared = z_imag*z_imag
            abs_z_squared = z_real_squared + z_imag_squared
            while divergence_steps[j][i] < escape and abs_z_squared < divergence:
                divergence_steps[j][i] += 1
                z_real = z_real_squared - z_imag_squared + c_real
                z_imag = 2*z_real*z_imag + c_imag
                z_real_squared = z_real*z_real
                z_imag_squared = z_imag*z_imag
                abs_z_squared = z_real_squared + z_imag_squared
    return divergence_steps


#cpdef numpy.ndarray[numpy.int16_t, ndim=2] mandelbrot_set_cython(
#        xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time, divergence_criteria):
#    cdef numpy.ndarray[numpy.double_t, ndim=1] c_real, c_imag, z_real, z_imag
#    c_imag = numpy.linspace(ymin, ymax, Ny)
#    c_real = numpy.linspace(xmin, xmax, Nx)
#    z_real = numpy.zeros_like(c_real)
#    z_imag = numpy.zeros_like(c_imag)
#    cdef numpy.ndarray[numpy.int16_t, ndim=2] divergence_steps
#    cdef int i, j, k, nx, ny, escape_time
#    nx = Nx
#    ny = Ny
#    escape_time = max_escape_time
#    divergence_steps = numpy.zeros([nx, ny], dtype=numpy.int16)
#    cdef double divergence, tmp_real, tmp_imag, tmp_real_squared, tmp_imag_squared
#    divergence = divergence_criteria
#    for k in range(nx):
#        for j in range(ny):
#            tmp_real_squared = z_real[k]*z_real[k]
#            tmp_imag_squared = z_imag[j]*z_imag[j]
#            for i in range(1, escape_time + 1):
#                if (tmp_real_squared + tmp_imag_squared) <= divergence:
#                    tmp_real = z_real[k]
#                    tmp_imag = z_imag[k]
#                    z_real[k] = tmp_real_squared - tmp_imag_squared + c_real[k]
#                    z_imag[k] = 2*tmp_real*tmp_imag + c_imag[k]
#                    tmp_real_squared = z_real[k]*z_real[k]
#                    tmp_imag_squared = z_imag[j]*z_imag[j]
#                    divergence_steps[k][j] = i
#    return divergence_steps
