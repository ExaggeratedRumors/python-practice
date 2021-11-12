# created by gajda dominik
# zad 4
from Lab03.sum_selected import sum_selected


def sum_all(first, last):
    return sum_selected(True, first, last) \
           + sum_selected(False, first, last)
