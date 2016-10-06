from setuptools import setup, find_packages

setup(name="mandelbrot",
      version='0.1',
      description='Create mandelbrot sets',
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
              'mandelbrot=mandelbrot:silly',
          ],
      },
     )
