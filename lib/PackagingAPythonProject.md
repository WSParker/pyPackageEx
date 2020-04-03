# Packaging a Python project

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

- [Why create a package?](#why-create-a-package)
- [Goal](#goal)
- [Core components of a package](#core-components-of-a-package)
    - [`__init__.py`](#__init__py)
    - [`setup.py`](#setuppy)
    - [`README.md`](#readmemd)
    - [`.gitignore`](#gitignore)
    - [`LICENSE`](#license)
    - [Extras](#extras)
- [Further Reading](#further-reading)

<!-- /code_chunk_output -->
## Why create a package?

The obvious answer is, create a package if you want to publish code to the Python Package Index (PyPI).

However, even if you're writing code only for yourself or for a small group, there are benefits to packaging it:

* Packages are easy to install and use.
* Packaging your code forces it to be simple and organized, even for large projects with lots of functionality.
* The code you write is a part of your portfolio. Potential employers will look at it, and neat packages look better than a mess of `.py`'s, notebooks, and miscellaneous files.

## Goal

We have two files - `manSetGen.py` and `plotUtils.py` - that contain code to generate Mandelbrot sets and plot them, respectively. We want to upload them to GitHub so that a user can run this install:

```Bash
$ pip install git+https://github.com/WSParker/pyPackageEx
```
and these imports:

```Python
import pyPackageEx as ppe
from pyPackageEx import plotUtils
```

Note: once you have a package it's [easy to publish to PyPI](https://packaging.Python.org/tutorials/packaging-projects/), and if you choose to do so then installation becomes
```Bash
$ pip install pyPackageEx
```

## Core components of a package
The structure of this repository is as follows:
```
pyPackageEx/                       Repository containing the package
     pyPackageEx/                  The package
          __init__.py
          manSetGen.py             Primary module
          plotUtils.py             A helper module
          coords/                  A subpackage
               __init__.py
     LICENSE
     .gitignore
     README.md
     setup.py
```

This is close to the minimal structure of a Python package, with a subpackage.

The versatility of packages comes from the `__init__.py` file. It behaves in packages a bit like the `__init__` method of Python classes - it defines the elements and attributes of the package.

Below are the key components of a Python package.

#### `__init__.py`

The existence of an `__init__.py` tells Python the enclosing folder is a package. So, this repository has one package `pyPackageEx` (containing two modules) and one subpackage `pyPackageEx.coords`. `__init__.py` is run every time the package is imported, so it can include code to initialize the package.

For example, in `pyPackageEx/__init__.py`, we have:
```Python
#### pyPackageEx/__init__.py
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

However, because we don't explicitly import anything from `plotUtils.py`, `pyPackageEx` does not inherit any of its attributes. Thus, if `plot()` is a function defined within `plotUtils.py`, we would need to run:
```Python
from pyPackageEx import plotUtils
plotUtils.plot(manSet)
# import pyPackageEx.plotUtils          Also works
# pyPackageEx.plotUtils.plot(manSet)
```

**Note**: intra-package import syntax is slightly different. A single dot indicates the current package, two represents the parent package.

Lastly, we have `pyPackageEx/coords/__init__.py`:
```Python
#### pyPackageEx/coords/__init__.py
from numpy import linspace, meshgrid

def cp(xmin = -1.5, xmax = 1.5, xres = 2**10,
            ymin = -1.5, ymax = 1.5, yres = 2**10):
    """
    Defines a complex plane (returns 2D numpy array).
    """
    X = linspace(xmin,xmax,xres)
    Y = linspace(ymin,ymax,yres)
    x, y = meshgrid(X,Y)
    z = x + 1j*y
    return(z)
```
Here we used the `__init__.py` file to directly define attributes of the package (`linspace`, `meshgrid`, and `cp`), so that we can run:
```Python
from pyPackageEx import coords
z = coords.cp()
```

There are two main highlights to this kind of structuring:

First, you can be explicit about how much of the package gets imported with each import statement. For large packages, it's important to only load what is necessary, and this is built directly into the import structure of the package; for example, `import scipy` only loads a portion of the `scipy` package. To get the rest, you have to be explicit: `from scipy import ____`.

Second, you have flexibility with intra-package references. For example, in one of my packages I define physical constants in the main package's `__init__.py`, and I use them throughout the rest of the package.

If you have something you want to do within a package, and it isn't explained here, it's probably explained in one of these:

* [The Python docs](https://docs.Python.org/3/tutorial/modules.html##packages)

* ["How to create a Python Package with \_\_init\_\_.py" by Timothy Bramlett](https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html)

#### `setup.py`

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
    python_requires='>=3.6',
    install_requires=['numpy','matplotlib']
)
```
`setup.py` tells Python how to install the package. `find_packages()` looks for `__init__.py` files. `install_requires` should include all external packages that yours depends on.

With `setup.py`, you have a few options for installation:
1. You can use `pip` to install (see the [README](../README.md)). This copies the source code directly into your package library. In addition, `pip` will automatically install the dependencies you list in `install_requires`. (**Note:** If the main repository is not a GitHub repository, you may need a local copy of it.)
2. If you plan to edit a local copy of the package, you can run
     ```Bash
     $ python setup.py develop
     ```
     which creates a link from your python package library to your local copy.

Thorough descriptions of install options [here](http://naoko.github.io/your-project-install-pip-setup/) and [here](https://stackoverflow.com/questions/15724093/difference-between-python-setup-py-install-and-pip-install).

#### `README.md`
The `README` is the first thing someone sees when they look at your package. It should contain:
* a **concise** explanation of your package's purpose
* installation instructions
* basic usage instructions

After that, there's room to include demos, extended usage, etc. as you feel necessary.

#### `.gitignore`
This tells git what to ignore when you upload your project. Typically, generated files such as `__pycache__` go in the `.gitignore`. For more see [the documentation](https://git-scm.com/docs/gitignore).

#### `LICENSE`
This tells users what they can and cannot do with your package. In general, you should include a license no matter how small the package. The most common are GNU and MIT, with MIT allowing users to create closed-source code from your package, and GNU not. More info on how to choose the right license for your purpose [here](https://choosealicense.com/).

#### Extras

As your package gets larger, or if it's intended for widespread distribution, there are some extra elements you may want to include. Arguably the most important is a [test suite](https://docs.python-guide.org/writing/tests/). You may also want to include more extensive [documentation](https://docs.python-guide.org/writing/documentation/), and your `setup.py` file may need a bit [more](https://github.com/navdeep-G/setup.py) than the bare functional minimum.

## Further Reading
More on `__init__.py`:
* [The Python docs](https://docs.Python.org/3/tutorial/modules.html##packages)
* ["How to create a Python Package with \_\_init\_\_.py" by Timothy Bramlett](https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html)

More on package structure:
* [The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/structure/)

More on `setup.py` and installation:
* [A comparison of installation methods](http://naoko.github.io/your-project-install-pip-setup/)
* [A comparison of `python setup.py install` vs `pip install`](https://stackoverflow.com/questions/15724093/difference-between-python-setup-py-install-and-pip-install)
* [A more thorough example](https://github.com/navdeep-G/setup.py)

`.gitignore` documentation:
* https://git-scm.com/docs/gitignore

How to choose a license:
* https://choosealicense.com/

Intro to writing tests:
* https://docs.python-guide.org/writing/tests/

Intro to writing docs:
* https://docs.python-guide.org/writing/documentation/

How to publish to PyPi:
* https://packaging.Python.org/tutorials/packaging-projects/
