# 5. Napisz program, który obliczy ze wzoru Herona
# pole trójkąta o bokach a,b,c > 0 podanymi z klawiatury .
# Sprawdź najpierw czy to jest faktycznie trójkąt
# (wzór Herona znajdujemy w wikipedii)

# Heron's formula:
# A = 0.25 * sqrt(4 * a^2 * b^2 - (a^2 + b^2 - c^2)^2)

import math


def heron_formula(a, b, c):
    return 0.25 * math.sqrt(4 * a ** 2 * b ** 2 - (a ** 2 + b ** 2 - c ** 2) ** 2)


def data_conditions(a, b, c):
    return a >= 0 and b >= 0 and c >= 0


def math_conditions(a, b, c):
    return (a + b) > c and (a + c) > b and (b + c) > a


print("Podaj boki trójkąta:\n")
[d, e, f] = [int(element) for element in input().split()]

if not (math_conditions(d, e, f) and data_conditions(d, e, f)):
    print("Podano nieprawidłowe dane, taki trójkąt nie istnieje")
else:
    print(f"Pole trójkąta wynosi: {heron_formula(d, e, f)}")
