# 2. Zapisywanie błędów aplikacji (obsługa błędów).
# Format pliku: Data - opis błędu (try except)
import codecs
import datetime

try:
    number = input("wprowadź liczbę: ")
    if number == 1:
        raise BaseException("Została wprowadzona jedynka")
    divide = 6 / number
except BaseException as e:
    path = "exceptions.txt"
    date = datetime.datetime.today()
    with codecs.open(path, "a", "utf-8") as file:
        file.write(f"\n{date}: {type(e)=}, {e.args}")
