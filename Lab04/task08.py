# 8. Liczymy całkę z funkcji podanej na stałe w
# programie podając jednocześnie krok całkowania.
# Sprawdzić różnicę przy podaniu różnych kroków całkowania.
import numpy as np


def f(x):
    return x ** 3 - 3 / x


def integral(x1, x2, dx):
    result = 0
    for x in np.arange(float(x1), float(x2), float(dx)):
        result += f(x)
    return result


print(integral(1, 5, 0.2))
