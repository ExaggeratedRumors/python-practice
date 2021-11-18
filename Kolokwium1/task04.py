# 4. Napisz skrypt, który policzy ile słów
# jest w dowolnym zdaniu
# (separator wyrazów to spacja ' ' - można wykorzystać fukcję split)
# np. (s = 'PYTHON. To jest kolokwium z przedmiotu Programowanie skryptowe, które wykorzystuje język python. PythoN jest OK').
# Następnie policzyć ilość wystąpień słowa 'python'
# pisanego znakami dowolnej wielkości.
# Następnie zamień słowo 'python' pisane
# dowolną wielkością literami na duże litery i
# wyświetl całą frazę bez zmiany wielkości pozostałych wyrazów.

delimiter = ' '
s = 'PYTHON. To jest kolokwium z przedmiotu Programowanie skryptowe, które wykorzystuje język python. PythoN jest OK'
splitted_s = s.split(delimiter)
print(f"Liczba słów w łańcuchu s: {len(splitted_s)}")

counter = 0
for i in splitted_s:
    if i.lower().__contains__('python'):
        counter += 1
        i.upper()

print(f"Liczba wystąpień słowa \'python\' {counter}")
print(delimiter.join(splitted_s))




