# 7. Mamy do despozycji plik baseball.txt
# Należy wyświetlić wszystkich zawodnikaów z drużyny 'OAK'
# Którzy zawodnicy rzucili najwięcej za trzy punkty?
# Którzy zawodnicy rzucili najwięcej za trzy punkty średnio w jednym meczu?

import re

with open("baseball.txt") as file:
    labels = file.readline()
    data = [[re.sub('[*#]', '', val) for val in line.split()] for line in file]

oak_players = [val for val in data if val[3] == "OAK"]
for i in oak_players:
    print(i)

triples = [float(player[9]) for player in oak_players]
max_triples = max(triples)
indexes = []
for i in range(0, len(triples)):
    if triples[i] == max_triples:
        indexes.append(oak_players[i])

print(f"\nZawodnicy którzy rzucili najwięcej za 3 punkty:")
for i in indexes:
    print(" ".join(i[0:2]))

avg_triples = [float(player[9])/float(player[4]) for player in oak_players]
max_avg_triples = max(avg_triples)
indexes = []
for i in range(0, len(avg_triples)):
    if avg_triples[i] == max_avg_triples:
        indexes.append(oak_players[i])
print(f"\nZawodnicy którzy rzucili najwięcej za 3 punkty średnio na mecz:")
for i in indexes:
    print(" ".join(i[0:2]))
