# created by gajda dominik
# zad 7
def multiply_while():
    i = 1
    while i != 11:
        if i < 10:
            print(end=' ')
        j = 1
        while j != 11:
            k = i * j
            space = ' '
            if i * (j + 1) < 100:
                space += ' '
            if i * (j + 1) < 10:
                space += ' '
            print(k, end=space)
            j += 1
        i += 1
        print()