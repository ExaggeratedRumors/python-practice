# 3. Dana jest lista:
# lista = [7, 13, 3, 6, 18, 6, 25, 5, 24, 4, 4, 5, 3, 19, 71, 21]
# Znajdz wszystkie trzy kolejne liczby z listy, które są malejące.


lista = [7, 13, 3, 6, 18, 6, 25, 5, 24, 4, 4, 5, 3, 19, 71, 21]

substring_length = 3
malejace = []

for i in range(1, len(lista)):
    temp = [lista[i]]
    index = 0
    for j in range(i, len(lista)):
        if lista[j] < temp[index] and index < substring_length:
            temp.append(lista[i])
            index += 1
    malejace.append(temp)

print(malejace)