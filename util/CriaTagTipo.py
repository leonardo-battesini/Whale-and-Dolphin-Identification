import csv
import os
import logging
import pandas as pd

class CriaTagTipo:
    def CriaTagTipo():

        """
        recebe CSV e identifica golfinho ou baleia.
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
                if "whale" in df.loc[i][1] or "beluga" in df.loc[i][1] or "globis" in df.loc[i][1]:
                    type = "whale"
                elif "dolphin" in df.loc[i][1] or "dolpin" in df.loc[i][1]:
                    type = "dolphin"
                else:
                    type = "ERROR"
                    logging.warning('Type ' + df.loc[i][1] + 'not found!')
                writer.writerow({'image': df.loc[i][0], 'species': df.loc[i][1], 'type': type, 'individual_id': df.loc[i][2]})

        csvfile.close()

        logging.info('Finished CriaTagTipo')

CriaTagTipo.CriaTagTipo()