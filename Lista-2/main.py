from zadanie_1 import data_Wielkanocy
from zadanie_2 import create_thumbnail
from zadanie_3 import create_zip_archive
from zadanie_4 import ModTimes


#zadanie 1 - wypisze datę Wielkanocy w roku 2020
print(data_Wielkanocy(2020))

#utworzy w obecnym folderze miniaturę obrazka w wymiarach 160 x 90 i zapisze domyślnie jako miniatura.jpg w obecnym folderze
create_thumbnail(r"Alpacas.jpg", (160, 90))

#utworzy w obecnym folderze archive.zip zawierający folder archive i wszystkie jego podfoldery oraz pliki w nich się znajdujące
create_zip_archive("archive","archive.zip")

#aby sprawdzić zadanie 4:
#directory = ModTimes("path_to_folder")
#directory.plot()
#wykres pojawi się w bieżącym folderze w formacie .png,
#przyjmie nazwę analizowanego folderu
#
#np:
analyse_archive = ModTimes(r"archive")
analyse_archive.plot()
#
#w repozytorium przesłałem plik Moje_memy.png, który przedstawia modyfikacje plików
#w moim folderze z memami na komputerze prywatnym