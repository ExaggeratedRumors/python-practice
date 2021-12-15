# 1. Wyświetlamy, każdą kolumnę i wartości w kolumnie występujące w pliku california1.txt.
# Całość zapisujemy do pliku california.csv jako plik tekstowy z separatorem średnik ';'.
# Jaka jest populacja ludzi we wszystkich miastach w przedziale wieku 18 - 64 lata
# i jaki to procent wszystkich ludzi.
# plik california1.txt jest taki sam jak pobrany w zad5 z poprzednich zajęć.

separator = ';'

with open("california1.txt") as file:
    labels = file.readline()
    data = [[val for val in line.split()] for line in file]

output = []
for i in data:
    city = " ".join(i[-len(i):-5])
    for j in range(6, len(i)):
        i.pop(-6)
    i[-6] = city
    output.append(separator.join(i))


avg = sum([float(i[1]) * 0.01 * float(i[3]) for i in data])
population = sum([float(i[1]) for i in data])
print(f"Populacja mieszkańców między 18 a 64 rokiem życia wynosi"
      f" {round(avg)} i stanowi {round(100 * avg/population,2)}% wszystkich mieszkańców")

with open("california.txt", 'w') as file:
    file.write(labels.replace(',', ';'))
    for i in output:
        file.write(i + "\n")
