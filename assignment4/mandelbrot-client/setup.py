from setuptools import setup, Extension
#from distutils.core import setup, Command
#from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
from os.path import abspath, dirname, join # Needed to get location of documentation

def documentation():
    with open(join(abspath(dirname(__file__)), 'README.rst'), 'r', encoding='utf-8') as f:
        return f.read()

extensions=[Extension("src.commands.mandelbrot", ["src/commands/mandelbrot.pyx"])]

setup(name="Mandelbrot",
      version='0.1',
      description='Hallo',
      long_description=documentation(),
      author=u'Øyvind Sigmundson Schøyen',
      packages=['src', 'src.commands'],
      ext_modules=extensions,
      cmdclass={'build_ext': build_ext},
      data_files=[('config', ['setup.cfg'])],
      test_suite='nose.collector',
      tests_require=['nose'],
     )
