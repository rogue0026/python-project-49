import prompt

from . import utils

MAX_ATTEMPTS = 3


def game_engine(game_objective: str, game_func):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_objective)
    attempts = 0
    all_answers_are_correct = True
    while attempts < MAX_ATTEMPTS:
        question_content, correct_answer = game_func()
        utils.create_question(question_content)
        user_answer = utils.receive_user_answer()
        if user_answer != correct_answer:
            all_answers_are_correct = False
            utils.send_wrong_answer(user_answer, correct_answer)
            utils.send_try_again(name)
            break
        else:
            attempts += 1
    if all_answers_are_correct:
        print(f"Congratulations, {name}!")
