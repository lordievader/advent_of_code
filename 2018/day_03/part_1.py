"""Code for part 1 of day 2
"""
import numpy
import re


class Grid():
    def __init__(self, tag):
        self.id = re.search(r'^(#[0-9]+).*', tag).group(1)
        positions = re.search(r'.*@ ([0-9]+),([0-9]+):.*', tag)
        self.positions = (int(positions.group(1)), int(positions.group(2)))
        size = re.search(r'.*: ([0-9]+)x([0-9]+)', tag)
        self.size = (int(size.group(1)), int(size.group(2)))
        self.gen_grid()

    def __repr__(self):
        line = f"{self.id} @ {self.positions} {self.size}"
        return line

    def gen_grid(self):
        self.grid = numpy.ndarray(shape=(1000, 1000), dtype=numpy.int32)
        self.grid[:, :] = 0
        start_x = self.positions[0]
        end_x = self.positions[0] + self.size[0]
        start_y = self.positions[1]
        end_y = self.positions[1] + self.size[1]

        for index in range(start_y, end_y):
            self.grid[start_x:end_x, index] = 1

    def add_grid(self, tag):
        positions = re.search(r'.*@ ([0-9]+),([0-9]+):.*', tag)
        size = re.search(r'.*: ([0-9]+)x([0-9]+)', tag)
        start_x = int(positions.group(1))
        end_x = start_x + int(size.group(1))
        start_y = int(positions.group(2))
        end_y = start_y + int(size.group(2))

        for index in range(start_y, end_y):
            numpy.add(
                self.grid[start_x:end_x, index],
                1,
                self.grid[start_x:end_x, index])


def solution(sequences):
    """Solution to part one.
    """
    grid = Grid(sequences[0])
    for sequence in sequences[1:]:
        grid.add_grid(sequence)

    return len(numpy.where(grid.grid > 1)[0])
