#!/usr/bin/env python
import fileinput

DEBUG = False

test_input = """\
""".split('\n')


def parse(lines):
    """
    >>> tests = parse(iter(test_input))
    >>> len(tests)
    0
    """
    num_tests = int(lines.next())
    return [0] * num_tests


def main(lines):
    """
    >>> main(iter(test_input))
    """
    tests = parse(lines)
    for i, test in enumerate(tests):
        print i, test


if __name__ == '__main__':
    main(fileinput.input())
