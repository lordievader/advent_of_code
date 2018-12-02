#!/usr/bin/env pypy3
import collections
import logging

def advance(ring, input_value=3, index=1):
    ring.rotate(input_value)
    ring.append(index)

def part1():
    ring = collections.deque([0])
    input_value = 349
    pos = 0
    # for index in range(2018):
    #     advance(ring, input_value, index)

    for index in range(1, 2018):
        new = ((pos + input_value ) % index) + 1
        ring.insert(new, index)
        pos = new

    index = ring.index(2017)
    value = ring[index + 1]
    logging.info('value to break the spinlock: %d', value)

def part2():
    logging.debug('begin')
    input_value = 349
    pos = 0
    for index in range(1, 50000001):
        pos = ((pos + input_value ) % index) + 1
        if pos == 1:
            value = index

    logging.info('value to break the spinlock: %d', value)

if __name__ == '__main__':
    FORMAT = '%(asctime)-15s: %(message)s'
    logging.basicConfig(format=FORMAT, level='DEBUG')
    part1()
    part2()
