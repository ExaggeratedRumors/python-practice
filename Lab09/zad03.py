# 2. Czytanie z pliku cereals.csv(wykorzystać moduł csv)
# Zapisywanie do pliku cereals.csv jednego dowolnego wiersza

import csv

with open("cereals.csv", 'r') as csvfile:
    data = csv.reader(csvfile)
    for i in data:
        print(i)

with open("cereals.csv", 'a', newline='') as csvfile:
    my_cereals = ['"My cereals"', '"N "', '"C "', '90', '3', '5', '110', '3.5', '11.5', '9', '130', '15', '1', '2', '0.75',
                  '40.236512', '0', '0', '0', '0', '0', '1', '0']
    writer = csv.writer(csvfile, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(my_cereals)
