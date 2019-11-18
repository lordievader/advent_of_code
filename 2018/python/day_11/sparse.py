"""Code for part 1 of day 05.
"""
import logging
import numpy
from scipy.sparse import bsr_matrix
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
    def __init__(self, nodes):
        positions = []
        velocity = []
        for index, node in enumerate(nodes):
            positions.append(node.position)
            velocity.append(node.velocity)

        self.positions = bsr_matrix(positions, shape=(len(nodes), 2), dtype=numpy.int8)
        self.velocity = bsr_matrix(velocity, shape=(len(nodes), 2), dtype=numpy.int8)
        self.bounding_box = (self.max_x, self.max_y)


    def __repr__(self):
        grid = numpy.ndarray(shape=(self.max_y + 1, self.max_x + 1), dtype=object)
        grid[:, :] = '.'
        try:
            for position in self.positions.toarray():
                grid[position[1], position[0]] = '#'

        except IndexError:
            pdb.set_trace()

        lines = []
        lines.append('-------')
        for line in grid:
            lines.append("".join(line))

        lines.append('-------')
        return "\n".join(lines)

    @property
    def max_x(self):
        return numpy.max(self.positions.toarray()[:, 0])

    @property
    def max_y(self):
        return numpy.max(self.positions.toarray()[:, 1])

    @property
    def done(self):
        bounding_box = (self.max_x, self.max_y)
        if bounding_box > self.bounding_box:
            return True

        self.bounding_box = bounding_box
        return False

    def update(self):
        temp = numpy.add(self.positions.toarray(), self.velocity.toarray())
        self.positions = bsr_matrix(temp)

    def previous(self):
        temp = numpy.subtract(self.positions.toarray(), self.velocity.toarray())
        self.positions = bsr_matrix(temp)

def vector(line):
    match = vector_regex.match(line)
    position = (int(match.group(1)), int(match.group(2)))
    velocity = (int(match.group(3)), int(match.group(4)))
    return (position, velocity)

def solution(problem_input):
    """Solution to part one.
    """
    nodes = []
    for line in problem_input:
        position, velocity = vector(line)
        node = Node(position, velocity)
        nodes.append(node)

    grid = Grid(nodes)
    del nodes
    while grid.done is False:
        grid.update()

    grid.previous()
    print(grid)
