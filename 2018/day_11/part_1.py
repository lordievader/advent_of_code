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
    def __init__(self, serial):
        self.serial = serial
        self.grid = numpy.ndarray(shape=(300, 300), dtype=numpy.int32)
        self.grid[:, :] = 0
        self.fill_grid()

    def fill_grid(self):
        # Rack ID
        for index in range(300):
            self.grid[index, :] = index

        numpy.add(self.grid, 10, out=self.grid)

        # Powerlevel start
        for index in range(300):
            numpy.multiply(self.grid[:, index], index, out=self.grid[:, index])

        # Add serial
        numpy.add(self.grid, self.serial, out=self.grid)

        # Multiply with rack ID
        for index in range(300):
            numpy.multiply(self.grid[index, :], index + 10, self.grid[index, :])

        # Hundreds digits
        numpy.mod(numpy.floor_divide(self.grid, 100), 10, out=self.grid)

        # Subtract 5
        numpy.subtract(self.grid, 5, out=self.grid)

    def print(self, x_min, x_max, y_min, y_max):
        grid = self.grid[x_min:x_max, y_min:y_max]
        lines = []
        lines.append("-"*(x_max - x_min)*5)
        for row in grid:
            lines.append(", ".join(f"{x:3d}" for x in row))

        lines.append("-"*(x_max - x_min)*5)
        print("\n".join(lines))

    def get(self, location):
        x, y = location
        return self.grid[x, y]

    def region(self, x, y):
        grid = self.grid[x:x+3, y:y+3]
        return grid.sum()

    def find_region(self):
        levels = numpy.ndarray(
            shape=((300 - 3) * (300 - 3), 3), dtype=numpy.int32)
        levels[:, :] = 0
        index = 0
        for x in range(300 - 3):
            for y in range(300 - 3):
                power = self.region(x, y)
                levels[index] = [x, y, power]
                index += 1

        return levels[numpy.where(levels[:, 2] == levels[:, 2].max())]

def solution(serial):
    """Solution to part one.
    """
    grid = Grid(serial)
    region = grid.find_region()
    return tuple(region[0])
