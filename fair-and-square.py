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
    for (i, (first, last)) in enumerate(ranges):
        count = 0
        if is_palindrome(str(first)) and is_fair_square(first):
            count += 1
        r = isqrt(first)
        while True:
            r = next_palindrome(r)
            p = r * r
            if p > last:
                break
            if is_palindrome(str(p)):
                count += 1
        print "Case #%d: %d" % (i + 1, count)


def next_palindrome(x):
    """
    >>> next_palindrome(0)
    1
    >>> next_palindrome(1)
    2
    >>> next_palindrome(9)
    11
    >>> next_palindrome(11)
    22
    >>> next_palindrome(100)
    101
    >>> next_palindrome(101)
    111
    >>> next_palindrome(111)
    121
    >>> next_palindrome(290)
    292
    >>> next_palindrome(205)
    212
    >>> next_palindrome(295)
    303
    """
    s = str(x)
    is_odd = len(s) % 2 == 1
    half_len = len(s) // 2
    l = s[:half_len]
    if is_odd:
        m = s[half_len]
        r = s[:half_len:-1]
    else:
        m = ''
        r = s[:half_len - 1:-1]
    if l > r:
        return int(l + m + l[::-1])
    if is_odd:
        if m != '9':
            m = str(int(m) + 1)
            return int(l + m + l[::-1])
        m = '0'
        if half_len == 0:
            l = '0'
        l = str(int(l) + 1)
        if len(l) > half_len:
            return int(l + l[::-1])
        return int(l + m + l[::-1])
    l = str(int(l) + 1)
    if len(l) > half_len:
        return int(l[:-1] + l[::-1])
    return int(l + l[::-1])


def is_fair_square(x):
    """
    >>> is_fair_square(9)
    True
    >>> is_fair_square(2)
    False
    >>> is_fair_square(99)
    False
    >>> is_fair_square(100)
    False
    >>> is_fair_square(121)
    True
    >>> is_fair_square(676)
    False
    """
    r = isqrt(x)
    return r * r == x and is_palindrome(str(r))


def isqrt(x):
    """
    >>> isqrt(1)
    1
    >>> isqrt(4)
    2
    >>> isqrt(10**6)
    1000
    >>> isqrt(11111111 * 11111111)
    11111111L
    >>> isqrt(12345678901234567890L * 12345678901234567890L)
    12345678901234567890L
    >>> isqrt(33)
    5
    """
    a = 1
    b = x // 2
    if x == 1:
        return 1
    while True:
        a = b
        b = (a + x // a) // 2
        if abs(b - a) <= 1:
            break
    return min(a, b)


def is_palindrome(s):
    """
    >>> is_palindrome('1')
    True
    >>> is_palindrome('12')
    False
    >>> is_palindrome('11')
    True
    >>> is_palindrome('121')
    True
    >>> is_palindrome('122')
    False
    """
    half = len(s) // 2
    is_odd = len(s) % 2 == 1
    if is_odd:
        return s[:half] == s[:half:-1]
    return s[:half] == s[:half - 1:-1]


if __name__ == '__main__':
    main(fileinput.input())
