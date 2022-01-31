class Analiza:
    def __init__(self, lista):
        self.lista = lista
        self.wynik = 0

    def suma(self):
        self.wynik = sum(self.lista)
        return self.wynik

    def print_suma(self):
        print(self.wynik)


# TEST

def test():
    lista = [34, 65, 53, 12, 94, 23]
    obj = Analiza(lista)
    obj.suma()
    obj.print_suma()
    print(f"Test sumy wyrażeń listy: {sum(lista)}")
    print(f"Wartości są równe: {obj.wynik == sum(lista)}")


if __name__ == "__main__":
    test()
