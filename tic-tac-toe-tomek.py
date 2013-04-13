#!/usr/bin/env python
# https://code.google.com/codejam/contest/32016/dashboard#s=p0
import fileinput

test_input = """\
6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O
""".split('\n')


def parse(lines):
    """
    >>> games = parse(iter(test_input))
    >>> len(games)
    6
    >>> games[0]
    'XXXT....OO......'
    >>> len(games[1])
    16
    """
    num_games = int(lines.next())
    games = []
    for _i in range(num_games):
        game = ''
        for _j in range(4):
            game += lines.next()
        lines.next()
        games.append(game)
    return games


def main(lines):
    """
    >>> main(iter(test_input))
    Case #1: X won
    Case #2: Draw
    Case #3: Game has not completed
    Case #4: O won
    Case #5: O won
    Case #6: O won
    """
    games = parse(lines)
    for i, game in enumerate(games):
        winner = check_win(game)
        if winner is not None:
            print "Case #%d: %s won" % (i + 1, winner)
            continue
        if '.' in game:
            print "Case #%d: Game has not completed" % (i + 1)
            continue
        print "Case #%d: Draw" % (i + 1)


def check_win(game):
    def check_four(start, delta):
        letter = game[start]
        if letter == 'T':
            letter = game[start + delta]
        if letter == '.':
            return None
        for i in range(1, 4):
            new_letter = game[start + i * delta]
            if new_letter == 'T':
                continue
            if new_letter != letter:
                return None
        return letter

    for x in range(4):
        winner = check_four(x * 4, 1)
        if winner is not None:
            return winner
        winner = check_four(x, 4)
        if winner is not None:
            return winner
    winner = check_four(0, 5)
    if winner is not None:
        return winner
    return check_four(3, 3)


if __name__ == '__main__':
    main(fileinput.input())
