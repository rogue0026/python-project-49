import math
from secrets import randbelow

from . import engine


def run_game():
    user_name = engine.greeting_user()
    print('Find the greatest common divisor of given numbers.')
    
    attempts = 0
    all_answers_are_correct = True
    while attempts < engine.MAX_ATTEMPTS:
        num1 = randbelow(1, 50)
        num2 = randbelow(1, 50)
        correct_answer = str(math.gcd(num1, num2))
        engine.create_question(f'{num1} {num2}')
        user_answer = engine.receive_user_answer()
        if correct_answer != user_answer:
            engine.send_wrong_answer(user_answer, correct_answer)
            engine.send_try_again(user_name)
            all_answers_are_correct = False
            break
        else:
            attempts += 1
            engine.send_correct_phrase()
    
    if all_answers_are_correct:
        engine.send_congratulations(user_name)
