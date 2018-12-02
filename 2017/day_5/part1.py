#!/usr/bin/python3
import sys

def read_input(input_file):
    with open(input_file, 'r') as io_ref:
        data = io_ref.readlines()

    codes = [int(line.replace('\n', '')) for line in data]
    return codes

def jump(data):
    jumping = True
    index = 0
    length = len(data)
    steps = 0
    while jumping is True:
        steps += 1
        offset = data[index]
        if offset >= 3:
            data[index] -= 1

        else:
            data[index] += 1

        index += offset
        if index >= length:
            break

    print('done in {0} steps'.format(steps))

def main():
    data = read_input(sys.argv[1])
    jump(data)

if __name__ == '__main__':
    main()
