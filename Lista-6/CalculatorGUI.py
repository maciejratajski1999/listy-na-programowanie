import tkinter
import tkinter.ttk
from FunctionParser import FunctionParser
from Graphs import Graphs

class CalculatorGUI:

    def __init__(self):
        pass
    def __call__(self):
        self.__root()

    def output(self, output):
        return output

    def __draw(self, outcome, xy_range_fields):
        # print("inside CalculatorGUI: ", outcome)
        xy_range = tuple([arg.get() for arg in xy_range_fields])
        parse = FunctionParser(outcome,xy_range)
        try:
            data, xy_ticks, ticks = parse()
            graph = Graphs(data, xy_ticks, ticks)
            graph()
        except SyntaxError:
            self.input_value.set(self.input_value.get() + "Błędny zapis jednej z funkcji")
        except ValueError:
            self.input_value.set(self.input_value.get() + "Funkcja poza dziedziną")




    def __root(self):
        self.root = tkinter.Tk()
        self.root.title("Kalkulator")
        self.root.geometry("400x500")
        bg_color = 'black'
        self.root.config(bg=bg_color)
        self.root.resizable(False, False)

        self.input_value = tkinter.StringVar(self.root)
        self.input_value.set("")


        def __entry():
            entryframe = tkinter.Frame(self.root, height=100, width=400, background=bg_color)
            entryframe.pack(side=tkinter.TOP)
            label = tkinter.Label(entryframe, text="Wprowadź funkcje f(x); g(x) ...", background=bg_color, fg='white')
            label.pack()
            entry = tkinter.Entry(entryframe, textvariable=self.input_value, width=100, justify='right', font=(10))
            entry.pack()
            return entry
        entry = __entry()

        def __addToEntry(arg):
            start = self.input_value.get()
            self.input_value.set(start + arg)
            entry.icursor(len(start + arg))

        buttonframe = tkinter.Frame(self.root, height=100, width=400, background=bg_color)
        buttonframe.pack(side=tkinter.TOP)
        def __buttonDraw():
            button = tkinter.Button(buttonframe, text='Rysuj', bg='#2000d0', fg='white', width=10, height=4)
            button.pack(side=tkinter.RIGHT)
            return button
        button = __buttonDraw()
        button.config(command= lambda: self.__draw(entry.get(), xy_range_fields))

        def __rangeEntries():
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

        def __addFuncButtons(*argv):
            frame = tkinter.Frame(self.root, height=100, width=400, bg=bg_color)
            frame.pack(pady=1, side=tkinter.TOP)
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

        def __clear():
            self.input_value.set("")
        clear = tkinter.Button(self.root, text="Czyść", command=__clear, bg="darkred", fg="lightgreen", width=4, height=2, font=("Helvetica", 10))
        clear.pack(side=tkinter.TOP,pady=1)

        self.root.mainloop()
