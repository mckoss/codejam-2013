#!/usr/bin/env python
from itertools import permutations

def main():
    with open('test.txt') as input:
        cases = int(input.readline())
        for case_number in range(1, cases+1):
            input.readline()
            v1 = [int(x) for x in input.readline().split()]
            v1.sort()
            v2 = [int(x) for x in input.readline().split()]
            v2.sort()
            v2.reverse()
            print "Case #%d: %d" % (case_number, dot_product(v1, v2))


def dot_product(v1, v2):
    return sum([p * q for p, q in zip(v1, v2)])

if __name__ == '__main__':
    main()
