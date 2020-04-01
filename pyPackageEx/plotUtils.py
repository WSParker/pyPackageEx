from matplotlib.pyplot import figure,xlabel,ylabel,imshow,show,savefig

def plot(set, fname = None, extent = None, cmap='gist_heat'):
    """
    Imshows a 2D input. Saves if fname is given.
    """
    figure(dpi=300)
    xlabel('Re(z)')
    ylabel('Im(z)')
    if extent is None:
        imshow(set, cmap = cmap)
    else:
        imshow(set, cmap = cmap, extent = extent)
    if fname is None:
        show()
    else:
        savefig(fname)
