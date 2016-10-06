from .usage import display_help
from sys import argv
from .src import MandelbrotPython, MandelbrotNumpy, MandelbrotCython
from argparse import ArgumentParser

def main():
    description = """
    A command line interface for controlling three different Python implementations
    computing and displaying the Mandelbrot. The three different implementations are
    written using Python, Python with Numpy vectorization and Cython.
    """
    parser = ArgumentParser(description=description)
    parser.add_argument("-c", "--cython", help="Create the Mandelbrot set using Cython")
    parser.parse_args()
#    mc = MandelbrotClient(argv)
#    mc()

class MandelbrotClient:

    def __init__(self, args):
        self.args = args
        self.valid_commands = []
        for i in display_help().split():
            if i == "Usage:":
                break
            if i.startswith("-"):
                self.valid_commands.append(i)
        self.commands = {"help": display_help,
                "cython": MandelbrotCython,
                "python": MandelbrotPython,
                "numpy": MandelbrotNumpy}

    def __call__(self):
        if len(self.args) < 2:
            print(display_help())
        else:
            if self.args[1] in self.valid_commands:
                pass
            else:
                print("mandelbrot: command not found: %s" % self.args[1])
