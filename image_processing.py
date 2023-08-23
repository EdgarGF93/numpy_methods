import numpy as np
import matplotlib.pyplot as plt


PATH_LO = r"C:\Users\edgar1993a\Desktop\descarga.jpg"

class ImageProc():
    def __init__(self, path_image=PATH_LO) -> None:
        self.path_image = path_image
        self.image = plt.imread(path_image)

    def decompose_image(self):
        mat_r = self.image[:,:,0]
        mat_g = self.image[:,:,1]
        mat_b = self.image[:,:,2]
        mat_zero = np.copy(mat_r) * 0
        new_mat_r = np.dstack([mat_r, mat_zero, mat_zero])
        new_mat_g = np.dstack([mat_zero, mat_g, mat_zero])
        new_mat_b = np.dstack([mat_zero, mat_zero, mat_b])
        
        fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(15,15))
        mat_list = [self.image, new_mat_r, new_mat_g, new_mat_b]
        for _ in range(4):
            axes[_].imshow(mat_list[_])
            axes[_].set_xticks([])
            axes[_].set_yticks([])