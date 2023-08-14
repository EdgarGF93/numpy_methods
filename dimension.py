import numpy as np
import matplotlib.pyplot as plt


def display_intensities(mat, ax):
    n_rows = mat.shape[0]
    n_cols = mat.shape[1]

    for r in range(n_rows):
        for c in range(n_cols):
            label = str(mat[r,c])
            ax.text(c, r, label, color='white', ha='center', va='center')

def rgb_to_grey(color=(0,0,0)):
    r = color[0]
    g = color[1]
    b = color[2]
    grey_value = 0.299 * r + 0.587 * g + 0.114 * b
    return grey_value


def display_coordinates(mat, ax):
    n_rows = mat.shape[0]
    n_cols = mat.shape[1]

    for r in range(n_rows):
        for c in range(n_cols):
            label = f"({r},{c})"
            ax.text(c, r, label, color='white', ha='center', va='center')

def display_color_rgb(mat, ax):
    n_rows = mat.shape[0]
    n_cols = mat.shape[1]

    for r in range(n_rows):
        for c in range(n_cols):
            pixel_value = mat[r, c]
            label = f"({pixel_value[0]},{pixel_value[1]},{pixel_value[2]})"
            ax.text(c, r, label, color='white', ha='center', va='center')

def display_grey(mat, ax):
    n_rows = mat.shape[0]
    n_cols = mat.shape[1]

    for r in range(n_rows):
        for c in range(n_cols):
            pixel_value = mat[r, c]
            grey = rgb_to_grey(color=pixel_value)
            label = f"({grey})"
            ax.text(c, r, label, color='white', ha='center', va='center')


def kk():
    fig, ax = plt.subplots(figsize=(6,6))

    colors = np.linspace(0,255,5)

    mat_color = np.array(
        [
            [(0,ii,jj) for jj in colors] for ii in colors
        ]
    ).astype(int)

    ax.imshow(mat_color)
    display_grey(
        mat=mat_color,
        ax=ax,
    )
    plt.show()


if __name__ == '__main__':
    kk()