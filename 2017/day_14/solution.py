#!/usr/bin/env python3.5
import sys
import logging
import collections
import numpy
import pickle
from collections import defaultdict

import knothash

FORMAT = '%(asctime)-15s: %(message)s'
logging.basicConfig(format=FORMAT, level='INFO')

def read_input(input_file):
    with open(input_file, 'r') as io_ref:
        data = io_ref.read().replace('\n', '').split(',')

    return data

def convert(data):
    input_bytes = [ord(c) for c in data]
    input_bytes.extend([17, 31, 73, 47, 23])
    return input_bytes

def hash_to_bits(dense_hash):
    binary = []
    for char in dense_hash:
       binary.append(bin(int(char, base=16))[2:].zfill(4))

    return "".join(binary)

def part1():
    data = sys.argv[1]
    grid = numpy.ndarray((128, 128), dtype=numpy.int)
    for index in range(128):
        data_bytes = convert("{0}-{1}".format(data, index))
        state = knothash.State(data_bytes)
        state.hash_rounds(64)
        dense_hash = state.compress()
        grid[index, :] = [int(c) for c in hash_to_bits(dense_hash)]

    print(grid[:8, :8])
    logging.info('sum of values: %d', numpy.sum(grid))
    return grid

class Region():
    def __init__(self, x=0, y=0, value=1):
        self.value = value
        self.cords = []
        self.map = {'x': defaultdict(list), 'y': defaultdict(list)}
        self.add(x, y)

    def __repr__(self):
        lines = ["{0}, {1}".format(x, y) for x, y in self.cords]
        return "\n".join(lines)

    def add(self, x, y):
        if (x, y) in self.cords:
            return

        self.cords.append((x, y))
        self.map['x'][x].append(y)
        self.map['y'][y].append(x)

    def is_adjacent(self, coordinates):
        add = False
        index = 0
        for x, y in sorted(list(coordinates)):
            if (x, y) in self.cords:
                continue

            adjacent = False
            if x in self.map['x'] and (y + 1 in self.map['x'][x] or y - 1 in 
                                       self.map['x'][x]):
                adjacent = True

            elif y in self.map['y'] and (x + 1 in self.map['y'][y] or x - 1 in 
                                         self.map['y'][y]):
                adjacent = True


            #logging.debug('x: %d, y: %d -- %s', x, y, adjacent)
            if adjacent is True:
                add = True
                self.add(x, y)

        return add

def adjacent(grid):
    regions = []
    value = 1
    coordinates = {(x, y) for x,y in numpy.argwhere(grid==1).tolist()}
    seen = set()
    while len(coordinates) > 0:
        x, y = sorted(list(coordinates))[0]
        if (x, y) in seen:
            continue

        seen |= {(x,y),}
        region = Region(x, y, value)
        value += 1
        regions.append(region)
        while region.is_adjacent(coordinates) is True:
           pass

        seen |= set(region.cords)
        coordinates -= seen

    return regions

def part2():
    grid = part1()
    # with open('part1.example.pickle', 'rb') as dump:
    #     grid = pickle.load(dump)

    regions = adjacent(grid)
    logging.info('number of regions: %d', len(regions))

if __name__ == '__main__':
    #part1()
    part2()
