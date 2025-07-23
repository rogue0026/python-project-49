import prompt


def welcome_user():
    """Welcomes the user."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
