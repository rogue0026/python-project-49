from random import choice, randint


GAME_OBJECTIVE = 'What is the result of the expression?'


def get_right_answer(left: int, op: str, right: int) -> int:
    """Get right answer for arithmetic operation.

    Parameters description:\n
    left - left arithmetic operand;\n
    op - arithmetic operation;\n
    right - right arithmetic operand;
    """
    match op:
        case '+':
            return left + right
        case '-':
            return left - right
        case '*':
            return left * right


def run_game() -> tuple:
    """Implements the logic of the game."""
    arithmetic_operations = ['+', '-', '*']
    operation = choice(arithmetic_operations)
    left_operand = randint(1, 50)
    right_operand = randint(1, 50)
    question = f'{left_operand} {operation} {right_operand}'
    right_answer = get_right_answer(left_operand, operation, right_operand)
    return question, right_answer
