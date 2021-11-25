# Dla pliku dane.dat obliczyć prędkość w danej chwili v=s/t i zapisać do pliku dane1.dat w miejscu prędkości zamiast 0.000000.

with open('dane.dat') as file:
    comment = [line for line in file if line[0] == "#"]
    file.seek(0)
    data = [[float(val) for val in line.split()] for line in file if line[0] != "#"]

output = []

for line in data:
    line[2] = line[1]/line[0]
    output.append(''.join(str(line)))
    print(line)

with open('newdane.txt', 'w') as file:
    for a in comment:
        file.write(a)
    for b in output:
        file.write(b+'\n')
