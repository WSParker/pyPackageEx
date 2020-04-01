
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

- [Why create a package?](#why-create-a-package)
- [Goal](#goal)
- [Components of a package](#components-of-a-package)
  - [`__init__.py`](#__init__py)
  - [`setup.py`](#setuppy)
  - [`.gitignore`](#gitignore)
  - [`LICENSE`](#license)
  - [`README.md`](#readmemd)

<!-- /code_chunk_output -->
# Why create a package?

The obvious answer is, create a package if you want to publish code to the Python Package Index (PyPI) so that others can `pip install` it.

However, even if you're writing code only for yourself, or for yourself and a few other people, there are benefits to packaging it:

* Packages are easy to install and use.
* Packaging your code forces it to be simple and organized, even for large projects with lots of functionality.
* The code you write is a part of your portfolio. Potential employers will look at your GitHub, and neat packages say much more than a mess of `.py`'s and notebooks.

# Goal

We have two files - `manSetGen.py` and `plotUtils.py` - that contain code to generate Mandelbrot sets and plot them, respectively. We want to upload them to GitHub so that somebody can run this install:

```Bash
git clone pyPackageEx
cd pyPackageEx
Python setup.py develop
```
And these imports:

```Python
import pyPackageEx as ppe
from pyPackageEx import plotUtils
```

Note: once you have a package it's [easy to publish to PyPI](https://packaging.Python.org/tutorials/packaging-projects/) (Python Package Index), and if you choose to do so then installation becomes
```bash
pip install pyPackageEx
```

# Components of a package
The structure of this folder is as follows:
```
pyPackageEx/                       Repository containing the package
     pyPackageEx/                  The package
          __init__.py
          manSetGen.py             Primary module
          plotUtils.py             A helper module
          coords/                  A subpackage
               __init__.py
     .gitignore
     README.md
     setup.py
```

This is close to the minimal structure of a Python package, with a subpackage (the .gitignore is extra, see [below](#gitignore)).

The versatility of packages comes from the `__init__.py` file. It behaves in packages a bit like the `__init__` method of Python classes - it defines elements and attributes of the package.

Here are the key components of a Python package.

## `__init__.py`

The existence of an `__init__.py` tells Python the enclosing folder is a package. So, this repository has one package `pyPackageEx` (containing two modules) and one subpackage `pyPackageEx.coords`. In addition, `__init__.py` is run every time the package is imported, so it can include code to initialize the package.

In `pyPackageEx/__init__.py`, we have:
```Python
## myPackageEx/__init__.py
from .manSetGen import *
```
This means when we run
```Python
import pyPackageEx
```
`pyPackageEx` inherits all the attributes of `manSetGen.py` - its functions, global variables, imported attributes, etc. So if `mandelbrot()` is a function defined within `manSetGen.py`, we can run:
```Python
pyPackageEx.mandelbrot(z)
```

However, because we don't explicitly import anything from `plotUtils.py`, `pyPackageEx` does not inherit any of its attributes. Thus, the following line is not valid:
```Python
pyPackageEx.plot(manSet)
```
where `plot()` is a function defined in `plotUtils.py`.

**Note**: the import syntax is slightly different in packages. A single dot indicates the current package, two represents the parent package.

Lastly, we have `pyPackageEx/coords/__init__.py`:
```Python
## myPackageEx/coords/__init__.py
from numpy import linspace, meshgrid

def cp(xmin = -1.5, xmax = 1.5, xres = 2**10,
            ymin = -1.5, ymax = 1.5, yres = 2**10):
    X = linspace(xmin,xmax,xres)
    Y = linspace(ymin,ymax,yres)
    x, y = meshgrid(X,Y)
    z = x + 1j*y
    return(z)
```
Here we used the `__init__.py` file to directly define attributes of the package, so that we can run:
```Python
from pyPackageEx import coords
z = coords.cp()
```

There are two main highlights to this kind of structuring:

First, you can be explicit about how much of the package gets imported with each import statement. For large packages (for example, `scipy`), it's important to only load what is necessary, and this is built directly into the import structure of the package.

Second, you have flexibility with intra-package references. For example, in one of my packages I defined a bunch of constants in the main package's `__init__.py`, and I use them throughout the rest of the package.

If you have something you want to do within a package, and it isn't explained here, it might be explained in one of these:

[The Python docs](https://docs.Python.org/3/tutorial/modules.html#packages)
["How to create a Python Package with \_\_init\_\_.py" by Timothy Bramlett](https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html)

## `setup.py`

This is more straightforward. The file included in this repository reads:
```Python
from setuptools import setup, find_packages

setup(
    name = 'pyPackageEx',
    packages = find_packages(),
    author = 'William Parker',
    author_email = 'wparker4@uoregon.edu',
    description = 'Example Python package. ',
    url = 'https://github.com/WSParker/pyPackageEx',
    license = 'MIT',
    long_description = open('README.md').read(),
    long_description_content_type = "text/markdown",
    python_requires='>=3.6'
)
```
`find_packages()` looks for `__init__.py` files. Make sure the name matches the name of the package, and the url matches the url of the repository (particularly if publishing to PyPI).

## `.gitignore`
This tells git what to ignore when you upload your project; typically, generated files such as `__pycache__` go in the `.gitignore`. For more see [the documentation](https://git-scm.com/docs/gitignore).

## `LICENSE`
This tells users what they can and cannot do with your package. The most common are GNU and MIT, with MIT allowing users to create closed-source code from your package, and GNU not. More info [here](https://choosealicense.com/).

## `README.md`
The `README` is the first thing someone sees when they look at your package. It should contain
* a **concise** explanation of your package's purpose
* installation instructions
* basic usage instructions.

After that, there's room to include demos, extended usage, etc as you feel necessary.