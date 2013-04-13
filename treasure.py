#!/usr/bin/env python
# https://code.google.com/codejam/contest/2270488/dashboard#s=p3
import fileinput
from collections import Counter

test_input = """\
3
1 4
1
1 0
1 2 1 3
2 0
3 1 2
3 3
1 1 1
1 0
1 0
1 0
1 1
2
1 1 1
""".split('\n')


def parse(lines):
    """
    >>> tests = parse(iter(test_input))
    >>> len(tests)
    3
    >>> tests[0].keys
    Counter({1: 1})
    >>> len(tests[0].chests)
    4
    """
    num_tests = int(lines.next())
    tests = [TreasureTest(lines) for _i in range(num_tests)]
    return tests


def main(lines):
    """
    >>> main(iter(test_input))
    Case #1: 2 1 4 3
    Case #2: 1 2 3
    Case #3: IMPOSSIBLE
    """
    tests = parse(lines)
    for i, treasure in enumerate(tests):
        order = treasure.open_order()
        if order is not None:
            print "Case #%d: %s" % (i + 1, ' '.join([str(x + 1) for x in order]))
        else:
            print "Case #%d: IMPOSSIBLE" % (i + 1)


class TreasureTest(object):
    def __init__(self, lines):
        _num_keys, num_chests = read_ints(lines)
        self.keys = Counter(read_ints(lines))
        self.chests = []
        for _i in range(num_chests):
            nums = read_ints(lines)
            self.chests.append({'lock': nums[0], 'keys': nums[2:]})

    def open_order(self):
        return self._open_order(self.keys, range(len(self.chests)))

    def _open_order(self, keys, chests):
        """ Return True iff chests can be open starting with keys. """
        if len(chests) == 0:
            return []
        if sum(keys.values()) == 0:
            return None
        keys = Counter(keys)
        for i, first in enumerate(chests):
            chest = self.chests[first]
            if keys[chest['lock']] == 0:
                continue
            keys.subtract([chest['lock']])
            keys.update(chest['keys'])
            order = self._open_order(keys, chests[:i] + chests[i + 1:])
            if order is not None:
                return [first] + order
            keys.subtract(chest['keys'])
            keys.update([chest['lock']])

        return None


def read_ints(lines):
    return [int(x) for x in lines.next().split()]


if __name__ == '__main__':
    main(fileinput.input())
