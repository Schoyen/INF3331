from . import silly
from .usage import display_help
from sys import argv
from .src import MandelbrotPython, MandelbrotNumpy, MandelbrotCython

def main():
    print (u"This is main\nNow calling silly() in __init__.py...")
    silly()
    print ("These are your command line arguments")
    print (argv)
    print (display_help())

