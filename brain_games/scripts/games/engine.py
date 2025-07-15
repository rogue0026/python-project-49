import prompt

MAX_ATTEMPTS = 3


def greeting_user() -> str:
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def create_question(content: str):
    print(f"Question: {content}")


def receive_user_answer() -> str:
    return prompt.string('Your answer: ')
    

def send_correct_phrase():
    return "Correct!"


def send_wrong_answer(wrong: str, right: str):
    print(f"'{wrong}' is wrong answer ;(. Correct answer was '{right}'.")


def send_try_again(name: str):
    print(f"Let's try again, {name}")


def send_congratulations(name: str):
    print(f"Congratulations, {name}")
