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

    def __root(self):
        root = tkinter.Tk()
        root.title('NBP currencies')
        root.geometry('250x250')
        root.resizable(False, False)

        f1 = tkinter.Frame(root, height=50, width=200)
        f1.pack()

        label = tkinter.Label(f1, text='Przelicz z: ')
        label.config(font=("Courier", 14))
        label.pack()

        variable = tkinter.StringVar(root)
        variable.set("Wybierz")

        w = tkinter.ttk.Combobox(f1, textvariable=variable, values=self.names, width=30)
        w.pack()

        value = tkinter.Frame(root, height=50, width=200)
        value.pack()

        f2 = tkinter.Frame(root, height=50, width=200)
        f2.pack()

        label = tkinter.Label(f2, text='Przelicz na: ')
        label.config(font=("Courier", 14))
        label.pack()

        variable = tkinter.StringVar(root)
        variable.set("Wybierz")

        w = tkinter.ttk.Combobox(f2, textvariable=variable, values=self.names, width=30)
        w.pack()

        root.mainloop()
