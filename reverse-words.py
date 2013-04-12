#!/usr/bin/env python

def main():
    with open('test.txt') as input:
        num = int(input.readline())
        lines = input.readlines()
        for n, line in enumerate(lines):
            words = line.split()
            print "Case #%d: %s" % (n + 1, ' '.join(words[::-1]))

if __name__ == '__main__':
    main()
