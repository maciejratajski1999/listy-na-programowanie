#backup
import os
import shutil
from datetime import datetime
import time

def backupcopy(suffix, dir = os.getcwd()):
    '''
    tworzy folder Backup/copy-rrrr-mm-dd w żądanym katalogu z kopią plików o podanym rozszerzenu utworzonych lub zmodyfikowanych w ciągu ostatnich 3 dni
    :param suffix (str): rozszerzenie plików, których kopię plików szukamy
    :param dir (str): ścieżka katalogu, dla którego robimy backup
    '''
    if not os.path.exists(dir + "\Backup"):
        os.makedirs(dir + "\Backup")

    day = datetime.today()
    date = day.strftime("%Y-%m-%d")
    destination = dir + "\Backup" + "\copy-" + date
    if os.path.exists(destination):
        raise FileExistsError("backup already done today")
    os.makedirs(destination)

    for (direc, subdirs, files) in os.walk(dir):
        for file in files:
            print(os.path.getmtime(os.getcwd()))
            fullstop = file.find(".") + 1
            time_since_modification = os.path.getmtime(os.path.join(direc, file)) - time.time()
            if file[fullstop:] == suffix and time_since_modification <= 3*24*60*60 :
                try:
                    shutil.copyfile(os.path.join(direc, file), destination + "/" + file)
                except shutil.SameFileError:
                    print("trying to backup the backup archive! change destination directory (dir)")






