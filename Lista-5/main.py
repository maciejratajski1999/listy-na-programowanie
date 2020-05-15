from NBP_currencies import NBP_currencies
from Currencies_GUI import Currencies_GUI

if __name__ == '__main__':
    # NBP_currencies()() generuje słownik z potrzebnymi danymi, ponieważ klasa NBP_currencies jest wywoływalna (callable)
    data = NBP_currencies()()

    # tworzymy instancję klasy Currencies_GUI z wygenerowanym przed chwilą słownikiem
    root = Currencies_GUI(data)\

    # i wyświetlamy okienko z kalkulatorem
    root()