#!/usr/bin/env python3

def read_input():
    with open('input-part1', 'r') as input_file:
        digits = input_file.read().replace('\n', '')

    return digits

def matches(digits):
    summed = 0
    for index, digit in enumerate(digits):
        if index == 0:
            previous = -1

        else:
            previous = index - 1

        previous_digit = digits[previous]
        if previous_digit == digit:
            summed += int(digit)

    return summed

def main():
    digits = read_input()
    print(matches(digits))


if __name__ == '__main__':
    main()
