# created by gajda dominik
# zad 8
import math


def quadratic_equation(a, b, c):
    if a == 0:
        return "to nie jest równanie kwadratowe"
    delta = math.pow(b, 2) - (4 * a * c)
    if delta < 0:
        return "brak rozwiązań"
    elif delta == 0:
        return (-1) * b / (2 * a)
    else:
        return ((-1) * b - math.sqrt(delta)) / (2 * a), ((-1) * b + math.sqrt(delta)) / (2 * a)
