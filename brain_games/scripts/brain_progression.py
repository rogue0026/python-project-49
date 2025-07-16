from ..games.engine import game_engine
from ..games.progression import game_progression

GAME_OBJECTIVE = 'What number is missing in the progression?'


def main():
    game_engine(GAME_OBJECTIVE, game_progression)


if __name__ == '__main__':
    main()
