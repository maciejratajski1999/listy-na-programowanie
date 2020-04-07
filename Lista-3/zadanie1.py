#pakowanie kilku plików txt w jeden
import json


def packtxt(dest = "archive.json", *args):
    '''
    tworzy słownik {nazwa_pliku : zawartość_pliku} i zapisuje go do pliku  .json
    :param dest (str): nazwa tworzonego archiwum
    :param args (str): ścieżki do plików, które pakujemy do archiwum
    '''
    archive = {}
    for text in args:
        file = open(text, "r")
        archive[text] = file.read()
        file.close()
    with open(dest, "w") as archive_json:
        json.dump(archive, archive_json)



