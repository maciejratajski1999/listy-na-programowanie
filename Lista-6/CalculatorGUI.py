import tkinter
import tkinter.ttk
from FunctionParser import FunctionParser
from Graphs import Graphs

class CalculatorGUI:
    '''
    Główna klasa, tworząca okienko, przypominające kalkulator
    '''
    def __init__(self):
        pass
    def __call__(self):
        '''
        Wywołanie instancji klasy
        '''
        self.__root()

    def __draw(self, input_value, xy_range_fields):
        '''
        funkcja wywołująca rysowanie wykresu
        :param input_value (string): pobrane z pola entry, to co znajduje się w oknie wpisywania funkcji
        :param xy_range_fields (tuple of tkinter.Entry) : pola do wpisywania zasięgów osi x i y
        '''
        # tworzy krotkę wartości x1, x2, y1, y2, zasięgi osi x i y
        xy_range = tuple([arg.get() for arg in xy_range_fields])
        # tworzymy instancję klasy FunctionParser, która przekonwertuje nasze wpisane wartości na dane do wykresu
        parse = FunctionParser(input_value,xy_range)
        try:
            # generowanie danych
            data, xy_ticks, ticks = parse()
            # tworzymy instancję klasy Graphs
            graph = Graphs(data, xy_ticks, ticks)
            # i wywołujemy ją, czyli wyśiwetlamy wykres na ekranie
            graph()
        except SyntaxError:
            self.input_value.set(self.input_value.get() + "Błędny zapis jednej z funkcji")
        except ValueError:
            self.input_value.set(self.input_value.get() + "Funkcja poza dziedziną")
        except NameError:
            self.input_value.set(self.input_value.get() + "Nie ma takiej funkcji")




    def __root(self):
        '''
        główna funkcja budująca okno GUI
        '''
        # parametry okna
        self.root = tkinter.Tk()
        self.root.title("Funkcje")
        self.root.geometry("400x500")
        bg_color = 'black'
        self.root.config(bg=bg_color)
        self.root.resizable(False, False)

        # Główna wartość input - w którą uzytkownik wpisywać będzie funkcje
        self.input_value = tkinter.StringVar(self.root)
        self.input_value.set("")


        def __entry():
            '''
            tworzę pole tekstowe na wprowadzanie funkcji
            :return entry (tkinter.Entry): pole wejściowe
            '''
            entryframe = tkinter.Frame(self.root, height=100, width=400, background=bg_color)
            entryframe.pack(side=tkinter.TOP)
            label = tkinter.Label(entryframe, text="Wprowadź funkcje f(x); g(x) ...", background=bg_color, fg='white')
            label.pack()
            entry = tkinter.Entry(entryframe, textvariable=self.input_value, width=100, justify='right', font=(10))
            entry.pack()
            return entry
        entry = __entry()

        def __addToEntry(arg):
            '''
            :param arg (string): co ma być dodane do entry
            '''
            start = self.input_value.get()
            self.input_value.set(start + arg)
            entry.icursor(len(start + arg))

        # tutaj tworzę przycisk button - do rysowania
        buttonframe = tkinter.Frame(self.root, height=100, width=400, background=bg_color)
        buttonframe.pack(side=tkinter.TOP)
        def __buttonDraw():
            '''
            tworzenie przycisku "Rysuj"
            :return button (tkinter.Button):
            '''
            button = tkinter.Button(buttonframe, text='Rysuj', bg='#2000d0', fg='white', width=10, height=4)
            button.pack(side=tkinter.RIGHT)
            return button
        button = __buttonDraw()
        button.config(command= lambda: self.__draw(entry.get(), xy_range_fields))

        # tutaj tworzę pola do wprowadzania żądanych zasięgów osi
        def __rangeEntries():
            '''

            :return (tuple of tkinter.Entry): xStart, xStop, yStart, yStop - pola do wprowadzania zasięgów osi x i y
            '''
            rangeframe2 = tkinter.Frame(buttonframe, height=100, width=100, background=bg_color)
            rangeframe2.pack(side=tkinter.RIGHT)
            xStop, yStop = tkinter.StringVar(rangeframe2), tkinter.StringVar(rangeframe2)
            label = tkinter.Label(rangeframe2, text="zasięg osi x do:", background=bg_color, fg='white')
            label.pack(side=tkinter.TOP)
            x2 = tkinter.Entry(rangeframe2, textvariable=xStop, width=5)
            x2.pack(side=tkinter.TOP)
            label = tkinter.Label(rangeframe2, text="zasięg osi y do:", background=bg_color, fg='white')
            label.pack(side=tkinter.TOP)
            y2 = tkinter.Entry(rangeframe2, textvariable=yStop, width=5)
            y2.pack(side=tkinter.TOP)

            rangeframe1 = tkinter.Frame(buttonframe, height=100, width=100, background=bg_color)
            rangeframe1.pack(side=tkinter.RIGHT)
            xStart, yStart= tkinter.StringVar(rangeframe1), tkinter.StringVar(rangeframe1)
            label = tkinter.Label(rangeframe1, text="zasięg osi x od:", background=bg_color, fg='white')
            label.pack(side=tkinter.TOP)
            x1 = tkinter.Entry(rangeframe1, textvariable=xStart, width = 5)
            x1.pack(side=tkinter.TOP)
            label = tkinter.Label(rangeframe1, text="zasięg osi y od:", background=bg_color, fg='white')
            label.pack(side=tkinter.TOP)
            y1 = tkinter.Entry(rangeframe1, textvariable=yStart, width=5)
            y1.pack(side=tkinter.TOP)

            xStart.set('-pi')
            xStop.set('pi')
            yStart.set('-1')
            yStop.set('1')

            return xStart, xStop, yStart, yStop
        xy_range_fields = __rangeEntries()

        # Tutaj dodaję Przyciski, po 4 w wierszu, służące do wpisywania danych funkcji do pola entry
        def __addFuncButtons(*argv):
            frame = tkinter.Frame(self.root, height=100, width=400, bg=bg_color)
            frame.pack(pady=1, side=tkinter.TOP)
            # {'tekst na przycisku' : 'poprawnie według pythona'}
            argv_dict = {"silnia" : "factorial()", "cosinus" : "cos()", "sinus" : "sin()", "tangens" : "tan()", "cotangens" : "(1/tan())",
                         "+" : "+",                 "-" : "-",           "^" : "**",        "e" : "e",
                         "Pi" : "pi",               "sqrt" : "sqrt()",  "/" : "/",          "moduł" : "fabs()",
                         "( )" : "()",                 "*" : "*",          "ln" : "log()", "," : "."}

            b1, b2, b3, b4 = argv
            button1 = tkinter.Button(frame, text=b1, command=lambda: __addToEntry(argv_dict[b1]), bg=bg_color, fg='white', width=10, height=4)
            button1.pack(side=tkinter.LEFT, padx=1)
            button2 = tkinter.Button(frame, text=b2, command=lambda: __addToEntry(argv_dict[b2]), bg=bg_color, fg='white', width=10, height=4)
            button2.pack(side=tkinter.LEFT, padx=1)
            button3 = tkinter.Button(frame, text=b3, command=lambda: __addToEntry(argv_dict[b3]), bg=bg_color, fg='white', width=10, height=4)
            button3.pack(side=tkinter.LEFT, padx=1)
            button4 = tkinter.Button(frame, text=b4, command=lambda: __addToEntry(argv_dict[b4]), bg=bg_color, fg='white', width=10, height=4)
            button4.pack(side=tkinter.LEFT, padx=1)

        __addFuncButtons("sinus","cosinus", "tangens", "cotangens")
        __addFuncButtons("+", "-", "^", "Pi")
        __addFuncButtons("*", "/", "sqrt", "e")
        __addFuncButtons("( )", "moduł", ",", "ln")

        # tutaj dodaję przyciski Czyść i Zakończ
        endframe = tkinter.Frame(self.root, height=100, width=100, background=bg_color)
        endframe.pack(side=tkinter.TOP, pady = 5)
        def __clear():
            self.input_value.set("")
        clear = tkinter.Button(endframe, text="Czyść", command=__clear, bg="darkred", fg="lightgreen", width=6, height=2, font=("Helvetica", 10))
        clear.pack(side=tkinter.LEFT,padx=5, pady=5)
        end = tkinter.Button(endframe, text="Zakończ", command=self.root.destroy, bg="darkred", fg="lightgreen", width=6, height=2, font=("Helvetica", 10))
        end.pack(side=tkinter.LEFT,padx=5, pady=5)

        # i wyświetlam okno
        self.root.mainloop()
