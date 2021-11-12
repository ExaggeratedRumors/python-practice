# 1. Dana jest lista:
# lista = [7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 4, 5, 3, 19, 71, 21]
# Trzeba odnaleźć takie dwie kolejne liczby, że druga jest kwadratem pierwszej.

# operowanie na łańuchu
any_flag = True
print("we stay at home" if any_flag else "we go out")

lista = [7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 4, 5, 3, 19, 71, 21]

for i in range(0, len(lista)):
    new_array = [x for x in lista if x == lista[i]**2]
    if new_array:
        print(lista[i], " ", new_array)
