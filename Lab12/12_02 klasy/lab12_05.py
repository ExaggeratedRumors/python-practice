# Napisz klasę LiczbaZespolona
# która przechowuje liczby zespolone: a+bi.
# Niech część rzeczywista nazywa się re (od real),a urojona im (od imagine).
# Poza tymi dwoma polami zdefiniuj metody:
# - modul(), oblicza moduł liczby zespolonej a+bi: sqrt(a**2+b**2)
# - add(), multiply(), subtract() (statyczne); obliczają odpowiednio sumę, iloczyn, rożnicę dwóch liczb zespolonych
# oraz zdefiniować metodę dzielenia dóch liczb division()
from math import sqrt


class Zespolona:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def show(self):
        if self.im < 0:
            print(f"{self.re}{self.im}i")
        else:
            print(f"{self.re}+{self.im}i")

    def module(self):
        return sqrt(self.re ** 2 + self.im ** 2)

    @staticmethod
    def add(z1, z2):
        return Zespolona(z1.re + z2.re, z1.im + z2.im)

    @staticmethod
    def subtract(z1, z2):
        return Zespolona(z1.re - z2.re, z1.im - z2.im)

    # (a+bi) * (c+di) = ac-bd + (bc+ad)i
    @staticmethod
    def multiply(z1, z2):
        a = z1.re
        b = z1.im
        c = z2.re
        d = z2.im
        return Zespolona(a * c - b * d, b * c + a * d)

    @staticmethod
    def division(z1, z2):
        return None


def main():
    z1 = Zespolona(1, 4)
    z2 = Zespolona(2, 5)
    z1.show()
    print(z1.module())
    z2.show()
    print(z2.module())
    Zespolona.add(z1, z2).show()
    Zespolona.subtract(z1, z2).show()
    Zespolona.multiply(z1, z2).show()


if __name__ == "__main__":
    main()
