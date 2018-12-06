import re
import numpy
from string import ascii_lowercase, ascii_uppercase

import part_1

def iterate(coordinates, x_min, x_max, y_min, y_max, distance):
    width = x_max - x_min
    height = y_max - y_min
    grid = numpy.ndarray((width, height), dtype=object)
    for row in range(y_min, y_max):
        for column in range(x_min, x_max):
            distances = []
            for coordinate in coordinates:
                distances.append(coordinate.distance(column, row))

            x = column - x_min
            y = row - y_min
            if sum(distances) < distance:
                grid[x, y] = '#'

            else:
                grid[x, y] = '.'


    return grid.T

def find_square(grid):
    count = numpy.sum(grid)
    return count.count('#')

def solution(sequences, distance):
    """Solution to part one.
    """
    xy_regex = re.compile(r'([0-9]+), ([0-9]+)')
    coordinates = []
    letters = ascii_lowercase + ascii_uppercase
    for index, line in enumerate(sequences):
        xy = xy_regex.match(line)
        x = int(xy.group(1))
        y = int(xy.group(2))
        letter = letters[index]
        coordinates.append(part_1.Coordinate(x, y, letter))

    x_min, x_max, y_min, y_max = part_1.bounding_box(coordinates)
    grid = iterate(
        coordinates,
        x_min, x_max,
        y_min, y_max,
        distance)
    return find_square(grid)
