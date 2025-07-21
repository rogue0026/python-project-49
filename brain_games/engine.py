import prompt

MAX_ATTEMPTS = 3


def game_engine(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module.GAME_OBJECTIVE)
    attempts = 0
    all_answers_are_correct = True
    while attempts < MAX_ATTEMPTS:
        question_content, correct_answer = game_module.run_game()
        create_question(question_content)
        user_answer = receive_user_answer()
        if user_answer != correct_answer:
            all_answers_are_correct = False
            send_wrong_answer(user_answer, correct_answer)
            send_try_again(name)
            break
        else:
            attempts += 1
    if all_answers_are_correct:
        print(f"Congratulations, {name}!")


def receive_user_answer() -> str:
    return prompt.string('Your answer: ')


def create_question(content: str):
    print(f"Question: {content}")


def send_wrong_answer(wrong: str, right: str):
    print(f"'{wrong}' is wrong answer ;(. Correct answer was '{right}'.")


def send_correct_phrase():
    print("Correct!")


def send_try_again(name: str):
    print(f"Let's try again, {name}!")
