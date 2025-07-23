from math import sqrt
from random import randint


GAME_OBJECTIVE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num: int) -> bool:
    """Computes, are number is prime or not."""
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def run_game():
    """Implements the logic of the game."""
    question = randint(1, 100)
    if is_prime(question):
        return question, 'yes'
    return question, 'no'
