from secrets import randbelow


GAME_OBJECTIVE = 'What number is missing in the progression?'


def generate_sequence() -> list:
    step = randbelow(9) + 1
    begin_number = randbelow(50) + 1
    sequence = [str(begin_number)]

    for _ in range(9):
        sequence.append(str(begin_number + step))
        begin_number += step
    replace_index = randbelow(len(sequence))
    sequence[replace_index] = '..'
    return sequence


def get_unknown_element(sequence: list) -> str:
    left = 0
    right = left + 1
    while right < len(sequence):
        if sequence[left] != '..' and sequence[right] != '..':
            break
        else:
            left += 1
            right += 1
        
    step = int(sequence[right]) - int(sequence[left])
    
    idx = sequence.index('..')
    unknown_element = None
    
    if idx == 0:
        unknown_element = int(sequence[idx + 1]) - step
    elif idx == len(sequence) - 1 or (idx != 0 and idx != len(sequence) - 1):
        unknown_element = int(sequence[idx - 1]) + step

    return str(unknown_element)


def run_game() -> tuple:
    sequence = generate_sequence()
    question = ' '.join(sequence)
    correct_answer = get_unknown_element(sequence)
    return question, correct_answer
