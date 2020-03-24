from math import floor

# źródło: http://www.algorytm.org/przetwarzanie-dat/wyznaczanie-daty-wielkanocy-metoda-meeusa-jonesa-butchera.html
def data_Wielkanocy(year):
    '''Zwraca datę wielkanocy dla żądanego roku

    :param year: (int) - żądany rok
    :return: dd. miesiąc rrrr. roku (str) - data Wielkanocy

    '''
    try:
        year = int(year)
    except:
        raise TypeError
    a = year % 19
    b = floor(year/100)
    c = year % 100
    d = floor(b / 4)
    e = b % 4
    f = floor((b+8)/25)
    g = floor((b - f + 1)/3)
    h = (19 * a + b - d - g + 15) % 30
    i = floor(c/4)
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = floor((a + 11 * h + 22 * l) / 451)
    p = (h + l - 7 * m + 114) % 31
    day = p + 1
    month = floor((h + l - 7*m + 114) / 31)
    months = {
        3 : "marca",
        4 : "kwietnia"
    }
    return str(day) + ". "  + months[month] + " " +  str(year) + ". roku"

