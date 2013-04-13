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
    Case #1: YES
    Case #2: NO
    Case #3: YES
    """
    lawns = parse(lines)
    for i, lawn in enumerate(lawns):
        min_h, max_h = height_range(lawn)
        for height in range(min_h, max_h + 1):
            if not unmow(lawn, height):
                break
        print "Case #%d: %s" % (i + 1, "YES" if len(lawn) == 0 else "NO")


def unmow(lawn, height):
    """
    >>> lawn = [[2, 1, 2], [1, 1, 1], [2, 1, 2]]
    >>> unmow(lawn, 1)
    True
    >>> lawn
    [[2, 2], [2, 2]]
    >>> unmow(lawn, 2)
    True
    >>> lawn
    []
    """
    max_row = len(lawn)
    row = 0
    while row < max_row:
        for col in range(len(lawn[row])):
            if lawn[row][col] != height:
                break
        else:
            lawn.pop(row)
            max_row -= 1
            continue
        row += 1

    if len(lawn) == 0:
        return True

    max_col = len(lawn[0])
    col = 0
    while col < max_col:
        for row in range(len(lawn)):
            if lawn[row][col] != height:
                break
        else:
            for row in range(len(lawn)):
                lawn[row].pop(col)
            max_col -= 1
        col += 1

    for row in range(max_row):
        for col in range(max_col):
            if lawn[row][col] <= height:
                return False

    return True


def height_range(lawn):
    """
    >>> height_range([[2, 1, 2], [1, 1, 1], [2, 1, 2]])
    (1, 2)
    """
    min_h = min(min(row) for row in lawn)
    max_h = max(max(row) for row in lawn)
    return (min_h, max_h)


if __name__ == '__main__':
    main(fileinput.input())
