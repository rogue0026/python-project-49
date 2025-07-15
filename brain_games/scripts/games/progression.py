from secrets import randbelow

from . import engine


def run_game():
    user_name = engine.greeting_user()
    print('What number is missing in the progression?')
    
    attempts = 0
    all_answers_are_correct = True
    while attempts < engine.MAX_ATTEMPTS:
        sequence = generate_sequence()
        correct_answer = get_unknown_element(sequence)
        engine.create_question(' '.join(sequence))
        user_answer = engine.receive_user_answer()
        if correct_answer != user_answer:
            all_answers_are_correct = False
            engine.send_wrong_answer(user_answer, correct_answer)
            engine.send_try_again(user_name)
            break
        else:
            engine.send_correct_phrase()
            attempts += 1
    
    if all_answers_are_correct:
        engine.send_congratulations(user_name)


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
    unknow_element = None
    
    if idx == 0:
        unknow_element = int(sequence[idx + 1]) - step
    elif idx == len(sequence) - 1 or (idx != 0 and idx != len(sequence) - 1):
        unknow_element = int(sequence[idx - 1]) + step

    return str(unknow_element)
