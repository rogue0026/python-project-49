from ..games.engine import game_engine
from ..games.prime import game_prime

GAME_OBJECTIVE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    game_engine(GAME_OBJECTIVE, game_prime)


if __name__ == '__main__':
    main()