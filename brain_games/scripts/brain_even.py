from ..games import engine, even

GAME_OBJECTIVE = 'Answer "yes" if the number is even, otherwise answer "no".' 


def main():
    engine.game_engine(GAME_OBJECTIVE, even.even_game)


if __name__ == '__main__':
    main()
