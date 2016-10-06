from setuptools import setup, find_packages

def read_doc():
    with open("README.rst", 'r') as f:
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
      entry_points={
          'console_scripts': [
              'mandelbrot=mandelbrot.mandelbrot_client:main',
          ],
      },
     )
