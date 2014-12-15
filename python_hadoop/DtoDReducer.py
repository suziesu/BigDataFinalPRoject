#!/usr/bin/env python
import itertools, operator, sys

def parseInput():
    for line in sys.stdin:
        yield line.strip('\n').split('\t')

def reducer():
    agg = {}
    for key, values in itertools.groupby(parseInput(), operator.itemgetter(0)):
        count = sum(map(int, zip(*values)[1]))
        (pickup,dropoff) = key.split('|')
        print '%s\t%s\t%s' % (pickup, dropoff, count)

if __name__=='__main__':
    reducer()