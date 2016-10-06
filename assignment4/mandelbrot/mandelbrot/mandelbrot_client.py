from . import silly
from sys import argv

def main():
    print (u"This is main\nNow calling silly() in __init__.py...")
    silly()
    print ("These are your command line arguments")
    print (argv)
