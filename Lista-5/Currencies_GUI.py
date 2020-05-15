import tkinter
import tkinter.ttk

class Currencies_GUI:
    '''
    Klasa tworząca okienko z kalkulatorem walutowym
    '''

    def __init__(self, currencies):
        '''
        :param currencies (Dictionary): generowany przez moduł NBP_currencies słownik
                                        {"kod i nazwa waluty" : kurs (Float)}
        '''
        # dodaję złotówkę do słownika, 1 złoty jest oczywiście warty 1 złoty, więc kurs typu (Float) ustawiam na 1.0
        currencies["PLN polski złoty"] = 1.0
        self.currencies = currencies
        # tworzę listę nazw walut, aby móc je wyświetlać w rozwijanym okienku
        self.names = self.__make_list()

    def __call__(self):
        '''
        wywołanie instancji ten klasy wywoła funkcję __root() wyświetlającą okienko z kalkulatorem
        '''
        self.__root()

    def __make_list(self):
        '''
        ta metoda tworzy listę wszystkich nazw walut zawartych w dictionary, i ustawia je w kolejności alfabetycznej, po PLN złoty na pierwszym miejscu
        :return:
        '''
        temp = dict(self.currencies)
        del temp["PLN polski złoty"]
        sorted_names = ["PLN polski złoty"] + sorted(temp.keys())
        return sorted_names

    def __calculate(self, cur1, cur2, amount):
        '''
        :param cur1 (String): nazwa waluty, z której przeliczamy (ten String stanowi klucz do słownika currencies)
        :param cur2 (String): nazwa waluty, na która zamieniamy (ten String stanowi klucz do słownika currencies)
        :param amount (Float): ilość początkowej waluty
        :return outcome (Float): ilość otrzymanej waluty
        '''
        # kurs jednej waluty do drugiej obliczamy wyciągając dane ze słownika currencies
        price_ratio = self.currencies[cur1] / self.currencies[cur2]
        # obliczam ilość otrzymanej waluty
        outcome = amount*price_ratio
        return str(outcome)

    def __root(self):
        '''
        główna metoda, wyświetlająca okienko z kalkulatorem
        '''
        def calculate():
            '''
            Wykonywana po naciśnięciu guzika button wewnątrz okienka,
            ta funkcja pobiera dane z pól wejściowych i wprowadza wynik do pola out
            '''
            try:
                # _cur1 - początkowa waluta             : pobierana z pola cur1
                # _cur2 - żądana waluta                 : pobierana z pola cur2
                # _amount - ilość początkowej waluty    : pobierana z pola entry
                _cur1, _cur2, _amount = cur1.get(), cur2.get(), float(entry.get())
                # wprowadź wynik funkcji __calculate do pola out
                outcome.set(self.__calculate(_cur1,_cur2,_amount))

            # jeśli podana liczba nie będzie Floatem
            except ValueError:
                outcome.set("wprowadź liczbę do pola wyżej")

            # jeśli podana waluta nie istnieje w słowniku
            except KeyError:
                outcome.set("wprowadź walutę z listy dostępnych")

        # tworzymy root, czyli moje okno
        root = tkinter.Tk()
        # przyjemne tło, koloru dolara amerykańskiego
        bg_color = '#85bb65'
        root.configure(background=bg_color)
        root.title('NBP currencies')
        root.geometry('250x250')
        root.resizable(False, False)

        # pierwsza część, w której wprowadzamy początkową walutę
        f1 = tkinter.Frame(root, height=62, width=200, background=bg_color)
        f1.pack()
        label1 = tkinter.Label(f1, text='Przelicz z: ', background=bg_color)
        label1.config(font=("Courier", 14))
        label1.pack()
        variable = tkinter.StringVar(f1)
        variable.set("PLN polski złoty")
        cur1 = tkinter.ttk.Combobox(f1, textvariable=variable, values=self.names, width=35)
        cur1.pack()

        # druga część, w której wprowadzamy ilość początkowej waluty, oraz znajduje się tutaj guzik Oblicz
        f2 = tkinter.Frame(root, height=62, width=200, background=bg_color)
        f2.pack()
        labelV = tkinter.Label(f2, text='Ilość: ', background=bg_color)
        labelV.config(font=("Courier", 14))
        labelV.pack()
        amount = tkinter.StringVar(f2)
        amount.set(1)
        entry = tkinter.Entry(f2, textvariable=amount, width=20, justify='right')
        entry.pack(side=tkinter.LEFT)
        # guzik aktywuje funkcję calculate zdefiniowaną wcześniej wewnątrz obecnej funkcji
        button = tkinter.Button(f2, text='Oblicz', command=calculate, height=1, background='#508035', font=("Courier", 10))
        button.pack(side=tkinter.RIGHT)

        # trzecia część, w której wprowadzamy końcową walutę
        f3 = tkinter.Frame(root, height=62, width=200, background=bg_color)
        f3.pack()
        label2 = tkinter.Label(f3, text='Przelicz na: ', background=bg_color)
        label2.config(font=("Courier", 14))
        label2.pack()
        variable2 = tkinter.StringVar(f3)
        variable2.set("USD dolar amerykański")
        cur2 = tkinter.ttk.Combobox(f3, textvariable=variable2, values=self.names, width=35)
        cur2.pack()

        # czwarta część, gdzie znajduje się pole z wynikiem
        f4 = tkinter.Frame(root, height=62, width=200, background=bg_color)
        f4.pack()
        labelO = tkinter.Label(f4, text='Wynik: ', background=bg_color, font=("Courier", 14))
        labelO.pack()
        outcome = tkinter.StringVar(f4)
        outcome.set("")
        out = tkinter.Entry(f4, textvariable=outcome, width=35, justify='right')
        out.pack()

        # wyświetlanie okienka
        root.mainloop()
