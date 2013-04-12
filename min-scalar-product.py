#!/usr/bin/env python
# https://code.google.com/codejam/contest/32016/dashboard#s=p0
import fileinput


def main(lines):
    cases = int(lines.next())
    for case_number in range(1, cases + 1):
        lines.next()
        v1 = [int(x) for x in lines.next().split()]
        v1.sort()
        v2 = [int(x) for x in lines.next().split()]
        v2.sort()
        v2.reverse()
        print "Case #%d: %d" % (case_number, dot_product(v1, v2))


def dot_product(v1, v2):
    return sum([p * q for p, q in zip(v1, v2)])


if __name__ == '__main__':
    main(fileinput.input())
