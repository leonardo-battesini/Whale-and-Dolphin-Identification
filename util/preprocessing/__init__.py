import os
import shutil
import pandas
from PIL import Image
from pathlib import Path
import tensorflow as tf

from util import FileOps


class ImgPreprocess(FileOps):
    
    def resize_image(self, image_file_path:str, new_size_in_pix:tuple, grayscale:bool = False):
        img = self.read_image(image_file_path)

        if(grayscale==True):
          img = img.convert(mode='L')

        img = img.resize(new_size_in_pix)

        return img    
    
   
    def set_dir_structure(self, img_base_dir:str, dataframe)->None:
      '''
      Set train folder structure to:
              main_directory/
              class_a/
                  a_image_1.jpg
                  a_image_2.jpg
              class_b/
                  b_image_1.jpg
                  b_image_2.jpg
      '''
      species = dataframe['species'].unique()
      for each_species in species:  
        figs_to_be_moved = dataframe[dataframe['species']==each_species]['image']  
        base_save_dir = img_base_dir+f'/{each_species}'
        self.create_dir(base_save_dir)
        
        for each_fig in figs_to_be_moved.iteritems():
          current_dir = img_base_dir+f'/{each_fig[1]}' 
          destination_dir =  base_save_dir+f'/{each_fig[1]}'

          if ('jpg' in current_dir):
            shutil.move(current_dir, destination_dir)
            print(f'moved from {current_dir}, to {destination_dir}')

      
    def create_img_training_dataset(base_dir:str, **kwargs):
        base_dir = Path(base_dir)
        return tf.keras.utils.image_dataset_from_directory(base_dir, **kwargs)


