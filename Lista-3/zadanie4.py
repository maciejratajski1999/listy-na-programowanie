#zmiana znaków końca linii


def changeEOLs(*args):
    '''
    Tłumaczy znaki końca linii między Unixem (\n) a Windowsem (\r\n), znajduje pierwszy znak końca linii i przyjmuje go za obecny standard pliku
    :param args (str): ścieżki do plików, które będzie tłumaczył program
    '''
    for file in args:
        old_file = open(file, "r")
        old_text = old_file.read()
        print(old_text)

        if old_text.find("\r\n") == -1:
            print("translating Unix EOLs to Windows")
            new_file = old_text.replace("\n", "\r\n")
            print(new_file)
        else:
            print("translating Windows EOLs to Unix")
            new_file = old_text.replace("\r\n", "\n")
            print(new_file)
        old_file = open(file, "w")
        old_file.write(new_file)


