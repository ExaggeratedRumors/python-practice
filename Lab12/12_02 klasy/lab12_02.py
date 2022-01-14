# 2. Utworzyć klasę Employee, która dziedziczy po klasie Person
# i zawiera dodatkowy atrybut Age.
# Zdefiniuj metodę displayEmployee(), która wyświetla nazwę pracownika,
# pensję oraz wiek.

from lab12_01 import Person  # lub skopiować daną klasę z pliku lab12_01.py


class Employee(Person):
    def __init__(self, name, salary, age):
        super().__init__(name, salary)
        self.age = age

    def displayEmployee(self):
        print(f'name: {self.name}, salary: {self.salary}, age: {self.age}')


if __name__ == "__main__":
    pracownik1 = Employee('Anna', 500, 25)
    pracownik2 = Employee('Piotr', 300, 31)
    pracownik1.displayEmployee()
    pracownik2.displayEmployee()

input('press any key -- Employee')
