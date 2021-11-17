# 11. Pobierz od użytkownika n liczb i
# zapisz je na liście. Wydrukuj: elementy
# listy i ich indeksy (enumerate),
# elementy w odwrotnej kolejności,
# posortowane elementy. Usuń z listy
# pierwsze wystąpienie elementu podanego
# przez użytkownika. Usuń z listy element
# o podanym indeksie. Podaj ilość
# wystąpień oraz indeks pierwszego
# wystąpienia podanego elementu. Wybierz
# z listy elementy od indeksu i do j.

print("Podaj liczby:\n")
_input = [int(item) for item in input().split()]
for idx, val in enumerate(_input):
    print(idx, val)
