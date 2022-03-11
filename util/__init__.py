import pandas
import shutil
from pathlib import Path
from PIL import Image


class FileOps:
  @staticmethod
  def read_csv(path_to_file:str, **kwargs)->pandas.DataFrame:
    try:
      return pandas.read_csv(path_to_file, **kwargs)
    
    except Exception as error:
      raise error


  @staticmethod
  def read_image(image_file_path:str):
      try:
          img = Image.open(image_file_path)
          return img

      except Exception as error:
        raise error


  @staticmethod
  def save_image(img, image_file_save_path:str)->None:
      base_dir = os.path.dirname(image_file_save_path)
      Path(base_dir).mkdir(parents=True, exist_ok=True)
      img.save(image_file_save_path)


  @staticmethod
  def create_dir(path_to_dir:str)->None:
    try:
      Path(path_to_dir).mkdir(parents=True, exist_ok=True)

    except Exception as error:
      raise error


  @staticmethod
  def move_file(origin:str, destination:str)->None:
    try:
      shutil.move(origin, destination)

    except Exception as error:
      raise error

