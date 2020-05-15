import tkinter
import tkinter.ttk

class Currencies_GUI:

    def __init__(self, currencies):
        currencies["PLN złoty (Polska)"] = 1.0
        self.currencies = currencies
        self.names = self.__make_lists()

    def __call__(self):
        self.__root()

    def __make_lists(self):
        temp = dict(self.currencies)
        del temp["PLN złoty (Polska)"]
        sorted_names = ["PLN złoty (Polska)"] + sorted(temp.keys())
        return sorted_names

    def __calculate(self, cur1, cur2, amount):

        price_ratio = self.currencies[cur1] / self.currencies[cur2]
        outcome = amount*price_ratio
        return outcome

    def __root(self):
        def calculate():
            try:
                _cur1, _cur2, _amount = cur1.get(), cur2.get(), float(entry.get())
                outcome.set(self.__calculate(_cur1,_cur2,_amount))
            except ValueError:
                outcome.set("wprowadź liczbę do pola wyżej")

        root = tkinter.Tk()
        bg_color = '#85bb65'
        bg_color = bg_color
        root.configure(background=bg_color)
        root.title('NBP currencies')
        root.geometry('250x250')
        root.resizable(False, False)

        f1 = tkinter.Frame(root, height=62, width=200, background=bg_color)
        f1.pack()
        label1 = tkinter.Label(f1, text='Przelicz z: ', background=bg_color)
        label1.config(font=("Courier", 14))
        label1.pack()
        variable = tkinter.StringVar(f1)
        variable.set("PLN złoty (Polska)")
        cur1 = tkinter.ttk.Combobox(f1, textvariable=variable, values=self.names, width=30)
        cur1.pack()

        f2 = tkinter.Frame(root, height=62, width=200, background=bg_color)
        f2.pack()
        labelV = tkinter.Label(f2, text='Ilość: ', background=bg_color)
        labelV.config(font=("Courier", 14))
        labelV.pack()
        amount = tkinter.StringVar(f2)
        amount.set(1)
        entry = tkinter.Entry(f2, textvariable=amount, width=20, justify='right')
        entry.pack(side=tkinter.LEFT)
        button = tkinter.Button(f2, text='Oblicz', command=calculate, height=1, background='#508035', font=("Courier", 10))
        button.pack(side=tkinter.RIGHT)

        f3 = tkinter.Frame(root, height=62, width=200, background=bg_color)
        f3.pack()
        label2 = tkinter.Label(f3, text='Przelicz na: ', background=bg_color)
        label2.config(font=("Courier", 14))
        label2.pack()
        variable2 = tkinter.StringVar(f3)
        variable2.set("USD dolar amerykański")
        cur2 = tkinter.ttk.Combobox(f3, textvariable=variable2, values=self.names, width=30)
        cur2.pack()

        f4 = tkinter.Frame(root, height=62, width=200, background=bg_color)
        f4.pack()
        labelO = tkinter.Label(f4, text='Wynik: ', background=bg_color, font=("Courier", 14))
        labelO.pack()
        outcome = tkinter.StringVar(f4)
        outcome.set(10)
        out = tkinter.Entry(f4, textvariable=outcome, width=20, justify='right')
        out.pack()
        root.mainloop()
