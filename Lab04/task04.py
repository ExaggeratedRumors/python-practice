# 4. Obliczanie BMI jako funkcja bmi(height, mass)
# zwraca informację w postaci liczby BMI, a następnie
# funkcję bmi_opis(height, mass), która zwraca opis
# słowny, niedowaga, waga poprawna itd. wykorzystując
# w swoim ciele funkcję bmi(height, mass)


def bmi(height, mass):
    bmi_value = mass / (height ** 2)
    return bmi_value


def bmi_opis(height, mass):
    bmi_value = bmi(height, mass)
    if bmi_value < 18.5:
        return 'niedowaga'
    if bmi_value < 25:
        return 'waga poprawna'
    if bmi_value < 30:
        return 'nadwaga'
    if bmi_value >= 30:
        return 'otyłość'


print(bmi_opis(1.53, 99.3))
