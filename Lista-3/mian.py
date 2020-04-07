from zadanie1 import packtxt
from zadanie2 import unpacktxt
from zadanie3 import backupcopy
from zadanie4 import changeEOLs

packtxt("text.json", "text_1.txt", "text_2.txt")
unpacktxt("text.json")
backupcopy("txt")
changeEOLs("text_1.txt")