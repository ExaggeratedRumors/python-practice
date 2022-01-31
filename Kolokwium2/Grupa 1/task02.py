class Koszyk:
    def __init__(self, lista):
        self.suma = 0
        self.lista = lista

    def koszyk_suma(self):
        self.suma = 0
        for i in self.lista:
            self.suma += float(i.get("price"))
        return self.suma

    def print_suma(self):
        print(f"Wartość koszyka: {self.suma}")


# TEST

def test():
    lista = [{'name': 'Pepsi', 'quantity': 3, 'price': 3.5},
             {'name': 'Water', 'quantity': 1, 'price': 1.5},
             {'name': 'Orange', 'quantity': 5, 'price': 7.25}]
    obj = Koszyk(lista)
    obj.koszyk_suma()
    obj.print_suma()


if __name__ == "__main__":
    test()
