# 7. Podajemy funkcję (na stałe w programie) np.
# liniową, kwadratową, hiberbole i sprawdzamy jej
# wartość w pkt podanym z klawiatury (nie obsługujemy błędów)

def f(x):
    return x ** 3 - 3 / x


x = float(input("podaj x: "))
print(f(x))
