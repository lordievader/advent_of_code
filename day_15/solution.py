#!/usr/bin/env python3
import sys
import logging
import collections
from timeit import timeit

FORMAT = '%(asctime)-15s: %(message)s'
logging.basicConfig(format=FORMAT, level='DEBUG')

def generator(N, C, M=1):
    while True:
        N = N * C % 2147483647
        if N % M == 0:
            yield N & 0xffff

def part1():
    # a_value = 65
    # b_value = 8921

    a_value = 703
    b_value = 516

    a_multiply = 16807
    b_multiply = 48271

    divide = 2147483647

    matches = 0
    for _ in range(int(4e7)):
        a_value = (a_value * a_multiply) % divide
        b_value = (b_value * b_multiply) % divide
        if (a_value & 0xffff) == (b_value & 0xffff):
            matches += 1

    logging.info('matches: %d', matches)
    return matches

def part2():
    # a_value = 65
    # b_value = 8921

    a_value = 703
    b_value = 516

    a_multiply = 16807
    b_multiply = 48271

    divide = 2147483647

    matches = 0
    for _ in range(int(5e6)):
        a_value = (a_value * a_multiply) % divide
        while a_value % 4 != 0:
            a_value = (a_value * a_multiply) % divide

        b_value = (b_value * b_multiply) % divide
        while b_value % 8 != 0:
            b_value = (b_value * b_multiply) % divide

        if (a_value & 0xffff) == (b_value & 0xffff):
            matches += 1

    logging.debug('matches: %d', matches)

if __name__ == '__main__':
    logging.info('time part 1: %f', timeit(
        "part1()", setup="from __main__ import part1", number=1))
    logging.info('time part 2: %f', timeit(
        "part2()", setup="from __main__ import part2", number=1))
