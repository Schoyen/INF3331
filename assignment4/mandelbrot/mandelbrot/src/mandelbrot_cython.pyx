import numpy as np
cimport numpy as np
cimport cython
from cpython.mem cimport PyMem_Malloc, PyMem_Free

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef np.ndarray[np.uint8_t, ndim=2] mandelbrot_set_cython(
        double xmin, double xmax, double ymin, double ymax, unsigned int Nx, unsigned int Ny,
        unsigned int max_escape_time, double divergence_criteria):
    cdef double c_real, c_imag, z_real, z_imag
    cdef unsigned int i, j, k
    cdef double dx = (xmax - xmin)/float(Nx - 1)
    cdef double dy = (ymax - ymin)/float(Ny - 1)

    # Allocate memory for matrix with escape times
    cdef int **divergence_steps = <int **>PyMem_Malloc(Ny * sizeof(int *))
    divergence_steps[0] = <int *>PyMem_Malloc(Nx*Ny * sizeof(int))
    # Make memory contiguous
    for i in range(1, Ny):
        divergence_steps[i] = divergence_steps[i - 1] + Nx
    # Set all elements in memory to zero (PyMem_Calloc did not work on my computer)
    for j in range(Ny):
        for i in range(Nx):
            divergence_steps[j][i] = 0

    cdef double div = divergence_criteria**2

    for j in range(Ny):
        c_imag = ymin + j*dx
        for i in range(Nx):
            c_real = xmin + i*dx
            z_real = 0.0
            z_imag = 0.0
            for k in range(1, max_escape_time + 1):
                z_real, z_imag = (z_real*z_real - z_imag*z_imag + c_real, 2*z_real*z_imag + c_imag)
                if (z_real*z_real + z_imag*z_imag) > div:
                    break
                divergence_steps[j][i] = k
    # Create numpy array used to return values to Python caller
    cdef np.ndarray[np.uint8_t, ndim=2] divergence_steps_np
    divergence_steps_np = np.zeros([Ny, Nx], dtype=np.uint8)
    # Copy elements from allocated memory to numpy array
    for i in range(Nx):
        for j in range(Ny):
            divergence_steps_np[j][i] = divergence_steps[j][i]
    # Free allocated memory
    PyMem_Free(divergence_steps[0])
    PyMem_Free(divergence_steps)
    return divergence_steps_np
