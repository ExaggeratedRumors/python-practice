# Rysowanie diagramu z ilością ocen 2,2.5,3,3.5,4,4.5,5 z kolokwium
# z pliku zewnętrznego (na początku z listy)
import matplotlib.pyplot as plt

marks = {2: 0, 2.5: 0, 3: 0, 3.5: 0, 4: 0, 4.5: 0, 5: 0}

with open("kolokwium.txt") as file:
    result = [float(line.split()[1]) for index, line in enumerate(file) if index > 0]

for i in result:
    marks[i] += 1

labels = [i for i, _ in enumerate(marks.keys())]

plt.bar(labels, marks.values(), color='blue')
plt.xlabel("Ocena")
plt.ylabel("Liczba ocen")
plt.title("Kolokwium 1")
plt.xticks(labels, marks.keys())
plt.show()
