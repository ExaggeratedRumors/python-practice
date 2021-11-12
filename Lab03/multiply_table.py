# created by gajda dominik
# zad 6
def multiply_table():
    for i in range(1, 11):
        if i < 10:
            print(end=' ')
        for j in range(1, 11):
            k = i * j
            space = ' '
            if i * (j + 1) < 100:
                space += ' '
            if i * (j + 1) < 10:
                space += ' '
            print(k, end=space)
        print()