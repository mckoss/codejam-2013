#!/usr/bin/env python
# https://code.google.com/codejam/contest/32016/dashboard#s=p0
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
    set(['dbc', 'abc', 'cba', 'bca', 'dac'])
    >>> tests
    ['(ab)(bc)(ca)', 'abc', '(abc)(abc)(abc)', '(zyx)bc']
    """
    nums = lines.next().split()
    _l, d, n = [int(x) for x in nums]
    words = set()
    for _i in range(d):
        words.add(lines.next())
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
    for i, pattern in enumerate(tests):
        feasible = 0
        for word in possible_words(pattern):
            if word in words:
                feasible += 1
        print "Case #%d: %d" % (i + 1, feasible)


def possible_words(pattern):
    """
    >>> list(possible_words('ab'))
    ['ab']
    >>> list(possible_words('(ab)c'))
    ['ac', 'bc']
    >>> list(possible_words('a(bc)'))
    ['ab', 'ac']
    >>> list(possible_words('(a)(bc)'))
    ['ab', 'ac']
    """
    if pattern == '':
        yield ''
        return
    if pattern[0] != '(':
        letters = [pattern[0]]
        pattern = pattern[1:]
    else:
        close_paren = pattern.index(')')
        letters = pattern[1:close_paren]
        pattern = pattern[close_paren + 1:]
    for suffix in possible_words(pattern):
        for letter in letters:
            yield letter + suffix


def dot_product(v1, v2):
    return sum([p * q for p, q in zip(v1, v2)])


if __name__ == '__main__':
    main(fileinput.input())
