import shutil
import csv
import os
import logging
import pandas as pd
import CriaTagTipo

class DivideGrupoDeBaleias:
    def filtragemBaleinhas (listaEspecies, df, groupName):

        """
        recebe uma lista de espécies, o dataframe e o nome desse grupo, então, move as fotos para um novo diretório em Outputs e gera o csv com a especificação de cada foto.
        """

        logging.info('Started filtragemBaleinhas')

        root_dir = os.path.abspath(os.curdir)
        destination_dir = root_dir + '\\outputs\\' + groupName
        csv_dir = destination_dir +'\\'+ groupName + '.csv'

        if not os.path.os.path.exists(destination_dir):
            os.makedirs(destination_dir)
            logging.info(groupName + ' folder created!')

        with open(csv_dir, 'w', newline='') as csvfile:
            fieldnames = ['image', 'species', 'type', 'individual_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for i in range(len(df.index)):
                if(df.loc[i][1]) not in listaEspecies:
                    pass
                else:
                    source = root_dir + '\\train_images\\' + df.loc[i][0]
                    destination = destination_dir + '\\' + df.loc[i][0]
                
                    if os.path.isfile(source):
                        shutil.move(source, destination)
                    else:
                        logging.warning('File not found in train_images: ' + df.loc[i][0])
                    
                    type = CriaTagTipo.IdentificaTipo(df.loc[i][1])

                    writer.writerow({'image': df.loc[i][0], 'species': df.loc[i][1], 'type': type, 'individual_id': df.loc[i][2]})

        csvfile.close()

        logging.info('Finished filtragemBaleinhas')

    def modeloChamada():

        super_raros = ['spotted_dolphin',
        'sei_whale',
        'short_finned_pilot_whale',
        'common_dolphin',
        'cuviers_beaked_whale',
        'pilot_whale',
        'long_finned_pilot_whale',
        'white_sided_dolphin',
        'brydes_whale',
        'pantropic_spotted_dolphin',
        'globis',
        'commersons_dolphin',
        'pygmy_killer_whale',
        'rough_toothed_dolphin',
        'frasiers_dolphin']

        df = pd.read_csv(os.path.abspath(os.curdir) +'\\train.csv')

        DivideGrupoDeBaleias.filtragemBaleinhas(super_raros, df, 'super_raros')

#DivideGrupoDeBaleias.modeloChamada()