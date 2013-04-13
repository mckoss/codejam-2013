#!/usr/bin/env python
# https://code.google.com/codejam/contest/2270488/dashboard#s=p2
import fileinput

test_input = """\
3
1 4
10 120
100 10003
""".split('\n')


def parse(lines):
    """
    >>> ranges = parse(iter(test_input))
    >>> len(ranges)
    3
    >>> ranges
    [[1, 4], [10, 120], [100, 10003]]
    """
    num_ranges = int(lines.next())
    ranges = []
    for _i in range(num_ranges):
        ranges.append([int(x) for x in lines.next().split()])
    return ranges


def main(lines):
    """
    >>> main(iter(test_input))
    Case #1: 2
    Case #2: 0
    Case #3: 2
    """
    ranges = parse(lines)
    n = 2
    for (i, (_first, _last)) in enumerate(ranges):
        print "Case #%d: %d" % (i + 1, n)


if __name__ == '__main__':
    main(fileinput.input())
