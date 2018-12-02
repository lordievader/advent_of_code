#!/usr/bin/pypy3
import sys
import pprint
import logging

def read_input():
    with open(sys.argv[1], 'r') as input_file:
        data = input_file.readlines()

    data = [line.replace('\n', '') for line in data]
    grid = []
    for line in data:
        grid.append([c for c in line])

    return grid

def move(direction, x, y):
    if direction == 'd':
        y += 1

    elif direction == 'u':
        y -= 1

    elif direction == 'r':
        x += 1

    elif direction == 'l':
        x -= 1

    return x, y

def part1():
    grid = read_input()
    direction = 'd'
    y = 0
    x = grid[y].index('|')
    letters = []
    steps = 0
    while True:
        char = grid[y][x]
        # logging.debug(char)
        # logging.debug("direction %s, (%d, %d)", direction, x, y)
        steps += 1
        if char == '|' or char == '-':
            x, y = move(direction, x, y)

        elif char == '+':
            if direction in ['u', 'd']:
                if grid[y][x - 1] != ' ':
                    direction = 'l'

                elif grid[y][x + 1] != ' ':
                    direction = 'r'

                else:
                    print('Error')

            elif direction in ['r', 'l']:
                if y - 1 >= 0 and grid[y - 1][x] != ' ':
                    direction = 'u'

                elif y + 1 < len(grid) and grid[y + 1][x] != ' ':
                    direction = 'd'

                else:
                    print('Error')


            logging.debug('new direction %s', direction)
            x, y = move(direction, x, y)

        elif char == ' ':
            logging.info('done')
            break

        else:
            letters.append(char)
            x, y = move(direction, x, y)

    logging.info('message reads: %s', "".join(letters))
    logging.info('took %d steps', steps - 1)

if __name__ == '__main__':
    FORMAT = '%(asctime)-15s: %(message)s'
    logging.basicConfig(format=FORMAT, level='DEBUG')
    part1()
