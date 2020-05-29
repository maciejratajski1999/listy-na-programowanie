from math import *
from numpy import linspace

class FunctionParser:

    def __init__(self, expression, xy_range):
        # print("inside __init__ FunctionParser: ", expression)
        self.expression = expression
        self.xy_range = xy_range

    def __call__(self):
        self.xy_range = eval(self.xy_range[0]), eval(self.xy_range[1]), eval(self.xy_range[2]), eval(self.xy_range[3])
        ticks = linspace(self.xy_range[0], self.xy_range[1], 1000)
        expressions = self.expression.split(";")
        results = [[eval(exp) for x in ticks] for exp in expressions]
        xy_ticks = list(linspace(self.xy_range[0], self.xy_range[1], 5)), list(linspace(self.xy_range[2], self.xy_range[3], 5))
        return results, xy_ticks, ticks

    # def  