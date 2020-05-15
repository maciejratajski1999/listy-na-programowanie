from NBP_currencies import NBP_currencies
from Currencies_GUI import Currencies_GUI

if __name__ == '__main__':
    data = NBP_currencies().currencies
    root = Currencies_GUI(data)
    root()