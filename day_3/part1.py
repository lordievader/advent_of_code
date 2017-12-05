#!/usr/bin/python3
import numpy

def grid(size=1001):
    zeros = numpy.zeros((size, size))
    middle = int((size - 1) / 2)
    block_size = 1
    for index in range(500):
        block_size = 1 + 2*index
        value = block_size ** 2

        zeros[middle + index][middle + index] = value
        print("{0}: {1} -- {2}".format(index, block_size, value))
        if value > 289326:
            # values of the corners
            rl = value
            ll = rl - block_size + 1
            lu = ll - block_size + 1
            ru = lu - block_size + 1
            print((rl, ll, lu, ru))
            # with the above the position of the input value can be found
            # and then it is a matter of tracing it back to the origin
            break


def main():
    grid()

if __name__ == '__main__':
    main()
