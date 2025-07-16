import prompt


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
