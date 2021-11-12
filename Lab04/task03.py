# 3. Konwersja stopni Celsjusza na Fahrenheita
# i odwrotnie (funkcja) def convert_temp(type, value)

def get_data():
    symbol = ''
    while symbol.lower() not in ['f', 'c', 'F', 'C']:
        symbol = input('podaj jednostkę [Celcius] - C, [Farenheit] - F: ')
    temperature = input('Podaj temperaturę: ')
    return symbol, temperature


def convert_temp(symbol, value):
    if symbol == 'f' or symbol == 'F':
        return (value - 32) / 1.8
    if symbol == 'c' or symbol == 'C':
        return value * 1.8 + 32


print(round(convert_temp(get_data(), 2)))
