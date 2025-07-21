import math
from secrets import randbelow


GAME_OBJECTIVE = 'Find the greatest common divisor of given numbers.'


def run_game() -> tuple:
    num1 = randbelow(50)
    num2 = randbelow(50)
    question = f'{num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer
