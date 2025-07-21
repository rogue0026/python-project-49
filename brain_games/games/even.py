from secrets import randbelow


GAME_OBJECTIVE = 'Answer "yes" if the number is even, otherwise answer "no".'


def run_game() -> tuple:
    number = randbelow(1000)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return number, correct_answer
