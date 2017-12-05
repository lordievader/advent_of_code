#!/usr/bin/python3
import sys

def read_input(input_file):
    with open(input_file, 'r') as io_ref:
        data = io_ref.readlines()

    return data

def process(data):
    valid = 0
    for line in data:
        line = line.replace('\n', '').split(' ')
        words = ["".join(sorted(list(word))) for word in line]
        if len(set(words)) == len(words):
            valid += 1


    return valid

def main():
    data = read_input(sys.argv[1])
    valid = process(data)
    print(valid)

if __name__ == '__main__':
    main()
