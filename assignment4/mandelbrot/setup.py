from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

def read_doc():
    """Function used for long description in setup."""
    with open("README.md", 'r') as f:
        return f.read()

setup(name="mandelbrot",
      version='0.1',
      description='Create mandelbrot sets',
      long_description=read_doc(),
      author=u'Øyvind Sigmundson Schøyen',
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ],
      packages=find_packages(),
      ext_modules=cythonize(
          [
              Extension("mandelbrot.src.mandelbrot_cython", ["mandelbrot/src/mandelbrot_cython.pyx"])
              ]
      ),
      entry_points={
          'console_scripts': [
              'mandelbrot=mandelbrot.mandelbrot_client:main',
          ],
      },
)
