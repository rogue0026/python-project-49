from math import sqrt
from random import randint

from . import engine


def run_game():
    user_name = engine.greeting_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    
    all_answers_are_correct = True
    attempts = 0
    while attempts < engine.MAX_ATTEMPTS:
        number = randint(1, 100)
        engine.create_question(number)
        user_answer = engine.receive_user_answer()
        correct_answer = is_prime(number)
        if user_answer != correct_answer:
            all_answers_are_correct = False
            engine.send_wrong_answer(user_answer, correct_answer)
            engine.send_try_again(user_name)
            break
        else:
            engine.send_correct_phrase()
            attempts += 1
            continue
    
    if all_answers_are_correct:
        engine.send_congratulations(user_name)


def is_prime(num: int) -> str:
    if num < 2:
        return 'no'
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return 'no'
    return 'yes'
