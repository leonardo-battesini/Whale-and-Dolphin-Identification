import os

import matplotlib as mpl
import matplotlib.pyplot as plt
from IPython.display import display
from PIL import Image

import pandas as pd
import numpy as np

# import Image from PIL
from PIL import Image

from skimage.feature import hog
from skimage.color import rgb2gray

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# import train_test_split from sklearn's model selection module
from sklearn.model_selection import train_test_split

# import SVC from sklearn's svm module
from sklearn.svm import SVC

# import accuracy_score from sklearn's metrics module
from sklearn.metrics import roc_curve, auc, accuracy_score

root_dir = os.path.abspath(os.curdir)
image_dir = root_dir +'\\outputs'

def get_image_and_resize(id_image, dir_name, resize = False, size = 0):
    """
    Recebe o nome do arquivo .JPG e o nome do diretório em que está e retorna a imagem como np.array. Entrar com resize = True e size = tamanho máximo em px pra uma imagem se quiser fazer um resize.
    """
    dir = image_dir + '\\' + dir_name
    filename = "{}.jpg".format(id_image)
    file_path = os.path.join(dir, filename)
    
    if(resize == False):
        img = Image.open(file_path)
        return np.array(img)
    else:
        MAX_SIZE = (size, size)
        img = Image.open(file_path)
        img.thumbnail(MAX_SIZE)
        return np.array(img)

#show the corresponding image of a Bombus
#plt.imshow(get_image('00db5ec9e46a3d', 'super_raros'))
#plt.show()

def turn_grey(img):
    """
    Recebe uma imagem e retorna ela com escala de cinza como np.array. plt.imshow(turn_grey(grey_photo), cmap=mpl.cm.gray)
    """
    grey_photo = rgb2gray(img)

    return grey_photo

#photo = get_image('00db5ec9e46a3d', 'super_raros')
#plt.imshow(turn_grey(photo), cmap=mpl.cm.gray)
#plt.show()

############### pra cima tá ok

def turn_hog(img):

    # run HOG using greyscale images
    hog_features, hog_image = hog(img,
                                visualize=True,
                                block_norm='L2-Hys',
                                pixels_per_cell=(16, 16))
    return hog_image

def create_features(img):
    """
    All the information for a given image will be returned in a single row.
    """
    # flatten three channel color image
    color_features = img.flatten()
    # convert image to greyscale
    grey_image = rgb2grey(img)
    # get HOG features from greyscale image
    hog_features = hog(grey_image, block_norm='L2-Hys', pixels_per_cell=(16, 16))
    # combine color and hog features into a single array
    flat_features = np.hstack([color_features, hog_features])
    return flat_features

#photo = get_image_and_resize('00db5ec9e46a3d', 'super_raros', True, 300)
#photo = turn_grey(photo)
#photo = turn_hog(photo)
#plt.imshow(photo, cmap=mpl.cm.gray)
#plt.show()
