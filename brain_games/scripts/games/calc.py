from random import randint
from random import choice

from . import engine


def run_game():
    user_name = engine.greeting_user()
    print('What is the result of the expression?')
    attempts = 0
    all_answers_are_correct = True
    while attempts < engine.MAX_ATTEMPTS:
        statement = create_statement()
        right_answer = get_right_answer(statement)
        engine.create_question(f"{statement[0]} {statement[1]} {statement[2]}")
        user_answer = engine.receive_user_answer()
        if user_answer != str(right_answer):
            all_answers_are_correct = False
            engine.send_wrong_answer(user_answer, right_answer)
            engine.send_try_again(user_name)
            break
        else:
            engine.send_correct_phrase()
        attempts += 1
    if all_answers_are_correct:
        engine.send_congratulations(user_name)
        

def create_statement() -> tuple:
    arithmethic_operations = ['+', '-', '*']
    op_left = randint(1, 50)
    op_right = randint(1, 50)
    operation = choice(arithmethic_operations)
    return (op_left, operation, op_right)
    

def get_right_answer(statement):
    match statement[1]:
        case '+':
            return int(statement[0]) + int(statement[2])
        case '-':
            return int(statement[0]) - int(statement[2])
        case '*':
            return int(statement[0]) * int(statement[2])
