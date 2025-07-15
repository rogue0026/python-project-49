from secrects import randbelow

from . import engine


def run_game():
    user_name = engine.greeting_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    all_answers_are_correct = True
    attempts = 0
    while attempts < engine.MAX_ATTEMPTS:
        number = randbelow(0, 1000)
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        engine.create_question(number)
        user_answer = engine.receive_user_answer()
        if user_answer != correct_answer:
            all_answers_are_correct = False
            engine.send_wrong_answer(user_answer, correct_answer)
            engine.send_try_again(user_name)
            break
        else:
            engine.send_correct_phrase()
            attempts += 1

    if all_answers_are_correct:
        engine.send_congratulations(user_name)


if __name__ == '__main__':
    run_game()
