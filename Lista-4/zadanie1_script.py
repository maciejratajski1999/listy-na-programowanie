#!/usr/bin/env python3
from zadanie1 import wahadlo
import sys

expected_args = "Q \n om \n A \n v0 \n th0 \n" \
                "wszystkie typu float"

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 6:
        print("zła ilość argumentów, oczekiwano: \n", expected_args)
    else:
        Q, om, A, v0, th0 = args[1:]
        try:
            __wahadlo = wahadlo(Q, om, A, v0, th0)
            __wahadlo()
        except TypeError as typ_err:
            print(typ_err.args[0])


# # przykładowe użycia nie z konsoli
# # przykład 1
#
# first = wahadlo(2, 2/3, 0.5, 0, 0.01)
# first()
#
# # przykład 2
#
# second = wahadlo(2, 2/3, 0.5, 0, 0.3)
# second()
#
# # przykład 3
#
# third = wahadlo(2, 2/3, 1.35, 0, 0.3)
# third()