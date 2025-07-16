from math import sqrt
from secrets import randbelow


def is_prime(num: int) -> str:
    if num < 2:
        return 'no'
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return 'no'
    return 'yes'


def game_prime():
    question = randbelow(100)
    correct_answer = is_prime(question)
    return question, correct_answer
