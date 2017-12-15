#!/usr/bin/env python3.5
import sys
import logging
import collections

FORMAT = '%(asctime)-15s: %(message)s'
logging.basicConfig(format=FORMAT, level='DEBUG')


def read_input(input_file):
    with open(input_file, 'r') as io_ref:
        data = io_ref.read().replace('\n', '').split(',')

    return data

def part1():
    data = read_input(sys.argv[1])
    counts = collections.Counter(data)
    logging.debug(counts)
    nw = counts['nw'] - counts['se']
    ne = counts['ne'] - counts['sw']
    n = counts['n'] - counts['s']
    logging.debug('n %d, ne %d, nw %d', n, ne, nw)
    if nw > 0 and ne > 0:
        if nw < ne:
            n += nw
            ne = ne - nw
            nw = 0

        else:
            n += ne
            nw = nw - ne
            ne = 0

    elif nw < 0 and ne < 0:
        if nw > ne:
            n += nw
            ne = ne - nw
            nw = 0

        else:
            n += ne
            nw = nw - ne
            ne = 0

    logging.info('n %d, ne %d, nw %d', n, ne, nw)
    steps = abs(n) + abs(ne) + abs(nw)
    logging.info('Steps from origin: %d', steps)

class State():
    def __init__(self):
        self.north = 0
        self.east = 0

        self.dict = {
            'n': self.move_north,
            'ne': self.north_east,
            'se': self.south_east,
            's': self.south,
            'sw': self.south_west,
            'nw': self.north_west
        }

    def __repr__(self):
        return "north: {0}, east: {1}".format(self.north, self.east)

    def move(self, direction):
        self.dict[direction]()

    def move_north(self):
        self.north += 1

    def north_east(self):
        self.north += 0.5
        self.east += 1

    def south_east(self):
        self.north -= 0.5
        self.east += 1

    def south(self):
        self.north -= 1

    def south_west(self):
        self.north -= 0.5
        self.east -= 1

    def north_west(self):
        self.north += 0.5
        self.east -= 1

    @property
    def steps(self):
        steps = abs(self.east)
        remaining = self.north - (steps / 2)
        logging.debug("%d, %d", steps, remaining)
        steps += remaining
        return steps

def part2():
    data = read_input(sys.argv[1])
    max_distance = 0
    state = State()
    for step in data:
        state.move(step)
        if state.steps > max_distance:
            max_distance = state.steps


    logging.info(state)
    logging.info(state.steps)
    logging.info(max_distance)

if __name__ == '__main__':
    part2()
