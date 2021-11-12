# created by gajda dominik
# zad 9
import random


def throw(number_of_throws):
    total_sum = 0
    for i in range(0, number_of_throws):
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        total_sum += (first_dice + second_dice)
    return total_sum


def play(number_of_games):
    less_than_21 = 0
    more_than_21 = 0
    blackjack = 0
    number_of_losses = 1

    for t in range(0, number_of_games):
        throws = input("ile razy chcesz rzucić? ")
        result = throw(int(throws))
        print("Wynik: ", result)
        if result < 21:
            less_than_21 += (21 - result)
        elif result == 21:
            blackjack += 1
        else:
            more_than_21 += (result - 21)
            number_of_losses += 1

    less_than_21 /= number_of_games
    more_than_21 /= number_of_losses
    return less_than_21, blackjack, more_than_21


game = input("ile razy chcesz zagrać? ")
print("Twój wynik: ", play(3))
