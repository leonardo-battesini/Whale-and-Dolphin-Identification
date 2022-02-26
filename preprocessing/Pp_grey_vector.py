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

def get_image(id_image, dir_name):
    """
    Recebe o nome do arquivo .JPG e o nome do diretório em que está e retorna a imagem como np.array. 
    """
    dir = image_dir + '\\' + dir_name
    filename = "{}.jpg".format(id_image)
    file_path = os.path.join(dir, filename)
    img = Image.open(file_path)
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

def turn_hog(image):

    MAX_SIZE = (100, 100) 
    #img = Image.new(image) #imagem não está ficando pequena
    img.thumbnail(MAX_SIZE)

    # run HOG using our greyscale bombus image
    hog_features, hog_image = hog(img,
                                visualize=True,
                                block_norm='L2-Hys',
                                pixels_per_cell=(16, 16))

    # show our hog_image with a grey colormap
    plt.imshow(hog_image, cmap=mpl.cm.gray)
    plt.show()

#photo = get_image('00db5ec9e46a3d', 'super_raros')
#photo = turn_grey(photo)
#print(type(photo))
#turn_hog(photo)
#plt.show()