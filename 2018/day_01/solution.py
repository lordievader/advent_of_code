#!/usr/bin/env python3
"""Author:      Olivier van der Toorn <oliviervdtoorn@gmail.com>
Description:    Solution for AoC day 01.
"""
import re

import part_1
import part_2

def main():
    """Main function.
    """
    with open('part_1_input', 'r') as input_file:
        part_1_input = input_file.read()

    part_1_numbers = re.findall(
        r'[+-][0-9]+',
        part_1_input,
        re.M)
    part_1_solution = part_1.solution(part_1_numbers)
    print(f"Solution to part one: {part_1_solution}")

    part_2_solution = part_2.solution(part_1_numbers)
    print(f"Solution to part two: {part_2_solution}")


if __name__ == '__main__':
    main()
