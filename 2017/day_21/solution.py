#!/usr/bin/python3
import sys
import logging
import re
import numpy

REGEX = re.compile(r'(.*)\s=>\s(.*)')

class Book():
    def __init__(self):
        self.keys = {}
        self.values = {}
        self.index = 0

    def __setitem__(self, key, value):
        self.keys[self.index] = key
        self.values[self.index] = value
        self.index += 1

    def __getitem__(self, key):
        for index, dictkey in self.keys.items():
            if key == dictkey:
                break

        else:
            raise KeyError

        return self.values[index]

    def __repr__(self):
        lines = []
        for index, key in sorted(self.keys.items()):
            value = self.values[index]
            lines.append("{0} -> {1}".format(key, value))

        return "\n".join(lines)

    def match(self, matrix):
        pounds = len(numpy.argwhere(matrix == '#'))
        for index, key in self.keys.items():
            if pounds != len(numpy.argwhere(key == '#')):
                continue

            if numpy.array_equal(matrix, key):
                break

            if numpy.array_equal(numpy.flip(matrix, 0), key):
                break

            if numpy.array_equal(numpy.flip(matrix, 1), key):
                break

            if numpy.array_equal(numpy.rot90(matrix, k=1), key):
                break

            if numpy.array_equal(numpy.rot90(matrix, k=2), key):
                break

            if numpy.array_equal(numpy.rot90(matrix, k=3), key):
                break

            if numpy.array_equal(
                numpy.rot90(numpy.flip(matrix, 0), k=1), key):
                    break

            if numpy.array_equal(
                numpy.rot90(numpy.flip(matrix, 0), k=2), key):
                    break

            if numpy.array_equal(
                numpy.rot90(numpy.flip(matrix, 0), k=3), key):
                    break

            if numpy.array_equal(
                numpy.rot90(numpy.flip(matrix, 1), k=1), key):
                    break

            if numpy.array_equal(
                numpy.rot90(numpy.flip(matrix, 1), k=2), key):
                    break

            if numpy.array_equal(
                numpy.rot90(numpy.flip(matrix, 1), k=3), key):
                    break

            if numpy.array_equal(
                numpy.flip(numpy.flip(matrix, 0), 1), key):
                    break

        else:
            logging.error('key not found, lookin for:\n%s\n\nkeys available:',
                    matrix)
            for key in self.keys.values():
                if pounds == len(numpy.argwhere(key == '#')):
                    print(key)
                    print()

            raise KeyError('key not found')

        return self.values[index]

def convert_matrix(lines):
    size = len(lines)
    grid = numpy.ndarray((size, size), dtype=object)
    for index, line in enumerate(lines):
        grid[index, :] = [c for c  in line]

    return grid

def read_input():
    with open(sys.argv[1], 'r') as input_file:
        data = input_file.readlines()

    data = [line.replace('\n', '') for line in data]
    book = Book()
    for line in data:
        regex = REGEX.search(line)
        key = convert_matrix(regex.group(1).split('/'))
        value = convert_matrix(regex.group(2).split('/'))
        book[key] = value

    return book

def break_matrix(matrix, step):
    rows = []
    size = matrix.shape[0]
    for row in range(0, size, step):
        columns = []
        for column in range(0, size, step):
            columns.append(matrix[row:row+step, column:column+step])

        rows.append(columns)

    return rows

def compile_matrix(rows):
    rows_np = []
    for columns in rows:
        if len(columns) == 1:
            rows_np.append(columns[0])

        else:
            rows_np.append(numpy.concatenate(columns, axis=0))

    if len(rows_np) == 1:
        rows = rows_np[0]

    else:
        rows = numpy.concatenate(rows_np, axis=1)

    return rows

def find_match(book, matrix):
    size = matrix.shape[0]
    if size % 2 == 0:
        rows = break_matrix(matrix, 2)
        replace_rows = []
        for row in rows:
            replace_columns = []
            for square in row:
                value = book.match(square)
                replace_columns.append(value)

            replace_rows.append(replace_columns)

        matrix = compile_matrix(replace_rows)

    elif size % 3 == 0:
        rows = break_matrix(matrix, 3)
        replace_rows = []
        for row_index, rows in enumerate(rows):
            replace_columns = []
            for column_index, square in enumerate(rows):
                value = book.match(square)
                replace_columns.append(value)

            replace_rows.append(replace_columns)

        matrix = compile_matrix(replace_rows)

    else:
        logging.error('wrong size!')
        raise RuntimeError('wrong size')

    return matrix

def part1():
    book = read_input()
    matrix = convert_matrix(['.#.', '..#', '###'])
    for _ in range(4):
        matrix = find_match(book, matrix)
        logging.debug('\n%s', matrix)

    print(matrix.size)
    logging.info('%d pixels are on', len(numpy.argwhere(matrix == '#')))

if __name__ == '__main__':
    FORMAT = '%(asctime)-15s: %(message)s'
    logging.basicConfig(format=FORMAT, level='DEBUG')
    part1()
