# pyPackageEx
This example package demonstrates how and why to make a Python package out of individual modules (```.py``` files). See [the lesson](lesson.md).

## Installation
```
git clone https://github.com/WSParker/pyPackageEx
cd pyPackageEx
python setup.py develop
```
Run `python setup.py develop` if you plan to edit this module, otherwise run `python setup.py install`.

## Usage
Basically all this package can do is generate Mandelbrot sets and plot them.
```
import pyPackageEx as ppe
from pyPackageEx import plotUtils
from pyPackageEx import coords

xmin,xmax,ymin,ymax = -1.5, 1.5, -1.5, 1.5
z = coords.cp(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax)
extent = [xmin,xmax,ymin,ymax]

manSet = ppe.mandelbrot(z)
plotUtils.plot(manSet, extent=extent, cmap='bone')
```
Output:
!["Mandelbrot Set"](lib/dummy.png)
