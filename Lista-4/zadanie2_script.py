#!/usr/bin/env python3
import sys
from zadanie2 import Agent

expected_args = "pierwszy argument: \n" \
                "   n (Integer) - ilość klatek w gifie, ilość ruchów agenta \n" \
                "drugi argument: \n" \
                "   temp (String) opcjonalne - nazwa tymczasowego folderu z obrazkami \n"

if __name__ == "__main__":
    args = sys.argv

    if len(args) > 3:
        print("podano za dużo argumentów \n", expected_args)

    if len(args) == 1:
        print("nie podano argumentów \n", expected_args)

    if len(args) == 2:
        n = args[1]
        try:
            __agent = Agent(n)
            __agent()
        except ValueError as val_err:
            print(str(val_err.args[0]))
        except TypeError as typ_err:
            print(str(typ_err.args[0]))

    if len(args) == 3:
        n = args[1]
        temp = args[2]
        try:
            __agent = Agent(n, temp)
            __agent()
        except ValueError as val_err:
            print(str(val_err.args[0]))
        except TypeError as typ_err:
            print(str(typ_err.args[0]))

# przykładowe użycie nie z konsoli:
# my_agent = Agent(100)
# my_agent()

# gif pojawi się w obecnym folderze