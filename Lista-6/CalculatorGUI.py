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





    def __draw(self, outcome):
        # print("inside CalculatorGUI: ", outcome)
        xy_range = ("-pi", "pi", "-1", "1")
        parse = FunctionParser(outcome,xy_range)
        data, xy_ticks, ticks = parse()
        graph = Graphs(data, xy_ticks, ticks)
        graph()


    def __root(self):
        self.root = tkinter.Tk()
        self.root.title("Kalkulator")
        self.root.geometry("400x400")
        bg_color = 'black'
        self.root.resizable(False, False)

        input_value = tkinter.StringVar(self.root)
        input_value.set("")
        def __entry():
            frame = tkinter.Frame(self.root, height=100, width=400, background=bg_color)
            frame.pack()
            label = tkinter.Label(frame, text='Funkcje F(x)', background=bg_color, fg='white')
            label.pack()
            entry = tkinter.Entry(frame, textvariable=input_value, width=100, justify='right', font=(10))
            entry.pack(side=tkinter.LEFT, pady=20)
            return entry
        entry = __entry()

        def __addToEntry(arg):
            start = input_value.get()
            input_value.set(start + arg)

        def __button():
            frame = tkinter.Frame(self.root, height=100, width=400, background=bg_color)
            frame.pack()
            button = tkinter.Button(frame, text='Rysuj', bg='#2000d0', fg='white', width=10, height=4)
            button.pack()
            return button
        button = __button()
        button.config(command= lambda: self.__draw(entry.get()))

        def __addFuncButtons(*argv):
            frame = tkinter.Frame(self.root, height=100, width=400, bg=bg_color)
            frame.pack()
            argv_dict = {"silnia" : "factorial()", "cosinus" : "cos()", "sinus" : "sin()", "tangens" : "tan()", "cotangens" : "ctan()", "+" : "+", "-" : "-", "^" : "**", "e" : "e"}
            for arg in argv:
                button = tkinter.Button(frame, text=arg, command=lambda: __addToEntry(argv_dict[arg]), bg=bg_color, fg='white', width=10, height=4)
                button.pack(side=tkinter.RIGHT)
        __addFuncButtons("cosinus","tangens", "sinus", "silnia")
        __addFuncButtons("+", "-", "^", "e")

        self.root.mainloop()
