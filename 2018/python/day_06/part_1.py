"""Code for part 1 of day 05.
"""
import re
import numpy
from string import ascii_lowercase, ascii_uppercase

class Coordinate():
    def __init__(self, x, y, name):
        self.name = name
        self.x = x
        self.y = y

    def distance(self, x, y):
        diff_x = abs(self.x - x)
        diff_y = abs(self.y - y)
        return diff_x + diff_y

def bounding_box(coordinates):
    x_min = min([coordinate.x for coordinate in coordinates])
    x_max = max([coordinate.x for coordinate in coordinates]) + 2
    y_min = min([coordinate.y for coordinate in coordinates])
    y_max = max([coordinate.y for coordinate in coordinates]) + 2

    x_min = 0
    y_min = 0
    return (x_min, x_max, y_min, y_max)

def iterate(coordinates, x_min, x_max, y_min, y_max):
    width = x_max - x_min
    height = y_max - y_min
    grid = numpy.ndarray((width, height), dtype=object)
    for row in range(y_min, y_max):
        for column in range(x_min, x_max):
            distances = {}
            for coordinate in coordinates:
                distances[coordinate.name] = coordinate.distance(column, row)

            min_distance = min(distances.values())
            names = [name for name in distances if distances[name] == min_distance]

            x = column - x_min
            y = row - y_min
            if len(names) == 1:
                grid[x, y] = names[0]

            else:
                grid[x, y] = '.'


    return grid.T

def find_square(grid):
    exclude = set(grid[0, :]) | set(grid[:, 0]) | set(grid[-1, :]) | set(grid[:, -1])
    count = numpy.sum(grid)
    include = set(count) - exclude
    counts = [count.count(letter) for letter in include]
    return max(counts)

def solution(sequences):
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
        coordinates.append(Coordinate(x, y, letter))

    x_min, x_max, y_min, y_max = bounding_box(coordinates)
    grid = iterate(
        coordinates,
        x_min, x_max,
        y_min, y_max)
    return find_square(grid)
