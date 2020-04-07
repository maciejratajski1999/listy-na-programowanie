from zadanie1 import packtxt
from zadanie2 import unpacktxt
from zadanie3 import backupcopy
from zadanie4 import changeEOLs

#pierwszy argument to nazwa pliku docelowego, kolejne argumenty to pliki txt, które chcemy razem "zapakować"
packtxt("text.json", "text_1.txt", "text_2.txt")

#odpakowujemy pierwszy argument funkcji z pliku typu json do folderu zawierającego wszystkie zawarte w argumencie pliki (domhyślnie do folderu "unpacked_archive")
unpacktxt("text.json")

#pierwszy argument to rozszerzenie plików, któryhc backup chcemy zrobić, drugi argument to folder, w którym owych plików szukamy (domyślnie bieżący folder)
backupcopy("txt")

#argumenty to ścieżki do plików, w których chemy zmienić znaki końca linii, program wypisze w konsoli z jakiego standardu tłumaczy
changeEOLs("text_1.txt")