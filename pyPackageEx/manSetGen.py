from numpy import abs, zeros_like

def mandelbrot(c, max_iter=50, div_lim=2):
    """
    Calculates a rough divergence time for complex number c.
    """
    f = 0j
    n = 0
    out = zeros_like(c,dtype=int)
    while n < max_iter:
        n += 1
        f = func(f,c)
        out[(out == 0) & (abs(f) > div_lim)] = n
        f[(out != 0)] = 100
    return(out)

def func(f,c):
    """
    The usual function for the Mandelbrot set.
    """
    return(f**2+c)
