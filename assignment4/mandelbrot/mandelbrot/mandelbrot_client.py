from sys import argv
from argparse import ArgumentParser
from . import MandelbrotPython, MandelbrotCython, MandelbrotNumpy, compute_mandelbrot

def main():
    description = """
    A command line interface for controlling three different Python implementations
    computing and displaying the Mandelbrot. The three different implementations are
    written using Python, Python with Numpy vectorization and Cython.
    """
    implementation_map = {'cython': MandelbrotCython,
            'python': MandelbrotPython,
            'numpy': MandelbrotNumpy}
    parser = ArgumentParser(description=description)
    parent_parser = ArgumentParser(add_help=False)
    subparser = parser.add_subparsers(help="commands")
    parent_parser.add_argument("coords", metavar='args', type=float, nargs=4,
            help="The coordinates for the Mandelbrot set (xmin, xmax, ymin, ymax)")
    parent_parser.add_argument("steps", metavar='steps', type=int, nargs=2,
            help="The number of steps in x and y direction (Nx, Ny)")
    parent_parser.add_argument("-f", "--filename", metavar="filename", type=str, nargs='?',
            help="The path and filename of an image with the mandelbrot set")
    parent_parser.add_argument("-e", "--escape-time", metavar="escape-time", type=int, nargs='?',
            help="The max escape time before determining convergence (default=1000)", default=1000)
    parent_parser.add_argument("-d", "--divergence-criteria", metavar="divergence-criteria", type=int, nargs='?',
            help="The divergence criteria for the Mandelbrot set (default=2)", default=2)
    python_parser = subparser.add_parser('python', help='Create the Mandelbrot set using Python', parents=[parent_parser])
    python_parser.set_defaults(func=MandelbrotPython)
    cython_parser = subparser.add_parser('cython', help='Create the Mandelbrot set using Cython', parents=[parent_parser])
    cython_parser.set_defaults(func=MandelbrotCython)
    numpy_parser = subparser.add_parser('numpy', help='Create the Mandelbrot set using Numpy', parents=[parent_parser])
    numpy_parser.set_defaults(func=MandelbrotNumpy)
    args = parser.parse_args()
    arg_list = args.coords + args.steps
    compute_mandelbrot(*arg_list, plot_filename=args.filename, max_escape_time=args.escape_time, divergence_criteria=args.divergence_criteria)
