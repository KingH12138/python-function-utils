import imageio
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import os


def science_plot_gif(X, Y, figsize, save_dir, filename, xlabel='x', ylabel='y', color='b', interval=100, repeat_delay=1000):
    """

    The function can generator according to input data.
    The gif's sample rate is 1——a gif's frame means the
    combinaton of an item and the items before it.

    Args:

    X,Y:two numpy.ndarray with same size like (length,)

    figsize:the figure of gif(inch).must be  a tuple.

    save_dir:gif's save dir.str types.

    filename:gif file's name that ends with .jpg,etc.str type.

    xlabel,ylabel:set gif's axis label.str type.

    interval:the duration between two frames.

    repeat_delay:repeating gif's duration.

    """

    ims = []
    fig = plt.figure(figsize=figsize)
    axes = fig.gca()
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.grid()
    point_num = len(X)
    for i in range(point_num):
        x = X[:i + 1]
        y = Y[:i + 1]
        im = axes.plot(x, y, color)
        ims.append(im)
    ani = animation.ArtistAnimation(fig, ims, interval=interval, repeat_delay=repeat_delay)
    ani.save(save_dir + '/' + filename, 'pillow')

def imageio_gif(imgs_dir, save_path, duration=0.5):
    dir_path = imgs_dir
    imgs = []
    for filename in os.listdir(dir_path):
        filepath = dir_path + '/' + filename
        img = imageio.imread(filepath)
        imgs.append(img)
    imageio.mimsave(save_path, imgs, "GIF", duration=0.5)



