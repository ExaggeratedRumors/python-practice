# created by gajda dominik
# zad 3

from Lab03.is_even import is_even


def sum_selected(even=True, first=0, last=100):
    sum_in_range = 0
    for num in range(first, last + 1):
        if (is_even(num) and even) \
                or (not is_even(num) and not even):
            sum_in_range += num
    return sum_in_range
