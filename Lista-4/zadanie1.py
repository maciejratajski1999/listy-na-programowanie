from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

class wahadlo:
    def __init__(self, Q, om, A, v0, th0):
        self.Q, self.om, self.A, self.v0, self.th0 = self.__test_for_var(Q, om, A, v0, th0)
        self.g = 9.8
        self.l = self.g / (self.om**2)
        self.x0 = [th0, v0]

    def __call__(self):
        self.wykresy()

    def __test_for_var(self, *args):
        '''
        ta metoda sprawdza czy wszystkie podane argumenty są liczbami

        :param args (tuple): dane do zadanie liczby
        :return (tuple): liczby przekonwertowane na typ float
        '''
        new_args = []
        for arg in args:
            print(arg)
            try:
                new_arg = float(arg)
            except ValueError:
                try:
                    slash_i = arg.find("/")
                    new_arg = float(arg[:slash_i]) / float(arg[slash_i + 1:])
                except:
                    raise TypeError("wszystkie argumenty muszą być liczbami, wystąpił błąd, ponieważ podano: \n" + arg)
            except TypeError:
                return tuple(new_args)
            new_args.append(new_arg)
        return tuple(new_args)



    def dy(self, x, t):
        '''
        :param x (list):
        :param t (int):
        :return:
        '''
        tau = (self.g/self.l)**(1/2)*t
        return [x[1], self.A*np.cos(self.om*tau) - (1/self.Q)*x[1] - np.sin(x[0])]

    def wykresy(self):
        '''
        rysuje i pokazuje wykres
        '''

        # 100'000 próbek czasu
        t = np.linspace(0, 100, 100000)

        x = odeint(self.dy, self.x0, t)

        # wykres położenia od czasu
        plt.subplot(1,2,1)
        plt.plot(t, x[:,0])
        plt.xlabel("czas")
        plt.ylabel("położenie (radian)")

        # wykres prędkości od położenia
        plt.subplot(1,2,2)
        plt.plot(x[:,0], x[:,1])
        plt.xlabel("położenie (radian)")
        plt.ylabel("prędkość")
        plt.show()