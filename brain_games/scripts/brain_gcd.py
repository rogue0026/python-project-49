from ..games import engine
from ..games.gcd import gcd_game

GAME_OBJECTIVE = 'Find the greatest common divisor of given numbers.'


def main():
    engine.game_engine(GAME_OBJECTIVE, gcd_game)


if __name__ == '__main__':
    main()
