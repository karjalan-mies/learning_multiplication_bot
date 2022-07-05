import logging
from random import randint


def get_x(list_of_numbers: list) -> tuple:
    try:
        x = list_of_numbers.pop(randint(0, len(list_of_numbers)-1))
        return x, list_of_numbers
    except ValueError:
        list_of_numbers = [i for i in range(1, 10)]
        x = list_of_numbers.pop(randint(0, len(list_of_numbers)-1))
        return x, list_of_numbers
