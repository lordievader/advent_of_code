#!/usr/bin/pypy3
import sys
import logging
import re
import collections

REGEX = re.compile((r'^p=<\s*([-0-9]+,[-0-9]+,[-0-9]+)>,'
                    r'\sv=<\s*([-0-9]+,[-0-9]+,[-0-9]+)>,'
                    r'\sa=<\s*([-0-9]+,[-0-9]+,[-0-9]+)>$'))

class Particle():
    def __init__(self, index, position, velocity, acceleration):
        self.index = index
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def __repr__(self):
        return "{0}: d={1}, p=<{2}>, v=<{3}>, a=<{4}>".format(
            self.index, self.distance, self.position, self.velocity,
            self.acceleration)

    def __lt__(self, other):
        return self.distance < other.distance

    def tick(self):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.velocity[2] += self.acceleration[2]
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]

    @property
    def distance(self):
        return sum([abs(c) for c in self.position])

    @property
    def pos(self):
        return "{0}-{1}-{2}".format(*self.position)

def read_input():
    with open(sys.argv[1], 'r') as input_file:
        data = input_file.readlines()

    data = [line.replace('\n', '') for line in data]
    return data

def process_particle(data):
    particles = []
    for index, line in enumerate(data):
        regex = REGEX.search(line)
        position = [int(c) for c in regex.group(1).split(',')]
        velocity = [int(c) for c in regex.group(2).split(',')]
        acceleration = [int(c) for c in regex.group(3).split(',')]
        particle = Particle(index, position, velocity, acceleration)
        particles.append(particle)

    return particles

def part1():
    data = read_input()
    particles = process_particle(data)
    for _ in range(int(1e4)):
        for particle in particles:
            particle.tick()

    for particle in sorted(particles)[:5]:
        print(particle)

def part2():
    data = read_input()
    particles = process_particle(data)
    start = len(particles)
    for _ in range(int(1e4)):
        for particle in particles:
            particle.tick()

        positions = collections.Counter(
            [particle.pos for particle in particles])
        for position, count in positions.items():
            if count == 1:
                continue

            for particle in particles.copy():
                if particle.pos == position:
                    logging.debug('collision')
                    particles.remove(particle)

    logging.info('start: %d, end: %d', start, len(particles))

if __name__ == '__main__':
    FORMAT = '%(asctime)-15s: %(message)s'
    logging.basicConfig(format=FORMAT, level='DEBUG')
    part1()
    part2()
