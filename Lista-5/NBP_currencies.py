from bs4 import BeautifulSoup, Tag
import urllib.request
import json

class NBP_currencies:
    '''
    Klasa sczytuje dane z pliku HTML w linku self.url i przemienia je w wygodny do użycia format
    '''

    def __init__(self):
        ''' currencies (Dictionary) : ("kod i nazwa waluty" : wartość w typie Float)'''
        # url pliku html, lub strony, z której będziemy pobierać dane
        self.url = "https://www.nbp.pl/home.aspx?f=/kursy/kursya.html"

        # generowanie danych do self.currencies
        try:
            self.currencies = self.__generate_currencies(self.__find_currencies())

        # w przypadku braku połączenia ze stroną internetową, załaduj dane z pliku .json
        except urllib.error.URLError:
            with open('currencies.json') as data_file:
                self.currencies = json.load(data_file)

    def __call__(self):
        '''
         w przypadku wywołania instancji tej klasy, zwracany jest słownik currencies

         :return: currencies (Dictionary) : {"kod i nazwa waluty" : kurs (Float)}'''
        return self.currencies

    def __find_currencies(self):
        '''
        ta metoda szuka w self.url odpowiednich pozycji i zwraca listę słowników,
        w której każdy słownik zawiera informacje dotyczące jednej waluty

        :return: currencies_list (List of Dictionaries) : każdy słownik zawiera dane jednej waluty
                                        [{"name" : "nazwa waluty",
                                        "multiplier" : przelicznik (Integer),
                                        "code" : "KOD waluty",
                                        "mean_price" : średni kurs (Float)}]
        '''

        # ten fragment kodu jest wzięty z Pani przykładu data_from_net.py
        with urllib.request.urlopen(self.url) as response:
            page = BeautifulSoup(response, 'html.parser')
            url2 = 'https://www.nbp.pl' + page.find_all(id="article")[0].find_all("a")[1]['href']
        with urllib.request.urlopen(url2) as response:
            page = BeautifulSoup(response, 'html.parser')

        # każda osobna waluta jest wpisana w tag <pozycja> w pliku HTML, więc tworzę listę wszystkich <pozycji>
        currencies_html = page.find_all('pozycja')
        currencies_list = []
        for position in currencies_html:
        # sczytuję dane z kolejnych tagów w każdej pozycji i tworzę z nich słownik
            currency = {
                "name": position.find('nazwa_waluty').contents[0],
                "multiplier": int(position.find('przelicznik').contents[0]),
                "code": position.find('kod_waluty').contents[0],
                "mean_price": float(position.find('kurs_sredni').contents[0].replace(",", "."))
            }
        # i dodaję słownik do listy
            currencies_list.append(currency)
        return currencies_list

    def __generate_currencies(self, currencies_list):
        '''
        Ta funkcja przerabia listę słowników zawierających dane pojedynczych walut na słownik, który będzie bardziej praktyczny w przypadku przeliczania kursów walut

        :param currencies_list (List of Dictionaries): lista słowników generowana przez metodę __find_currencies
                                        [{"name" : "nazwa waluty",
                                        "multiplier" : przelicznik (Integer),
                                        "code" : "KOD waluty",
                                        "mean_price" : średni kurs (Float)}]

        :return currencies (Dictionary):  {"kod i nazwa waluty" : kurs (Float)}
        '''
        # generuję słownik z listy, w którym każda para klucz : wartość odpowiada jednej parze waluta : kurs
        currencies = {cur["code"] + " " + cur["name"] : cur["mean_price"] / cur["multiplier"] for cur in currencies_list}

        # zapisujemy dane do pliku .json, aby mieć dostęp do danych offline
        with open('currencies.json', 'w') as data_file:
            json.dump(currencies, data_file, indent=1)

        return currencies

