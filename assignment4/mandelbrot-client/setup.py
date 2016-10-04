from distutils.core import setup, Extension
from Cython.Distutils import build_ext

setup(name="Mandelbrot",
      version='0.1',
      author=u'Øyvind Sigmundson Schøyen',
      packages=['src', 'src.commands', 'src.tests'],
      ext_modules=[Extension("mandelbrot", ["src/commands/mandelbrot.pyx"])],
      cmdclass={'build_ext': build_ext},
      data_files=[('config', ['setup.cfg'])],
     )
