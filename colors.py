import matplotlib.pyplot as plt
import numpy as np
#########3

DICT_COLORS = {
    'black' : (0,0,0),
    'white' : (255,255,255),
    'lavender' : (0,230,250),
}

R = ('r', 'R', 'red', 'RED')
G = ('g', 'G', 'green', 'GREEN')
B = ('b', 'B', 'blue', 'BLUE')


def show_color(name_color='lavender'):
    fig = plt.figure(figsize=(6,6))
    fig.set_facecolor(np.array(DICT_COLORS[name_color]) / 255)
    plt.show()

def color_matrix():
    mat = np.array([
        [(0,0,0), (50,50,50)],
        [(100,100,100), (255,255,255)]
    ])
    plt.imshow(mat)
    plt.show()

def closecolor_matrix_red(init_color=(0,0,0), n_colors=20, step=10):
    r_color_init = init_color[0]
    g_color_init = init_color[1]
    b_color_init = init_color[2]

    new_color_r_0 = r_color_init - n_colors // 2 * step
    new_color_r_f = r_color_init + n_colors // 2 * step

    if new_color_r_0 < 0:
        new_color_r_f = new_color_r_f - new_color_r_0
        new_color_r_0 = 0

    new_colors_r = np.linspace(new_color_r_0, new_color_r_f, n_colors).astype(int)

    mat = np.array([
        [(ii, g_color_init, b_color_init) for ii in new_colors_r]
    ])

    plt.imshow(mat)
    plt.show()

def closecolor_matrix_green(init_color=(0,0,0), n_colors=20, step=10):
    r_color_init = init_color[0]
    g_color_init = init_color[1]
    b_color_init = init_color[2]

    new_color_g_0 = g_color_init - n_colors // 2 * step
    new_color_g_f = g_color_init + n_colors // 2 * step

    if new_color_g_0 < 0:
        new_color_g_f = new_color_g_f - new_color_g_0
        new_color_g_0 = 0

    new_colors_g = np.linspace(new_color_g_0, new_color_g_f, n_colors).astype(int)
    
    mat = np.array([
        [(r_color_init, ii, b_color_init) for ii in new_colors_g]
    ])

    plt.imshow(mat)
    plt.show()

def closecolor_matrix_blue(init_color=(0,0,0), n_colors=20, step=10):
    r_color_init = init_color[0]
    g_color_init = init_color[1]
    b_color_init = init_color[2]

    new_color_b_0 = b_color_init - n_colors // 2 * step
    new_color_b_f = b_color_init + n_colors // 2 * step

    if new_color_b_0 < 0:
        new_color_b_f = new_color_b_f - new_color_b_0
        new_color_b_0 = 0

    new_colors_b = np.linspace(new_color_b_0, new_color_b_f, n_colors).astype(int)
    
    mat = np.array([
        [(r_color_init, g_color_init, ii) for ii in new_colors_b]
    ])

    plt.imshow(mat)
    plt.show()

def get_new_colors(color_init=0, n_colors=20, step=10):

    new_color_0 = color_init - n_colors // 2 * step
    new_color_f = color_init + n_colors // 2 * step

    if new_color_0 < 0:
        new_color_f = new_color_f - new_color_0
        new_color_0 = 0

    new_colors = np.linspace(new_color_0, new_color_f, n_colors).astype(int)

    return new_colors




def closecolor_matrix_rg(init_color=(0,0,0), n_colors=20, step=10):

    r_color_init = init_color[0]
    g_color_init = init_color[1]
    b_color_init = init_color[2]

    r_colors_new = get_new_colors(
        color_init=r_color_init,
        n_colors=n_colors,
        step=step,
    )

    g_colors_new = get_new_colors(
        color_init=g_color_init,
        n_colors=n_colors,
        step=step,
    )

    mat = np.array(
        [
            [(r,g,b_color_init) for r in r_colors_new] for g in g_colors_new
        ]
    )

    plt.imshow(mat)
    plt.show()



def closecolor_matrix_rb(init_color=(0,0,0), n_colors=20, step=10):

    r_color_init = init_color[0]
    g_color_init = init_color[1]
    b_color_init = init_color[2]

    r_colors_new = get_new_colors(
        color_init=r_color_init,
        n_colors=n_colors,
        step=step,
    )

    b_colors_new = get_new_colors(
        color_init=b_color_init,
        n_colors=n_colors,
        step=step,
    )

    mat = np.array(
        [
            [(r,g_color_init,b) for r in r_colors_new] for b in b_colors_new
        ]
    )

    plt.imshow(mat)
    plt.show()

def closecolor_matrix_gb(init_color=(0,0,0), n_colors=20, step=10):

    r_color_init = init_color[0]
    g_color_init = init_color[1]
    b_color_init = init_color[2]

    g_colors_new = get_new_colors(
        color_init=g_color_init,
        n_colors=n_colors,
        step=step,
    )

    b_colors_new = get_new_colors(
        color_init=b_color_init,
        n_colors=n_colors,
        step=step,
    )

    mat = np.array(
        [
            [(r_color_init,g,b) for g in g_colors_new] for b in b_colors_new
        ]
    )

    plt.imshow(mat)
    plt.show()



def closecolor_matrix(init_color=(0,0,0), constant_color='b', n_colors=20, step=10):

    if constant_color in R:
        closecolor_matrix_gb(
            init_color=init_color,
            n_colors=n_colors,
            step=step,
        )
    elif constant_color in G:
        closecolor_matrix_rb(
            init_color=init_color,
            n_colors=n_colors,
            step=step,
        )
    elif constant_color in B:
        closecolor_matrix_rg(
            init_color=init_color,
            n_colors=n_colors,
            step=step,
        )
    else:
        return



if __name__ == '__main__':
    closecolor_matrix(
        init_color=(100,50,0),
        constant_color='r',
        n_colors=10,
        step=10,
    )