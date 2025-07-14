import random

import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempts = 0
    all_answers_are_correct = True
    while attempts < 3:
        number = random.randint(0, 1000000)
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            attempts += 1
            continue
        else:
            all_answers_are_correct = False
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if all_answers_are_correct:
        print(f"Congratulations, {name}!")
    

if __name__ == '__main__':
    main()