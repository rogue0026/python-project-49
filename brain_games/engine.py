import prompt

MAX_ATTEMPTS = 3


def game_engine(game_module):
    """Starts game logic.

    Parameters description:\n
    game_module - must contain a function with signature:\n
    def run_game() -> tuple.\n
    You should return question and correct answer from any game.
    """
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
        if user_answer != str(correct_answer):
            all_answers_are_correct = False
            send_wrong_answer(user_answer, correct_answer)
            send_try_again(name)
            break
        else:
            attempts += 1
    if all_answers_are_correct:
        print(f"Congratulations, {name}!")


def receive_user_answer() -> str:
    """Waits for input from user."""
    return prompt.string('Your answer: ')


def create_question(content: str):
    """Sends question to the user."""
    print(f"Question: {content}")


def send_wrong_answer(wrong: str, right: str):
    """Sends a phrase about an incorrect response."""
    print(f"'{wrong}' is wrong answer ;(. Correct answer was '{right}'.")


def send_correct_phrase():
    """Sends a phrase about a correct response."""
    print("Correct!")


def send_try_again(name: str):
    """Sends a phrase asking user to try again."""
    print(f"Let's try again, {name}!")
