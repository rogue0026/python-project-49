import math
from secrets import randbelow


def gcd_game() -> tuple:
    num1 = randbelow(50)
    num2 = randbelow(50)
    question = f'{num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer