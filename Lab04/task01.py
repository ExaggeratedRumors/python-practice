# 1. Rozwiązywanie równania kwadratowego
# w dziedzinie liczb urojonych (zespolonych)

import cmath


def quadratic_equation(a, b, c):
    if a < 0:
        return "Brak pierwiastków równania kwadratowego"
    delta = b ** 2 - 4 * a * c
    x1 = ((-1) * b - cmath.sqrt(delta)) / (2 * a)
    x2 = ((-1) * b + cmath.sqrt(delta)) / (2 * a)
    return x1, x2


print(quadratic_equation(32, 64, 2224))
