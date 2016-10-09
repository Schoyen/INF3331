import numpy as np
cimport numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef np.ndarray[np.uint8_t, ndim=2] mandelbrot_set_cython(
        double xmin, double xmax, double ymin, double ymax, int Nx, int Ny,
        int max_escape_time, int divergence_criteria):
    cdef double dx, dy, c_real, c_imag, z_real, z_imag, div
    cdef int i, j, k
    dx = (xmax - xmin)/float(Nx - 1)
    dy = (ymax - ymin)/float(Ny - 1)
    cdef np.ndarray[np.uint8_t, ndim=2] divergence_steps
    divergence_steps = np.zeros([Ny, Nx], dtype=np.uint8)
    div = divergence_criteria**2

    for i in range(Nx):
        c_real = xmin + i*dx
        for j in range(Ny):
            c_imag = ymin + j*dx
            z_real = 0.0
            z_imag = 0.0
            for k in range(1, max_escape_time + 1):
                z_real, z_imag = (z_real*z_real - z_imag*z_imag + c_real, 2*z_real*z_imag + c_imag)
                if (z_real*z_real + z_imag*z_imag) > div:
                    break
                divergence_steps[j][i] = k
    return divergence_steps
