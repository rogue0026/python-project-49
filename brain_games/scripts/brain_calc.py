from ..games import calc, engine

GAME_OBJECTIVE = 'What is the result of the expression?'


def main():
    engine.game_engine(GAME_OBJECTIVE, calc.calc_game)


if __name__ == '__main__':
    main()
