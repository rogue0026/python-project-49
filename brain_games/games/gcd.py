import math
from random import randint


GAME_OBJECTIVE = 'Find the greatest common divisor of given numbers.'


def run_game() -> tuple:
    """Implements the logic of the game."""
    num1 = randint(1, 50)
    num2 = randint(1, 50)
    question = f'{num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer
