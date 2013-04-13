#!/usr/bin/env python
# https://code.google.com/codejam/contest/2270488/dashboard#s=p1
import fileinput

test_input = """\
3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1
""".split('\n')


def parse(lines):
    """
    >>> lawns = parse(iter(test_input))
    >>> len(lawns)
    3
    >>> lawns[0]
    [[2, 1, 2], [1, 1, 1], [2, 1, 2]]
    >>> len(lawns[1])
    5
    >>> len(lawns[1][0])
    5
    """
    num_lawns = int(lines.next())
    lawns = []
    for _i in range(num_lawns):
        n, _m = [int(x) for x in lines.next().split()]
        lawn = []
        for _j in range(n):
            nums = lines.next().split()
            lawn.append([int(x) for x in nums])
        lawns.append(lawn)
    return lawns


def main(lines):
    """
    >>> main(iter(test_input))
    """
    _lawns = parse(lines)


if __name__ == '__main__':
    main(fileinput.input())
