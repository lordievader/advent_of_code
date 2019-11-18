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


class Cart():
    """Representation of a cart.
    """
    up = numpy.array([[-1, 0]])
    down = numpy.array([[1, 0]])
    left = numpy.array([[0, -1]])
    right = numpy.array([[0, 1]])

    def __init__(self, direction, row, column):
        self.position = numpy.ndarray(shape=(1, 2), dtype=numpy.int64)
        self.position[0, :] = [row, column]
        self.direction = direction
        self.intersections = 0

    def __lt__(self, other):
        if self.position[0, 0] < other.position[0, 0]:
            return self.position[0, 1] < other.position[0, 1]

        return False

    def __repr__(self):
        line = f"{self.direction_rep} {self.row} {self.column}"
        return line

    @property
    def direction_rep(self):
        """Returns the representation of the direction.
        """

        if numpy.all(self.direction == self.up):
            rep = '^'

        elif numpy.all(self.direction == self.down):
            rep = 'v'

        elif numpy.all(self.direction == self.left):
            rep = '<'

        elif numpy.all(self.direction == self.right):
            rep = '>'

        return rep

    @property
    def row(self):
        """Returns the row position of the cart.
        """
        return self.position[0, 0]

    @property
    def column(self):
        """Returns the column position of the cart.
        """
        return self.position[0, 1]

    def backslash(self):
        """Determines the direction on a backslash.
        """
        if numpy.all(self.direction == self.right):
            self.direction = self.down

        elif numpy.all(self.direction == self.up):
            self.direction = self.left

        elif numpy.all(self.direction == self.left):
            self.direction = self.up

        elif numpy.all(self.direction == self.down):
            self.direction = self.right

        else:
            pdb.set_trace()

    def forwardslash(self):
        """Determines the direction on a forwardslash.
        """
        if numpy.all(self.direction == self.left):
            self.direction = self.down

        elif numpy.all(self.direction == self.up):
            self.direction = self.right

        elif numpy.all(self.direction == self.right):
            self.direction = self.up

        elif numpy.all(self.direction == self.down):
            self.direction = self.left

        else:
            pdb.set_trace()

    def turn_left(self):
        """Turns the cart left.
        """
        if (numpy.all(self.direction == self.up)
                or numpy.all(self.direction == self.down)):
            self.direction = numpy.flip(self.direction, axis=1)

        elif (numpy.all(self.direction == self.left)
                or numpy.all(self.direction == self.right)):
            self.direction = numpy.multiply(numpy.flip(self.direction, axis=1), -1)


    def turn_right(self):
        """Turns the cart right.
        """
        if (numpy.all(self.direction == self.up)
                or numpy.all(self.direction == self.down)):
            self.direction = numpy.multiply(numpy.flip(self.direction, axis=1), -1)

        elif (numpy.all(self.direction == self.left)
                or numpy.all(self.direction == self.right)):
            self.direction = numpy.flip(self.direction, axis=1)

    def plus(self):
        """Determines the direction on an intersection.
        """

        if self.intersections % 3 == 0:
            self.turn_left()

        elif self.intersections % 3 == 2:
            self.turn_right()

        self.intersections += 1

    def next_direction(self, symbol):
        """Determines the next direction.

        :param symbol: the symbol on the grid.
        :type symbol: str:
        """
        if symbol == '\\':
            self.backslash()

        elif symbol == '/':
            self.forwardslash()

        elif symbol == '+':
            self.plus()

    def move(self, grid):
        """Moves the cart one spot according to the grid.
        """
        numpy.add(self.position, self.direction, out=self.position)
        symbol = grid[self.row][self.column]
        self.next_direction(symbol)

    def crash(self, cart):
        """Checks if a cart has crashed.

        :param cart: another cart
        :type cart: Cart
        :return: boolean
        """
        return numpy.all(self.position == cart.position)

def build_grid(problem_input):
    """Build a grid of the problem input.
    Along with a list of carts.

    :param problem_input: input lines
    :type problem_input: str
    :return: list of lines, list of carts
    """
    up = numpy.array([[-1, 0]])
    down = numpy.array([[1, 0]])
    left = numpy.array([[0, -1]])
    right = numpy.array([[0, 1]])
    grid = []
    carts = []
    for row, line in enumerate(problem_input.split('\n')):
        cart = None
        if '^' in line:
            column = line.index('^')
            cart = Cart(up, row, column)
            line = f"{line[:column]}|{line[column+1:]}"

        elif 'v' in line:
            column = line.index('v')
            cart = Cart(down, row, column)
            line = f"{line[:column]}|{line[column+1:]}"

        elif '<' in line:
            column = line.index('<')
            cart = Cart(left, row, column)
            line = f"{line[:column]}-{line[column+1:]}"

        elif '>' in line:
            column = line.index('>')
            cart = Cart(right, row, column)
            line = f"{line[:column]}-{line[column+1:]}"

        grid.append(line)
        if cart is not None:
            carts.append(cart)

    return grid, carts


def print_grid(grid, carts):
    """Prints the current grid with locations of the carts.

    :param grid: grid to print
    :type grid: list
    :param carts: list of carts
    :type carts: list
    """
    lines = []
    for row, line in enumerate(grid):
        for cart in carts:
            if row == cart.row:
                column = cart.column
                line = f"{line[:column]}{cart.direction_rep}{line[column+1:]}"

        lines.append(line)

    print("\n".join(lines))

def crash(carts):
    """Checks if any cart has crashed.

    :param carts: list of carts
    :type carts: list
    :return: boolean
    """
    crashed = False
    position = None
    for index, cart_a in enumerate(carts):
        for cart_b in carts[index+1:]:
            if cart_a.crash(cart_b) == True:
                crashed = True
                position = numpy.flip(cart_a.position, axis=1)
                break

        if crashed is True:
            break

    return crashed, position


def solution(problem_input):
    """Solution to part one.
    """
    grid, carts = build_grid(problem_input)
    # print_grid(grid, carts)
    while crash(carts)[0] is False:
        for cart in sorted(carts):
            cart.move(grid)
            if crash(carts)[0] is True:
                break

        # print_grid(grid, carts)

    position = crash(carts)[1]
    return ",".join([str(x) for x in position[0]])
