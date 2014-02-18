#!/usr/bin/env python

import fileinput

test_input = """\
3
this is a test
foobar
all your base\
"""


def main(lines):
    """
    >>> main(iter(test_input.split('\\n')))
    Case #1: test a is this
    Case #2: foobar
    Case #3: base your all
    """
    _ = int(lines.next())
    for n, line in enumerate(lines):
        words = line.split()
        print "Case #%d: %s" % (n + 1, ' '.join(words[::-1]))


if __name__ == '__main__':
    main(fileinput.input())
