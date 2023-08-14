import numpy as np
import matplotlib.pyplot as plt
from dimension import display_color_rgb, display_grey

def generate_noise_grey_map(rows=3, cols=3):
    g_noise = np.random.randint(255, size=(rows, cols))
    return g_noise

def generate_noise_rgb_map(rows=3, cols=3):
    r_noise = np.random.randint(255, size=(rows, cols))
    g_noise = np.random.randint(255, size=(rows, cols))
    b_noise = np.random.randint(255, size=(rows, cols))

    # Merge the three matrix in a (rows, cols, 3) matrix
    rgb_noise = np.dstack((r_noise, g_noise, b_noise))

    return rgb_noise

def generate_noise_map(rows=3, cols=3, grey=False):
    if grey:
        noise = generate_noise_grey_map(rows=rows, cols=cols)
    else:
        noise = generate_noise_rgb_map(rows=rows, cols=cols)
    return noise


def plot_noise(rows=3, cols=3, grey=False, labels=False, show_map=True, show_hist=True, bins=100):

    noise_map = generate_noise_map(
        rows=rows,
        cols=cols,
        grey=grey,
    )

    fig, axes = plt.subplots(ncols=2, nrows=1)
    ax_map = axes[0]
    ax_hist = axes[1]

    cmap = 'Greys' if grey else 'BrBG'
    
    if labels:
        if grey:
            display_grey(mat=noise_map, ax=ax_map)
        else:
            display_color_rgb(mat=noise_map, ax=ax_map)

    if show_map:
        ax_map.imshow(noise_map, cmap=cmap)
    
    if show_hist:
        hist, bin_edges = np.histogram(noise_map, bins=bins)
        ax_hist.hist(noise_map, bins=bins)
    
    
    plt.show()








if __name__ == '__main__':
    square = 100
    plot_noise(square,square,grey=True, bins=10)