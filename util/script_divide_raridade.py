import shutil
import csv
import os

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

with open('D:/base gigante/super_raros/super_raros.csv', 'w', newline='') as csvfile:
    fieldnames = ['image', 'species', 'individual_id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(len(df.index)):
        if(df.loc[i][1]) not in super_raros:
            pass
        else:
            source = 'D:\\base gigante\\train_images\\' + df.loc[i][0]
            destination = 'D:\\base gigante\\super_raros\\' + df.loc[i][0]
        
            if os.path.isfile(source):
                shutil.move(source, destination)
            
            writer.writerow({'image': df.loc[i][0], 'species': df.loc[i][1], 'individual_id': df.loc[i][2]})

csvfile.close()
