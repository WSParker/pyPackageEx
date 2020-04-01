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
