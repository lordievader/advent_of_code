#!/usr/bin/env pypy3
import sys
import collections
import string
import logging

def read_input(input_file):
    with open(input_file, 'r') as input_data:
        data = input_data.read().replace('\n','').split(',')

    return data

def spin(ring, instruction):
    ring.rotate(instruction)

def exchange(ring, a, b):
    ring[a], ring[b] = ring[b], ring[a]

def partner(ring, a, b):
    a_index = ring.index(a)
    b_index = ring.index(b)
    ring[a_index], ring[b_index] = ring[b_index], ring[a_index]

def part1():
    programs = string.ascii_lowercase[:16]
    ring = collections.deque(programs)
    instructions = read_input(sys.argv[1])

    logging.debug("".join(ring))
    functions = {'s': spin,
                 'x': exchange,
                 'p': partner}
    instructions_decoded = []
    #for instruction in instructions:
    #    functions[instruction[0]](ring, instruction[1:])
    #    instructions_decoded.append((functions[instruction[0]], instruction[1:]))

    for instruction in instructions:
        function = instruction[0]
        arguments = instruction[1:]
        if function == 's':
            arguments = int(arguments)
            spin(ring, arguments)
            arguments = (arguments, )
            function = spin

        elif function == 'x':
            a, b = arguments.split('/')
            a, b = int(a), int(b)
            exchange(ring, a, b)
            arguments = (a, b)
            function = exchange

        elif function == 'p':
            a, b = arguments.split('/')
            partner(ring, a, b)
            arguments = (a, b)
            function = partner

        instructions_decoded.append((function, arguments))


    logging.info("".join(ring))
    return instructions_decoded

def part2(instructions_decoded):
    programs = string.ascii_lowercase[:16]
    ring = collections.deque(programs)

    logging.debug("".join(ring))
    states = []
    count = 1000000000
    for index in range(count):
        if index % 1000 == 0:
            print(index)

        for function, arguments in instructions_decoded:
            function(ring, *arguments)

        if ring not in states:
            states.append(ring.copy())

        else:
            break

    logging.info("".join(ring))
    logging.info("The cycle repeats after %d iterations", index)
    occurences = count % index
    logging.info('The cycle occurs %f times', occurences)
    logging.info('Cycle begins after: %s', states.index(ring))
    ring = collections.deque(programs)
    for index in range(int(occurences)):
        for function, arguments in instructions_decoded:
            function(ring, *arguments)

    logging.info("".join(ring))


if __name__ == '__main__':
    FORMAT = '%(asctime)-15s: %(message)s'
    logging.basicConfig(format=FORMAT, level='DEBUG')
    instructions_decoded = part1()
    part2(instructions_decoded)

