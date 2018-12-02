#!/usr/bin/env python3.5
import sys
import logging
import collections

FORMAT = '%(asctime)-15s: %(message)s'
logging.basicConfig(format=FORMAT, level='DEBUG')

class State():
    def __init__(self, lengths, registers=256):
        self.registers = collections.deque(range(registers))
        self.lengths = lengths
        self.current_position = 0
        self.skip_size = 0

    def __repr__(self):
        self.turn(self.current_position, 'back')
        line = "position {0},\nskip size {1},\nlengths {2},\nregisters {3}\n".format(
            self.current_position, self.skip_size, self.lengths, self.registers)
        self.turn(self.current_position)
        return line

    def turn(self, count=1, direction='forward'):
        count = count % len(self.registers)
        if direction == 'forward':
            for _ in range(count):
                self.registers.append(self.registers.popleft())

        else:
            for _ in range(count):
                self.registers.appendleft(self.registers.pop())

    def reverse(self, length):
        start = 0
        end = length
        part = list(self.registers)[start:end]
        for index, value in enumerate(reversed(part)):
            self.registers[start+index] = value

    def move_forward(self, length):
        count = length + self.skip_size
        self.current_position += count
        self.turn(count)

    def hash(self):
        for length in self.lengths:
            self.reverse(length)
            self.move_forward(length)
            self.skip_size += 1

    def hash_rounds(self, count):
        for index in range(count):
            self.hash()

    def compress(self):
        self.turn(self.current_position, 'back')
        step_size = 16
        sparse_hash = list(self.registers)
        dense_hash = []
        for index in range(0, len(sparse_hash), step_size):
            sub_hash = sparse_hash[index:index+step_size]
            value = sub_hash[0]
            for subindex in range(1, len(sub_hash)):
                value = value ^ sub_hash[subindex]

            value = "{0:2x}".format(value).replace(' ', '').zfill(2)
            dense_hash.append(value)

        dense_hash = "".join(dense_hash)
        return dense_hash

def read_input(input_file):
    with open(input_file, 'r') as io_ref:
        data = io_ref.read().replace('\n', '').replace(' ', '')

    return [int(c) for c in data.split(',')]

def read_input_part2(input_file):
    with open(input_file, 'r') as io_ref:
        data = io_ref.read().replace('\n', '').replace(' ', '')

    input_bytes = [ord(c) for c in data]
    input_bytes.extend([17, 31, 73, 47, 23])
    return input_bytes

def part1():
    logging.info('part 1')
    lengths = read_input(sys.argv[1])
    state = State(lengths)
    logging.info('start: %s', state)
    state.hash()
    logging.info('end:\n%s', state)
    state.turn(state.current_position, 'back')
    logging.info('answer: %d * %d = %d',
            state.registers[0], state.registers[1],
            state.registers[0] * state.registers[1])
    logging.info('part 1 done\n\n')

def part2():
    logging.info('part 2')
    lengths = read_input_part2(sys.argv[1])
    state = State(lengths)
    state.hash_rounds(64)
    state.compress()

if __name__ == '__main__':
    #part1()
    part2()
