from random import randint
import matplotlib.pyplot as plt
from matplotlib import colors
import os
from PIL import Image
from datetime import datetime
import numpy as np

class Agent:
    '''
    klasa Agent służy do generowania gifa symulującego ruch agenta po kratce o wymiarach 20 x 20

    jeśli w obecnym folderze znajduje się już folder o takiej samej nazwie jak zawartość zmiennej
        self.temp, wywołanie instancji klasy nie zadziała

    przy ilości klatek n większej niż 200 zdarzyły mi się błędy niespowodowane błędnym kodem,
        a raczej niewystarczającą pamięcią komputera błąd 'failed to allocate bitmap'
    '''

    def __init__(self, n, temp = 'temporary_images' ):
        '''
        :param n (int): ilość klatek, pojedynczych ruchów, które wykona agent
        :param temp (string): domyślnie 'temporary_images' : nazwa tymczasowego folderu, w którym przchowywane będą klatki przed wykonaniem gifa
        '''
        self.temp = self.__test_for_temp(temp)
        self.n = self.__test_for_n(n)

    def __call__(self):
        '''
        wywołując instancję tej klasy, wyowołujemy metodę generate_path()
        '''
        self.__generate_path()

    def __test_for_n(self, n):
        '''
        sprawdzamy czy n (w ewentualnym zaokrągleniu) jest liczbą naturalną, jeśli nie jest, funkcja zwraca błąd
        :param n: n podane przez użytkownika
        :return: new_n (int): liczba naturalna, ilość klatek w animacji, ilość kroków agenta
        '''
        try:
            new_n = int(n)
            if new_n > 0:
                return new_n
            else:
                raise ValueError("argument n musi być liczbą naturalną")
        except TypeError:
            raise TypeError("argument n musi być typu integer")

    def __test_for_temp(self, temp):
        '''
        sprawdzamy czy temp jest prawidłową nazwą folderu
        :param temp: temp podane przez użytkownika
        :return: new_temp (string): niezawierające znaków niedozwolonych w nazwie folderu:
            \ / * ? : " < > |
        '''
        new_temp = str(temp)
        invalid = {"\\", "/", "*", "?", ":", "\"", "<", ">", "|"}
        if any(character in invalid for character in new_temp):
            raise ValueError("temp (String) nie może zawierać znaków: \n\ / * ? : \" < > |")
        else:
            return new_temp

    def __jump(self, pos):
        '''
        metoda jump losuje w którą stronę wykonany będzie następny skok agenta
            agent może ruszyć się o jedną kratkę w lewo-prawo, góra-dół, bądź na skos

        :param pos (tuple(int, int)): obecna pozycja agenta na siatce
        :return: new_pos (tuple(int, int)): nowa pozycja agenta na siatce
        '''

        # zmienna x_y losuje w którą stronę na osi x oraz y poruszy się agent w następnym kroku
        # jeśli wylosuje się ruch (0,0) losujemy od nowa, bo nie chcę żeby mój agent stał w miejscu (gid wtedy wyglądałby jakby się przyciął na tej klatce)
        x_y = randint(-1, 1), randint(-1, 1)
        if x_y == (0, 0):
            return self.__jump(pos)
        # zmienna new_pos, czyli poprzednia pozycja agenta zmieniona o właśnie wylosowany ruch
        new_pos = pos[0] + x_y[0], pos[1] + x_y[1]

        # ponieważ rozmiar mojej siatki to 20x20, kiedy agent wyjdzie poza krawędź, chcę aby pojawiał się po drugiej stronie obrazka
        # tutaj sprawdzam dla osi x
        if new_pos[0] not in range(1, 21):
            if new_pos[0] > 20:
                new_pos = pos[0] + x_y[0] - 20,  pos[1] + x_y[1]
            if new_pos[0] < 1:
                new_pos = pos[0] + x_y[0] + 20, pos[1] + x_y[1]
        # a tutaj dla osi y
        if new_pos[1] not in range(1, 21):
            if new_pos[1] > 20:
                new_pos = new_pos[0], pos[1] + x_y[1] - 20
            if new_pos[1] < 1:
                new_pos = new_pos[0], pos[1] + x_y[1] + 20

        return new_pos

    def __generate_image(self, pos, i):
        '''
        metoda generate_image generuje jedną klatkę i zapisuje ją do pliku typu .png w tymczasowym folderze temporary_images

        :param pos (tuple(int, int)): nowa pozycja agenta
        :param i (int): indeks obrazka (numer kroku agenta)
        :param grid (numpy.ndarray): obiekt klasy numpy.ndarray, czyli siatka po której porusza się agent, będąca bitmapą
            0 oznacza pustą kratkę, 1 oznacza kratkę na której znajduje się agent, 2 kratkę w której agent był wcześniej (w tej wersji agent jest dopiero wstawiany na siatkę,
            tzn. domyślnie grid zawiera jedynie zera oraz dwójki)
            0 - brak agenta
            1 - agent
            2 - ślad agenta
        '''

        # wstawienie agenta na odpowiednie miejsce na siatce
        self.grid[pos[0] - 1][pos[1] - 1] = 1

        # generowanie i zapis obrazka
        cmap = colors.ListedColormap(['white', 'red', "#ff8888"])
        plt.figure(figsize=(10, 10))
        plt.pcolor(self.grid[::-1], cmap=cmap, edgecolors='black', linewidths=5)
        plt.xticks(np.arange(1, 20.1, step=1))
        plt.yticks(np.arange(1, 20.1, step=1))
        plt.savefig(self.temp + '//' + str(i))

        # usunięcie agenta z siatki, zastąpienie go śladem
        self.grid[pos[0] - 1][pos[1] - 1] = 2

    def __delete_temp(self):
        '''
        ta metoda usuwa tymczasowy folder z pojedynczymi klatkami wraz  z całą zawartośćią

        usuwa domyślnie 'temporary_images', czyli folder w którym zapisywane są pojedyncze klatki przed wygenerowaniem gifa
        '''
        for (direc, subdirs, files) in os.walk(self.temp):
            for file in files:
                os.remove(os.path.join(self.temp, file))
        os.rmdir(self.temp)

    def __generate_gif(self):
        '''
        ta metoda otwiera archiwum z plikami i znajduje potrzebne pliki .png,
        następnie tworzy z nich gifa, którego zapisuje jako agents_pathDATA.gif w obecnym folderze,
            gdzie data to obecna data i godzina w formacie: YYYY_MM_DD_HH_mm_ss   malejąca znaczącość od roku do sekundy
        '''

        # self.n to ilość klatek, generujemy tablicę n nazwami plików w kolei od 0 - n .png
        images = [str(i) + ".png " for i in range(0, self.n)]

        # do tablicy frames dodaję instancję klasy Image
        frames = []
        for image in images:
            path = os.path.join(self.temp, image)
            new_frame = Image.open(path)
            frames.append(new_frame)

        # mając tablicę potrzebnych klatek generuję gifa i zapisuję go z nazwą zawierającą datę w odpowiednim formacie
        time_now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        frames[0].save('agents_path' + time_now + '.gif', format='GIF',
                       append_images=frames[1:],
                       save_all=True,
                       duration=100, loop=0)



    def __generate_path(self):
        '''
        główna funkcjonalna metoda klasy
        '''

        # startowa pozycja po środku kratki o wymiarach 20 x 20
        pos = 10, 10

        # generuję bitmapę zawierającą same 0
        self.grid = np.zeros(400).reshape(20,20)

        # tworzę tymczasowy folder w którym przechowywane będą wygenerowane obrazy .png
        os.mkdir(self.temp)

        # generuję n klatek, po jednej na każdy ruch agenta
        for i in range(0, self.n):
            pos = self.__jump(pos)
            self.__generate_image(pos, i)

        # wywołuję metodę generującą gifa
        self.__generate_gif()

        # wywołuję metodę usuwającą tymczasowy folder
        self.__delete_temp()




