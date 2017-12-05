#!/usr/bin/env python3
import sys
def read_input(input_file):
    with open(input_file, 'r') as io_ref:
        data = io_ref.read().replace('\n','')

    return data

def match_sum(input_data):
    length = len(input_data)
    summed = 0
    for index, digit in enumerate(input_data):
        compare_index = int(index + length / 2) % length
        compare_digit = input_data[compare_index]
        if compare_digit == digit:
            summed += int(digit)

    print(summed)

def main():
    input_file = sys.argv[1]
    input_data = read_input(input_file)
    match_sum(input_data)

if __name__ == '__main__':
    main()
