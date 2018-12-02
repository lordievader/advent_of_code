#!/usr/bin/env python3.5
import sys
import logging
import re

FORMAT = '%(asctime)-15s: %(message)s'
logging.basicConfig(format=FORMAT, level='DEBUG')

DEPTH = re.compile(r'([0-9]+):')
RANGE = re.compile(r': ([0-9]+)$')

class Layer():
    def __init__(self, depth, range):
        self.depth = depth
        self.range = range
        self.modulo = range * 2 - 2
        self.index = 0
        self.cost = depth * range

    def __repr__(self):
        state = [' '] * self.range
        state[self.index] = 'S'
        line = "{0} [{1}]".format(self.depth, "] [".join(state))
        return line

    def reset(self):
        self.index = 0

    def tick(self, amount=1):
        self.index = (self.index + amount) % self.modulo

    def is_caught(self):
        return self.index == 0

class Firewall():
    def __init__(self, layers):
        self.layers = {}
        self.packet = 0
        for layer in layers:
            depth = int(DEPTH.search(layer).group(1))
            range = int(RANGE.search(layer).group(1))
            self.layers[depth] = Layer(depth, range)

        self.outer_layer = max(self.layers.keys())
        self.depths = set(self.layers.keys())

    def __repr__(self):
        lines = []
        for layer in list(self.layers.values()):
            line = str(layer)
            if layer.depth == self.packet:
                lines.append("* {0}".format(line))

            else:
                lines.append("  {0}".format(line))

        lines.append('')
        return '\n'.join(lines)

    def reset(self):
        self.packet = 0
        for layer in self.layers.values():
            layer.reset()

    def tick(self, amount=1):
        for layer in self.layers.values():
            layer.tick(amount)

    def move_packet(self):
        self.packet += 1

    def is_caught(self):
        cost = 0
        caught = False
        packet = self.packet
        if packet in self.depths:
            layer = self.layers[packet]
            if layer.is_caught() is True:
                cost = layer.cost
                caught = True

        return caught, cost

def read_input(input_file):
    with open(input_file, 'r') as io_ref:
        data = io_ref.readlines()
        
    return [line.replace('\n', '') for line in data]

def operate_firewall(firewall, break_on_caught=False):
    severity = 0
    while firewall.packet < firewall.outer_layer:
        caught, cost = firewall.is_caught()
        if caught is True:
            if break_on_caught is True:
                return

            severity += cost

        firewall.tick()
        firewall.move_packet()
        #print(firewall)

    caught, cost = firewall.is_caught()
    if caught is True:
        severity += cost
        if break_on_caught is True:
            return

    return severity

def part1():
    data = read_input(sys.argv[1])
    firewall = Firewall(data)
    cost = operate_firewall(firewall)
    logging.info('severity of the whole trip: %d', cost)

def part2():
    data = read_input(sys.argv[1])
    delay = 0
    cost = None
    firewall = Firewall(data)
    while cost is None:
        if delay % 100000 == 0:
            logging.debug('delay: %s', delay)

        firewall.reset()
        firewall.tick(delay)

        cost = operate_firewall(firewall, True)
        if cost is None:
            delay += 1

    logging.info('cost is %d when delayed with %d picoseconds', cost, delay)

if __name__ == '__main__':
    part1()
    part2()
