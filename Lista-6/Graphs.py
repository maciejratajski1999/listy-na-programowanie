from matplotlib import pyplot as plt
from numpy import linspace


class Graphs:
    '''
    Klasa tworząca wykres
    '''

    def __init__(self, data, xy_ticks, ticks):
        '''
        parametry pobrane z klasy FunctionParser:

        :param data (dictionary): {'funkcja' : [wartości funkcji w równych odstępach w zasięgu osi x]}
        :param xy_ticks (tuple): [x1, ..., x2], [y1, ..., y2] - listy używane później do tworzenia siatki na wykresie
        :param ticks (numpy.ndarray) : wartości x w równych odstępach wewnątrz zasięgu
        '''
        self.data = data
        self.x_range = xy_ticks[0]
        self.y_range = xy_ticks[1]
        self.ticks = ticks

    def __call__(self):
        '''
        Rysowanie i wyświetlanie wykresu
        '''
        plt.close()
        def single_plot(single_data):
            '''
            :param single_data (tuple): ('funkcja', [wartości funkcji w równych odstępach w zasięgu osi x])
            '''
            # rysuję pojedynczy wykres i dodaję do niego legendę
            plt.plot(self.ticks, single_data[1], label=single_data[0])
            plt.legend(fontsize='medium')

        # rysuję każdy wykres po kolei, wyłączając pojedyncze pary 'funkcja' : [wartości funkcji] ze słownika self.data
        for single_data in self.data.items():
            single_plot(single_data)

        # dodaję siatkę i ograniczam wielkość osi x oraz y
        plt.xticks(ticks=self.x_range)
        plt.yticks(ticks=self.y_range)
        plt.grid()
        plt.xlim(self.x_range[0], self.x_range[-1])
        plt.ylim(self.y_range[0], self.y_range[-1])

        # wyświetlam wykres
        plt.show()