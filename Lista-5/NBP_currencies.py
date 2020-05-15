import urllib.request
import json
class NBP_currencies:
    '''
    Klasa sczytuje dane do pliku JSON w linku self.url i przemienia je w wygodny do użycia format
    '''

    def __init__(self):
        ''' currencies (Dictionary) : {"kod i nazwa waluty" : wartość (Float)}'''
        # url strony, z której będziemy pobierać dane
        self.url = 'https://api.nbp.pl/api/exchangerates/tables/A'

        # pobieranie danych ze strony NBP
        try:
            self.__download_data()
        # w przypadku braku połączenia ze stroną internetową
        except urllib.error.URLError:
            print('brak połączenia z internetem, wczytuję z archiwum')
        # generowanie słownika z danych
        try:
            self.currencies = self.__generate_currencies()
        # jeśli nie znaleziono pliku z danymi
        except IOError:
            print("nie znaleziono pliku nbp_data.json")

    def __call__(self):
        '''
         w przypadku wywołania instancji tej klasy, zwracany jest słownik currencies

         :return: currencies (Dictionary) : {"kod i nazwa waluty" : kurs (Float)}'''
        return self.currencies

    def __download_data(self):
        '''
        metoda wywoływana przy inicjalizacji klasy, pobiera z url dane NBP, konwertuje do typu List i zapisuje je w pliku JSON
        '''
        # pobieram JSON z url za pomocą dostępnego API
        request = urllib.request.Request(self.url)
        request.add_header('Accept', 'application/json')
        response = urllib.request.urlopen(request)
        # konwertuję otrzymany plik z typu Bytes do typu List
        json_bytes = response.read()
        json_string = json_bytes.decode('utf-8')
        json_list = json.loads(json_string)
        # i zapisuję do pliku JSON
        with open('nbp_data.json', 'w') as data_file:
            json.dump(json_list, data_file, indent=1)

    def __generate_currencies(self):
        '''
        metoda sczytuje dane z pliku JSON i wybiera potrzebne informacje, a następnie tworzy z nich słownik currencies
        :return currencies (Dictionary) : {"kod i nazwa waluty" : wartość (Float)}
        '''
        # wczytuję dane z pliku
        with open('nbp_data.json', 'r') as data_file:
            json_list = json.load(data_file)
            json_dict = json_list[0]
        # generuję wygodniejszy dla mnie słownik nazwa_waluty : kurs w zł
        currencies_data = json_dict["rates"]
        currencies = {}
        for currency in currencies_data:
            currencies[currency['code'] + " " + currency['currency']] = currency['mid']
        return currencies
