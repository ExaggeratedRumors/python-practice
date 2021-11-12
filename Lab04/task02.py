# 2. Konwersja km na mile i odwrotnie. W programie
# wybieramy w pętli aż podamy poprawny wybór np.
# 'Podaj typ konwersji [km->mile]- 0, [mile->km]-1'.
# Na tej podstawie wykonujemy funkcje wcześniej zdefiniowaną
# km_mile(distance) lub mile_km(distance)


def km_mile(distance):
    return distance / 1.609344


def mile_km(distance):
    return distance * 1.609344


y = ''
while y.lower() not in ['k', 'm']:
    y = input('Podaj typ konwersji [km->mile] - k, [mile->km] - m: ')


odl = -1.0
while not odl > 0:
    odl = float(input('Podaj odległość = '))

if y == 'm':
    wynik = mile_km(odl)
elif y == 'k':
    wynik = km_mile(odl)
else:
    wynik = 0