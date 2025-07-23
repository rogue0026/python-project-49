from random import randint


GAME_OBJECTIVE = 'What number is missing in the progression?'


def generate_sequence() -> tuple:
    """Generates arithmetic progression sequence."""
    step = randint(1, 10)
    begin_number = randint(1, 50)

    sequence = [str(begin_number)]

    for _ in range(9):
        sequence.append(str(begin_number + step))
        begin_number += step
    replace_index = randint(0, len(sequence) - 1)
    correct_answer = sequence[replace_index]
    sequence[replace_index] = '..'
    return sequence, correct_answer


def run_game() -> tuple:
    """Implements the logic of the game."""
    sequence, answer = generate_sequence()
    question = ' '.join(sequence)
    return question, answer
