# created by gajda dominik
# zad 2
from is_even import is_even


def sum_even(first, last):
    sum_in_range = 0
    for num in range(first, last):
        if is_even(num):
            sum_in_range += num
    return sum_in_range
