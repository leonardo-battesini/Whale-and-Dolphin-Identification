from msilib.schema import Error
import os
import logging

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

class Pp_vectorize:

    def pp_vectorize():
        """
        Recebe uma str com o nome da espécie (já contida nos Outputs) e retorna seu DF com os features.
        """
        root_dir = os.path.abspath(os.curdir)
        image_dir = root_dir + '\\train_images'
        output_dir = root_dir + '\\outputs\\embeddings' # + name_specie + '_pp'

        if not os.path.os.path.exists(image_dir):
            logging.warning(image_dir + ' not found! Please verify.')
            return 0

        if not os.path.os.path.exists(output_dir):
            os.makedirs(output_dir)
            logging.info(output_dir + ' folder created!')

        #TODO se o train_with_tags.csv não existir, chama o método que gera
        df = pd.read_csv(root_dir + '\\outputs\\train_with_tags.csv')
        
        return Pp_vectorize.generate_and_save_feature(df, image_dir, output_dir, True, 500)

    def get_image_and_resize(image_file_name, dir, resize = False, size = 0):
        """
        Recebe o nome do arquivo .JPG e o nome do diretório em que está e retorna a imagem como np.array. Entrar com resize = True e size = tamanho máximo em px pra uma imagem se quiser fazer um resize.
        """
        file_path = os.path.join(dir, image_file_name)
        
        if(resize == False):
            img = Image.open(file_path)
            return np.array(img)
        else:
            MAX_SIZE = (size, size)
            img = Image.open(file_path)
            img.thumbnail(MAX_SIZE)
            return np.array(img)

    def create_features(img):
        """
        All the information for a given image will be returned in a single row.
        """
        # flatten three channel color image
        color_features = img.flatten()

        # convert image to greyscale
        if img.ndim > 2:
            grey_image = rgb2gray(img)
        else:
            grey_image = img
        # get HOG features from greyscale image
        hog_features = hog(grey_image, block_norm='L2-Hys', pixels_per_cell=(16, 16))
        # combine color and hog features into a single array
        flat_features = np.hstack([color_features, hog_features])
        return flat_features

    def create_feature_matrix(label_dataframe, dir, image_dir = False, size = 0):
        features_list = []
        

        for i in range(len(label_dataframe.index)):
            img_name = label_dataframe.loc[i][0]
            # load image
            img = Pp_vectorize.get_image_and_resize(img_name, dir, image_dir, size)
            # get features for image
            print('create_feature_matrix(): ' + str(i+1) + '/' + str(len(label_dataframe.index)))
            image_features = Pp_vectorize.create_features(img)
            features_list.append(image_features)
            
        # convert list of arrays into a matrix
        feature_matrix = np.array(features_list)
        return feature_matrix

    def generate_and_save_feature(labeled_dataframe, image_dir, output_dir, resize = False, size = 0):
        cont = 0

        for i in range(len(labeled_dataframe.index)):
            img_file_name = labeled_dataframe.loc[i][0]
            # load image
            img = Pp_vectorize.get_image_and_resize(img_file_name, image_dir, resize, size)

            # get features for image
            print('create_feature_matrix(): ' + str(i+1) + '/' + str(len(labeled_dataframe.index)))
            image_features = Pp_vectorize.create_features(img)
            # save
            file_name_output = output_dir + '\\' + img_file_name[:-4]
            np.savetxt(file_name_output, image_features, delimiter=',')
            cont += 1
        return cont

print(Pp_vectorize.pp_vectorize())