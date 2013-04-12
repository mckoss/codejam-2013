#!/usr/bin/env python
# https://code.google.com/codejam/contest/32016/dashboard#s=p0
import re
import fileinput

test_input = """\
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc
""".split('\n')


def parse(lines):
    """
    >>> words, tests = parse(iter(test_input))
    >>> words
    ['abc', 'bca', 'dac', 'dbc', 'cba']
    >>> tests
    ['(ab)(bc)(ca)', 'abc', '(abc)(abc)(abc)', '(zyx)bc']
    """
    nums = lines.next().split()
    _l, d, n = [int(x) for x in nums]
    words = []
    for _i in range(d):
        words.append(lines.next())
    tests = []
    for _i in range(n):
        tests.append(lines.next())
    return words, tests


def main(lines):
    """
    >>> main(iter(test_input))
    Case #1: 2
    Case #2: 1
    Case #3: 3
    Case #4: 0
    """
    words, tests = parse(lines)
    patterns = [re.compile(pattern_to_regex(test)) for test in tests]
    for i, pattern in enumerate(patterns):
        feasible = 0
        for word in words:
            if pattern.match(word):
                feasible += 1
        print "Case #%d: %d" % (i + 1, feasible)


def pattern_to_regex(test):
    """
    >>> pattern_to_regex('ab')
    'ab'
    >>> pattern_to_regex('(ab)c')
    '(a|b)c'
    >>> pattern_to_regex('a(bc)')
    'a(b|c)'
    """
    if test == '':
        return ''
    if test[0] != '(':
        return test[0] + pattern_to_regex(test[1:])
    close_paren = test.index(')')
    or_exp = '|'.join(list(test[1:close_paren]))
    return "(%s)%s" % (or_exp, pattern_to_regex(test[close_paren + 1:]))


if __name__ == '__main__':
    main(fileinput.input())
