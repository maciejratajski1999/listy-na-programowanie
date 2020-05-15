from bs4 import BeautifulSoup, Tag
import urllib.request

class NBP_currencies:

    def __init__(self):
        self.url = "https://www.nbp.pl/home.aspx?f=/kursy/kursya.html"
        self.currencies = self.__generate_currencies(self.__find_currencies())

    def __call__(self):
        return self.currencies

    def __find_currencies(self):
        with urllib.request.urlopen(self.url) as response:
            page = BeautifulSoup(response, 'html.parser')
            url2 = 'https://www.nbp.pl' + page.find_all(id="article")[0].find_all("a")[1]['href']
        with urllib.request.urlopen(url2) as response:
            page = BeautifulSoup(response, 'html.parser')
        currencies_html = page.find_all('pozycja')
        currencies_list = []
        for position in currencies_html:
            currency = {
                "name": position.find('nazwa_waluty').contents[0],
                "multiplier": int(position.find('przelicznik').contents[0]),
                "code": position.find('kod_waluty').contents[0],
                "mean_price": float(position.find('kurs_sredni').contents[0].replace(",", "."))
            }
            currencies_list.append(currency)
        return currencies_list

    def __generate_currencies(self, currencies_list):
        currencies = {cur["code"] + " " + cur["name"] : cur["mean_price"] / cur["multiplier"] for cur in currencies_list}
        return currencies

