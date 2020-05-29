from math import *
from numpy import linspace

class FunctionParser:
    '''
    Klasa zamieniająca funkcje wpisane przez użytkownika na dane
    '''

    def __init__(self, expression, xy_range):
        '''
        :param expression (string): pobierane z okienka entry, wartość wpisana przez użytkownika
        :param xy_range (tuple): x1, x2, y1, y2 - zasięg osi x i y
        '''
        self.expression = expression
        self.xy_range = xy_range

    def __call__(self):
        '''
        :return:
            data (dictionary): {'funkcja' : [wartości funkcji w równych odstępach w zasięgu osi x]}
            xy_ticks (tuple): [x1, ..., x2], [y1, ..., y2] - listy używane później do tworzenia siatki na wykresie
            ticks (numpy.ndarray) : wartości x w równych odstępach wewnątrz zasięgu
        '''
        self.xy_range = eval(self.xy_range[0]), eval(self.xy_range[1]), eval(self.xy_range[2]), eval(self.xy_range[3])
        ticks = linspace(self.xy_range[0], self.xy_range[1], 10000)
        expressions = self.expression.split(";")
        expressions = [exp.replace("^", "**") for exp in expressions]
        try:
            data = {exp : [eval(exp) for x in ticks] for exp in expressions}
            xy_ticks = list(linspace(self.xy_range[0], self.xy_range[1], 5)), list(linspace(self.xy_range[2], self.xy_range[3], 5))
            return data, xy_ticks, ticks
        except SyntaxError:
            raise SyntaxError
        except ValueError:
            raise ValueError
        except NameError:
            raise NameError


    # def __Weierstrass(self, a, b, x):
    #     if a > b:
    #         a, b = b, a
    #     seq = [(a**float(n))*cos((b**float(n))*pi*x) for n in range(1, 100)]
    #     return sum(seq)
