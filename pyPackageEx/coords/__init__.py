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
