from secrets import randbelow


def get_right_answer(left: int, op: str, right: int) -> str:
    match op:
        case '+':
            return str(left + right)
        case '-':
            return str(left - right)
        case '*':
            return str(left * right)


def calc_game() -> tuple:
    arithmetic_operations = ['+', '-', '*']
    operation = arithmetic_operations[randbelow(len(arithmetic_operations))]
    left_operand = randbelow(50)
    right_operand = randbelow(50)
    question = f'{left_operand} {operation} {right_operand}'
    right_answer = get_right_answer(left_operand, operation, right_operand)
    return question, right_answer
