import json
import os

def unpacktxt(archive, dest = "unpacked_archive"):
    '''
    otwiera słownik {nazwa_pliku : zawartość_pliku} z pliku  .json
    i tworzy folder, w którym odtwarza wszystkie pierwotne pliki tekstowe zawarte w otwieranym archiwum
    :param archive (str): archiwum pod postacią słownika zapisanego w .json
    :param dest (str): nazwa folderu do którego odpakowujemy pliki tekstowe
    '''
    if not os.path.exists(os.getcwd() + "/" + dest):
        os.makedirs(os.path.join(os.getcwd(), dest))
    json_dict = open(archive, "r")
    python_dict = (json.loads(json_dict.read()))
    for file, content in python_dict.items():
        text = open(os.path.join(os.getcwd(), dest) + "/" + file, "w")
        text.write(content)
        text.close()

