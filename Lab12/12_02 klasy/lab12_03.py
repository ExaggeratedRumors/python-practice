# 3. Zdefiniować klasę Calculator
# (Standardowy + - * / opcja zapamiętywania oraz kasowania wyniku)
# metody add(self, amount), subtract(self, amount), multiply(self, amount), division(self, amount).
# Gdzie amount wartość, która jest np. dodawana do wartości w pamięci current.
import math

class Calculator:
    current = 0

    def add(self, amount):
        self.current += amount

    # lub
    def add1(self, a1, a2):
        self.current += a1 + a2

    def subtract(self, amount):
        self.current -= amount

    def multiply(self, amount):
        self.current *= amount

    def division(self, amount):
        self.current /= amount


c1 = Calculator()
c1.add(15)
print(c1.current)
# lub
c1.add1(10, 4)
print(c1.current)

# Zdefiniować klasę ScientificCalculator, która dziedziczy po klasie Calculator
# Zawiera metody pierwiastek_kwadratowy, zamiana rad na kąty i odwrotnie oraz sin i cos

class ScientificCalculator(Calculator):
    def square_root(self):
        self.current = math.sqrt(self.current)

    def to_degrees(self):
        self.current = math.degrees(self.current)

    def to_radians(self):
        self.current = math.radians(self.current)

    def sin(self):
        self.current = math.sin(self.current)

    def cos(self):
        self.current = math.cos(self.current)