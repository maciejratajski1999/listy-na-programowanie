import zipfile
import os
from datetime import datetime


def create_zip_archive(folder_path, destination_path):
    '''tworzy archiwum zip danego folderu

    :param folder_path: (str) - ścieżka do folderu
    :param destination_path: (str) - ścieżka do tworzonego pliku .zip

    '''
    current_time = str(datetime.now())
    current_time = current_time[:10]
    new_zip = zipfile.ZipFile(current_time + destination_path, "w")
    for root, dirs, files in os.walk(folder_path):
        new_zip.write(root)
        for file in files:
            new_zip.write(os.path.join(root, file))
    new_zip.close()


