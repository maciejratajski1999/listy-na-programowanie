import os
import datetime
import matplotlib.pyplot as plt

class ModTimes:

    def __init__(self, dir):
        '''inicjator klasy
        :param dir: (str) - ścieżka folderu do analizy
        '''
        self.directory = dir
        self.times_for_files = self.modification_times()
        self.n_by_month = self.count_by_month()

    def modification_times(self):
        '''czyta czas modyfikacji plików z directory metodą os.walk() i os.path.getmtime()

        :return times_for_files: (dict) - {plik (str) : rrrr-mm-dd gg:mm:ss (str)}
        '''
        times_for_files = {}
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                time_of_modification = os.path.getmtime(os.path.join(root, file))
                readable_time = datetime.datetime.fromtimestamp(time_of_modification).strftime('%Y-%m-%d %H:%M:%S')
                times_for_files[file] = readable_time
        return times_for_files

    def count_by_month(self):
        '''liczy ile plików było modyfikowanych w jakich miesiącach

        :return n_by_month: (dict) - {rrrr-mm (str) : n (int)}
        '''
        sorted_times = [time for file, time in sorted(self.times_for_files.items(), key=lambda items : items[1])]
        n_by_month = {}
        for time in sorted_times:
            key = time[:7]
            if key in n_by_month:
                n_by_month[key] += 1
            else:
                n_by_month[key] = 1

        return n_by_month

    def plot(self):
        '''tworzy wykres słupkowy pokazujący ile plików zostało zmodyfikowanych w którym miesiącu

        :return: zapisuje wykres w bieżącym folderze pod nazwą folderu, który analizujemy w formacie .png
        '''
        keys = list(self.n_by_month.keys())
        values = self.n_by_month.values()

        fig, ax = plt.subplots()
        plt.bar(keys, values)
        ax.tick_params(axis ='x', rotation = 45)
        ax.set_xlabel("miesiąc modyfikacji", fontsize ='large')
        ax.set_ylabel("liczba zmodyfikowanych plików", fontsize ='large')
        for k in keys:
            plt.annotate(str(self.n_by_month[k]), (k, self.n_by_month[k]))

        plt.tight_layout()
        folder_name = os.path.basename(self.directory)
        plt.savefig(folder_name + ".png", dpi = 200)

