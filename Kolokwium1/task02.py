# 2. Poszukujemy kwadratów liczb naturalnych od 1 do 300,
# o wartościach z przedziału otwartego (500, 10000).
# Zapisz te liczby naturalne (przed podniesieniem do kwadratu)
# w postaci listy o nazwie list_output i wyświetl je.

n_min = 1
n_max = 300


def conditions(number):
    q_min = 500
    q_max = 10000
    return q_min < number < q_max


natural_list = [n for n in range(n_min, n_max + 1)]
new_array = [x for x in natural_list if conditions(x ** 2)]
print(new_array)
