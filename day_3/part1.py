#!/usr/bin/python3
import numpy
numpy.set_printoptions(linewidth=100)

def grid(search_value=289326):
    for index in range(int(1e3)):
        block_size = 1 + 2*index
        rl = block_size ** 2
        if rl > search_value:
            # values of the corners
            ll = rl - block_size + 1
            lu = ll - block_size + 1
            ru = lu - block_size + 1
            print((rl, ll, lu, ru))
            # with the above the position of the input value can be found
            # and then it is a matter of tracing it back to the origin
            if rl > search_value > ll:
                print('bottom row')

            elif ll > search_value > lu:
                print('left column')

            elif lu > search_value > ru:
                print('upper row')
                diff = (lu - search_value)
                if diff > 269:
                    diff = diff - 269

                else:
                    diff = 269 - diff

                steps_to_center = diff + index

            else:
                print('right column')

            break

    print(steps_to_center)

def go_up(coordinates):
    start = coordinates[-1]
    x = start[0]
    y = start[1]
    while x != y:
        y += 1
        coordinates.append((x, y))

    return coordinates

def go_left(coordinates):
    start = coordinates[-1]
    x = start[0]
    y = start[1]
    while x != -y:
        x -= 1
        coordinates.append((x, y))

    return coordinates

def go_down(coordinates):
    start = coordinates[-1]
    x = start[0]
    y = start[1]
    while x != y:
        y -= 1
        coordinates.append((x, y))

    return coordinates

def go_right(coordinates):
    start = coordinates[-1]
    x = start[0]
    y = start[1]
    while -x != y:
        x += 1
        coordinates.append((x, y))

    return coordinates

def go_up_half(coordinates):
    start = coordinates[-1]
    x = start[0]
    y = start[1]
    while y != coordinates[0][1] - 1:
        y += 1
        coordinates.append((x, y))

    return coordinates

def go_round(index):
    start = (0 + index, 0)
    coordinates = [start]
    #print('Start: {0}'.format(coordinates))
    coordinates = go_up(coordinates) 
    #print('Up: {0}'.format(coordinates))
    coordinates = go_left(coordinates)
    #print('Left: {0}'.format(coordinates))
    coordinates = go_down(coordinates)
    #print('Down: {0}'.format(coordinates))
    coordinates = go_right(coordinates)
    x, y = coordinates[-1]
    coordinates.append((x + 1, y))
    coordinates = go_up_half(coordinates)
    #print('Right: {0}'.format(coordinates))

    return coordinates

def coordinate_to_matrix(x, y, size):
    middle = int((size - 1) / 2)
    matrix_x = middle + x
    matrix_y = middle + y
    return (matrix_x, matrix_y)

def slice_matrix(x, y, matrix):
    return matrix[x -1:x + 2, y - 1:y + 2]

def test():
    search_value = 289326
    diag = 5
    size = 1 + diag * 2
    zeros = numpy.zeros((size, size))
    middle_x = middle_y = int((size - 1) / 2)
    zeros[middle_x][middle_y] = 1
    for index in range(1, diag + 1):
        coordinates = go_round(index)
        for value, coordinate in enumerate(coordinates):
            #print("{0:3d} {1:3d}".format(*coordinate))
            x = coordinate[0]
            y = coordinate[1]
            matrix_x, matrix_y = coordinate_to_matrix(x, y, size)
            matrixslice  = slice_matrix(matrix_x, matrix_y, zeros)
            value = int(numpy.sum(matrixslice))
            try:
                zeros[matrix_x][matrix_y] = value

            except IndexError:
                print((matrix_x, matrix_y, value))
                break

            if value > search_value:
                print((matrix_x, matrix_y, value))

        #print(numpy.rot90(zeros).astype('int'))

    zeros = numpy.rot90(zeros)
    print(zeros.astype('int'))

def main():
    #grid()
    test()

if __name__ == '__main__':
    main()
