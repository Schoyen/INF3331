from setuptools import setup, Command, Extension
#from distutils.core import setup, Command
#from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
from os.path import abspath, dirname, join # Needed to get location of documentation

class ExecuteTests(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print ("Hello, World!")

with open(join(abspath(dirname(__file__)), 'README.rst'), 'r', encoding='utf-8') as f:
    documentation = f.read()

extensions=[Extension("src.commands.mandelbrot", ["src/commands/mandelbrot.pyx"])]

setup(name="Mandelbrot",
      version='0.1',
      description='Hallo',
      long_description=documentation,
      author=u'Øyvind Sigmundson Schøyen',
      packages=['src', 'src.commands'],
      ext_modules=extensions,
      entry_points={
          'console_scripts': ['mandelbrot=src.command_client.py:main',],
          },
      cmdclass={'build_ext': build_ext, 'test': ExecuteTests},
      data_files=[('config', ['setup.cfg'])],
     )
