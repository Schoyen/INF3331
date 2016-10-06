
def display_help():
    return """
mandelbrot

Synopsis:
    A command line interface for controlling three different Python implementations
    computing and displaying the Mandelbrot. The three different implementations are
    written using Python, Python with Numpy vectorization and Cython.

Options:
    -h --help                       Display this help message
    -c --cython                     Use Cython implementation
    -p --python                     Use Python implementation
    -n --numpy                      Use Numpy implementation

Usage:
    mandelbrot -[cpn] xmin xmax ymin ymax Nx Ny filename

Here 'filename' is optional
"""
