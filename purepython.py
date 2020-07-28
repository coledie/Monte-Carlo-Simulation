"""
Playing a lot of games of craps real slow in pure python.

Single game at a time, repeated.
"""
from random import randint


def roll2() -> int:
    return randint(1, 6) + randint(1, 6)


def simple(n_games: int) -> int:
    """
    Play game of craps in the simplest way possible.

    Returns
    -------
    Number of wins
    """
    wins = 0
    for _ in range(n_games):
        roll_first = roll2()

        if roll_first in [7, 11]:
            wins += 1
        elif roll_first in [2, 3, 12]:
            pass
        else:
            while True:
                roll_curr = roll2()

                if roll_curr == roll_first:
                    wins += 1
                    break
                elif roll_curr == 7:
                    break

    return wins


if __name__ == '__main__':
    N_GAMES = 10**6

    print(simple(N_GAMES) / N_GAMES)

    import timeit
    python_time = timeit.timeit(lambda: simple(N_GAMES), number=1)

    print(f'{N_GAMES} iterations, time: {python_time:.3f}s.')

