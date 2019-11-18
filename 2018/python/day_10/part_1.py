"""Code for part 1 of day 05.
"""
import logging
import numpy
import re
import pdb

logging.basicConfig(
    format='%(asctime)-23s %(funcName)15s: %(message)s',
    level=logging.DEBUG
)

vector_regex = re.compile(r'position=<(\s*-*[0-9]+),(\s*-*[0-9]+)> velocity=<(\s*-*[0-9]+),(\s*-*[0-9]+)>')

class Node():
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

class Grid():
    def __init__(self, positions, velocity):
        self.positions = positions
        self.velocity = velocity
        self.previous_size = self.size

    def __repr__(self):
        positions = numpy.subtract(self.positions, self.min)
        size = numpy.flip(
            numpy.add(
                numpy.append(
                    [[0, 0]],
                    [numpy.max(positions, axis=0)],
                    axis=0
                ).sum(axis=0),
                1
            ),
            axis=0
        )
        grid = numpy.ndarray(shape=size, dtype=object)
        grid[:, :] = ' '
        grid[positions[:, 1], positions[:, 0]] = '#'

        lines = []
        for line in grid:
            lines.append("".join(line))

        return "\n".join(lines)

    @property
    def size(self):
        return numpy.abs(
                numpy.append(
                    [numpy.min(self.positions, axis=0)],
                    [numpy.max(self.positions, axis=0)],
                    axis=0
                ).sum(axis=0),
            ).sum(axis=0).prod()

    @property
    def max(self):
        return numpy.array([numpy.max(self.positions, axis=0)])

    @property
    def min(self):
        return numpy.array([numpy.min(self.positions, axis=0)])

    @property
    def done(self):
        size = self.size
        if self.previous_size < size:
            return True

        self.previous_size = size
        return False

    def update(self):
        numpy.add(self.positions, self.velocity, out=self.positions)

def solution(problem_input):
    """Solution to part one.
    """
    length = len(problem_input)
    positions = numpy.ndarray(shape=(length, 2), dtype=numpy.int32)
    velocity = numpy.ndarray(shape=(length, 2), dtype=numpy.int8)
    for index, line in enumerate(problem_input):
        match = vector_regex.match(line)
        positions[index, :] = [int(match.group(1)), int(match.group(2))]
        velocity[index, :] = [int(match.group(3)), int(match.group(4))]

    seconds = 0
    grid = Grid(positions, velocity)
    while grid.done is False:
        grid.update()
        seconds += 1

    print(f"{grid}\n{seconds}")
