from matplotlib import pyplot as plt
from numpy import linspace


class Graphs:

    def __init__(self, data, xy_ticks, ticks):
        self.data = data
        self.x_range = xy_ticks[0]
        self.y_range = xy_ticks[1]
        self.ticks = ticks

    def __call__(self):
        plt.close()
        def single_plot(single_data):
            plt.plot(self.ticks, single_data[1], label=single_data[0])
            plt.legend(fontsize='medium')

        for single_data in self.data.items():
            single_plot(single_data)
        plt.xticks(ticks=self.x_range)
        plt.yticks(ticks=self.y_range)
        plt.grid()
        plt.xlim(self.x_range[0], self.x_range[-1])
        plt.ylim(self.y_range[0], self.y_range[-1])


        plt.show()