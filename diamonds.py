#!/usr/bin/env python
import fileinput
from functools import wraps
from math import sqrt

DEBUG = False

test_input = """\
7
1 0 0
1 0 2
3 0 0
3 2 0
3 1 1
4 1 1
4 0 2""".split('\n')


def parse(lines):
    """
    >>> tests = parse(iter(test_input))
    >>> len(tests)
    7
    >>> tests[0]
    [1, 0, 0]
    """
    num_tests = int(lines.next())
    tests = []
    for _i in range(num_tests):
        tests.append([int(x) for x in lines.next().split(' ')])
    return tests


def main(lines):
    """
    >>> main(iter(test_input))
    Case #1: 1.000000
    Case #2: 0.000000
    Case #3: 1.000000
    Case #4: 0.750000
    Case #5: 0.250000
    Case #6: 0.500000
    Case #7: 0.000000
    """
    tests = parse(lines)
    for i, test in enumerate(tests):
        print "Case #%d: %0.6f" % (i + 1, solve(*test))


def solve(num_diamonds, x, y):
    # print "D: %d, (%d, %d)" % (num_diamonds, x, y)
    full_height = get_height(num_diamonds)
    test_height = (abs(x) + abs(y)) / 2 + 1
    if test_height <= full_height:
        return 1.0
    if test_height > full_height + 1:
        return 0.0
    residual = num_diamonds - d_from_h(full_height)
    return prob(y, residual, 2 * full_height)


def memoize(fn):
    d = dict()

    @wraps(fn)
    def wrapper(*args):
        if args not in d:
            d[args] = fn(*args)
        # print "%r -> %f" % (args, d[args])
        return d[args]

    return wrapper


@memoize
def prob(level, r, m):
    """
    >>> prob(0, 0, 2)
    0.0
    >>> prob(0, 1, 2)
    0.5
    >>> prob(0, 2, 2)
    0.75
    >>> prob(1, 1, 2)
    0.0
    >>> prob(1, 2, 2)
    0.25
    >>> prob(0, 3, 2)
    1.0
    >>> prob(1, 4, 2)
    1.0
    """
    assert r < 2 * m + 1
    if level < 0:
        return 1.0
    if level >= r:
        return 0.0
    filled = prob(level, r - 1, m)
    forced = prob(m - 1, r - 1, m)
    supported = prob(level - 1, r - 1, m)
    added = supported * (0.5 + forced / 2)
    return filled + (1 - filled) * added


def get_height(num_diamonds):
    """
    >>> get_height(1)
    1
    >>> get_height(2)
    1
    >>> get_height(5)
    1
    >>> get_height(6)
    2
    >>> get_height(7)
    2
    >>> get_height(15)
    3
    """
    h = int(sqrt(num_diamonds / 2))
    while True:
        if d_from_h(h) > num_diamonds:
            return h - 1
        h += 1


def d_from_h(h):
    """
    >>> d_from_h(1)
    1
    >>> d_from_h(2)
    6
    >>> d_from_h(3)
    15
    """
    return h * (2 * h - 1)

if __name__ == '__main__':
    main(fileinput.input())
