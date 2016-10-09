import numpy as np
cimport numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef np.ndarray[np.int16_t, ndim=2] mandelbrot_set_cython(
        double xmin, double xmax, double ymin, double ymax, int Nx, int Ny,
        int max_escape_time, int divergence_criteria):
        cdef np.ndarray[np.double_t, ndim=1] c_real, c_imag
        c_real = np.linspace(xmin, xmax, Nx)
        c_imag = np.linspace(ymin, ymax, Ny)
        cdef np.ndarray[np.int16_t, ndim=2] divergence_steps
        divergence_steps = np.zeros([Nx, Ny], dtype=np.int16)
        cdef int i, j, k
        cdef double z_real, z_imag, z_imag_squared, z_real_squared
        for i in range(Nx):
            for j in range(Ny):
                z_real = 0
                z_imag = 0
                z_real_squared = z_real*z_real
                z_imag_squared = z_imag*z_imag
                while divergence_steps[i][j] < max_escape_time:
                    divergence_steps[i][j] += 1
                    z_real = z_real_squared - z_imag_squared + c_real[i]
                    z_imag = 2*z_real*z_imag + c_imag[j]
                    z_real_squared = z_real*z_real
                    z_imag_squared = z_imag*z_imag
                    if (z_real_squared + z_imag_squared) < divergence_criteria:
                        break
        return divergence_steps

##cpdef numpy.ndarray[numpy.int16_t, ndim=2] mandelbrot_set_cython(
#        double xmin, double xmax, double ymin, double ymax, int Nx, int Ny,
#        int max_escape_time, int divergence_criteria):
#    cdef double c_real, c_imag, z_real, z_imag, dx, dy
#    cdef double z_imag_squared, z_real_squared, abs_z_squared
#    cdef int i, j, k
#    cdef numpy.ndarray[numpy.int16_t, ndim=2] divergence_steps
#    divergence_steps = numpy.zeros([Nx, Ny], dtype=numpy.int16)
#    dx = (xmax - xmin)/float(Nx - 1)
#    dy = (ymax - ymin)/float(Ny - 1)
#    for j in range(Ny):
#        for i in range(Nx):
#            z_real = c_real = xmin + i*dx
#            z_imag = c_imag = ymin + j*dy
#            z_real_squared = z_real*z_real
#            z_imag_squared = z_imag*z_imag
#            abs_z_squared = z_real_squared + z_imag_squared
#            while divergence_steps[j][i] < max_escape_time and abs_z_squared < divergence_criteria:
#                divergence_steps[j][i] += 1
#                z_real = z_real_squared - z_imag_squared + c_real
#                z_imag = 2*z_real*z_imag + c_imag
#                z_real_squared = z_real*z_real
#                z_imag_squared = z_imag*z_imag
#                abs_z_squared = z_real_squared + z_imag_squared
#    return divergence_steps


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
