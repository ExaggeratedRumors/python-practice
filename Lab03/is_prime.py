# created by gajda dominik
# zad 5

def is_prime(number):
    for num in range(1, number + 1):
        print(num)
        if number % num == 0 \
                and num != 1 \
                and num != number:
            return False
    return True
