#!/usr/bin/env python3
"""Author:      Olivier van der Toorn <oliviervdtoorn@gmail.com>
Description:    Solution for AoC day 02.
"""
import re

import part_1
import part_2


def main():
    """Main function.
    """
    with open('part_1_input', 'r') as input_file:
        part_1_input = input_file.read()

    part_1_sequences = re.findall(
            r'\[.*].*[a-z]+',
        part_1_input,
        re.M)
    part_1_solution = part_1.solution(part_1_sequences)
    print(f"Solution to part one: {part_1_solution}")

    part_2_solution = part_2.solution(part_1_sequences)
    print(f"Solution to part two: {part_2_solution}")


if __name__ == '__main__':
    main()
