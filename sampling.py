import numpy as np
import matplotlib.pyplot as plt
from dimension import display_color_rgb, display_grey

def generate_noise_grey_map(rows=3, cols=3):
    g_noise = np.random.randint(low=0, high=255, size=(rows, cols), dtype=int)
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

def get_histogram(map, n_bins=10):
    counts, bins = np.histogram(map, bins=n_bins)
    return counts, bins

def plot_histogram(ax, map, n_bins=10, label='', color='black'):
    counts, bins = get_histogram(map=map, n_bins=n_bins)
    ax.hist(bins[:-1], bins, weights=counts, histtype='step', label=label, color=color)    


def plot_noise_grey(rows=3, cols=3, labels=False, show_map=True, show_hist=True, n_bins=10):
    noise_map = generate_noise_map(
        rows=rows,
        cols=cols,
        grey=True,
    )
    fig, axes = plt.subplots(ncols=2, nrows=1)
    ax_map = axes[0]
    ax_hist = axes[1]

    if labels:
        display_grey(mat=noise_map, ax=ax_map)

    if show_map:
        ax_map.imshow(noise_map, cmap='Greys')
    
    if show_hist:
        plot_histogram(
            ax=ax_hist,
            map=noise_map,
            n_bins=n_bins,
            label='grey',
        )
    plt.show()

def plot_noise_rgb(rows=3, cols=3, labels=False, show_map=True, show_hist=True, n_bins=10):

    noise_map = generate_noise_map(
        rows=rows,
        cols=cols,
        grey=False,
    )

    fig, axes = plt.subplots(ncols=2, nrows=1)
    ax_map = axes[0]
    ax_hist = axes[1]

    if labels:
        display_color_rgb(mat=noise_map, ax=ax_map)

    if show_map:
        ax_map.imshow(noise_map, cmap='BrBG')
    
    if show_hist:
        plot_histogram(
            ax=ax_hist,
            map=noise_map[:,:,0],
            n_bins=n_bins,
            label='red',
            color='red',
        )

        plot_histogram(
            ax=ax_hist,
            map=noise_map[:,:,1],
            n_bins=n_bins,
            label='green',
            color='green',
        )

        plot_histogram(
            ax=ax_hist,
            map=noise_map[:,:,2],
            n_bins=n_bins,
            label='blue',
            color='blue',
        )


    plt.show()








if __name__ == '__main__':
    square = 100
    n_bins = 50
    plot_noise_rgb(square, square, show_map=True, n_bins=n_bins)