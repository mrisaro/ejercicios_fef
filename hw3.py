#%% Arranco con la carga de librerías
# import os, os.path, time
# print("Last modified: %s" % time.ctime(os.path.getmtime("fotis/G0010628.JPG")))
# print("Created: %s" % time.ctime(os.path.getctime("fotis/G0010628.JPG")))

import os
import shutil
from datetime import datetime

path = '/home/matias/Dropbox/Learning_python/curso_fisiques/clase0/'
DIR = path+'fotis/'
dir_ord = path + 'fotis_ord/'

lista = os.listdir(DIR)


os.mkdir(dir_ord)
for i in lista:

    modified= os.stat(DIR+i).st_mtime
    fech = datetime.fromtimestamp(modified)
    fecha = fech.strftime("%Y-%m")
    src = DIR + i                       # source archivo a copiar
    dst = dir_ord+fecha                 # destination

    if os.path.exists(dir_ord+fecha)==False:
        os.mkdir(dir_ord+fecha)
        shutil.copy(src, dst)
    else:
        shutil.copy(src, dst)

print('Todo ordenado ya')
