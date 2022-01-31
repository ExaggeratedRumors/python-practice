import datetime

file_name = "student.txt"
name = "Gajda Dominik"
index = 240661
group_number = "I6"
date = datetime.datetime.now()

with open(file_name, 'w') as file:
    file.write(f"{name}\r{index}\r{group_number}\r{date}\r")

with open(file_name, 'r', newline='') as file:
    lista_wynikowa = [line for line in file]

for element in lista_wynikowa:
    print(element)
