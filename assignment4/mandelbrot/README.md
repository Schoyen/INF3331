# Mandelbrot Python and Cython package

## Installation
To install in the default location run
```shell
sudo python setup.py install
```
For other pre-defined locations run
```shell
python setup.py install --prefix=/path/to/location
```
Make sure that you set PYTHONPATH and PATH to this location.

```shell
export PATH=/path/to/location/bin:$PATH
export PYTHONPATH=/path/to/location/lib/python3.x/site-packages:$PYTHONPATH
```
where `python3.x` is set to your version of Python 3.

## Running
Typing
```shell
mandelbrot -h
```
on the shell shows the instructions on how to use the module.

## Known issues
If the module is installed on a system trying to import the packages does not work
while the user is in the `mandelbrot/` dir.
