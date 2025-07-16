from secrets import randbelow


def even_game() -> tuple:
    number = randbelow(1000)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return number, correct_answer
