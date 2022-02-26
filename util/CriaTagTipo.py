import csv
import os
import logging
import pandas as pd

class CriaTagTipo:
    def CriaTagTipo():

        """
        Lê o CSV 'train.csv', identifica golfinho ou baleia e gera 'train_with_tags.csv' em Outputs.
        """

        logging.info('Started CriaTagTipo')

        df = pd.read_csv(os.path.abspath(os.curdir) +'\\train.csv')

        root_dir = os.path.abspath(os.curdir)
        destination_dir = root_dir + '\\outputs\\'
        csv_dir = destination_dir +'\\train_with_tags.csv'

        if not os.path.os.path.exists(destination_dir):
            os.makedirs(destination_dir)
            logging.info('outputs folder created!')

        with open(csv_dir, 'w', newline='') as csvfile:
            fieldnames = ['image', 'species', 'type', 'individual_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for i in range(len(df.index)):
                type = IdentificaTipo(df.loc[i][1])
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

#CriaTagTipo.CriaTagTipo()