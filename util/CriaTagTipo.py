import csv
import os
import logging
import pandas as pd
import platform

class CriaTagTipo:
    def run():
        """
        Identifica o os e ajusta a sintaxe dos paths .
        """
        os_name = platform.system()
        print(os_name)
        if ((str(os_name) != '5.10.60.1-microsoft-standard-WSL2') and (str(os_name) != 'Linux')):
            TRAINING_CSV = '\\happy-whale-and-dolphin\\train.csv'
            OUTPUT_DIR = '\\outputs\\'
            OUTPUT_FILE = '\\train_with_tags.csv'
        
        else:
            TRAINING_CSV = '/happy-whale-and-dolphin/train.csv'
            OUTPUT_DIR = '/outputs/'
            OUTPUT_FILE = '/train_with_tags.csv'

        """
        Lê o CSV 'train.csv', identifica golfinho ou baleia e gera 'train_with_tags.csv' em Outputs.
        """

        logging.info('Started CriaTagTipo')

        df = pd.read_csv(os.path.abspath(os.curdir) + TRAINING_CSV)

        root_dir = os.path.abspath(os.curdir)
        destination_dir = root_dir + OUTPUT_DIR
        csv_dir = destination_dir + OUTPUT_FILE

        if not os.path.os.path.exists(destination_dir):
            os.makedirs(destination_dir)
            logging.info('outputs folder created!')

        with open(csv_dir, 'w', newline='') as csvfile:
            fieldnames = ['image', 'species', 'type', 'individual_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for i in range(len(df.index)):

                type = CriaTagTipo.IdentificaTipoPeixe(df.loc[i][1])

                writer.writerow({'image': df.loc[i][0], 'species': df.loc[i][1], 'type': type, 'individual_id': df.loc[i][2]})

        csvfile.close()

        logging.info('Finished CriaTagTipo')

def IdentificaTipo(nome):
    """
    Lê o nome da espécie e devolve o tipo.
    """

    if "whale" in nome or "beluga" in nome or "globis" in nome:
        type = "whale"
    elif "dolphin" in nome or "dolpin" in nome:
        type = "dolphin"
    else:
        type = "ERROR"
        logging.warning('Type of' + nome + ' not found!')
    return type

