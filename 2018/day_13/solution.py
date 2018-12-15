#!/usr/bin/env python3
"""Author:      Olivier van der Toorn <oliviervdtoorn@gmail.com>
Description:    Solution for AoC day 02.
"""
import timeit
import functools
import re
import pdb

import part_1
import part_2


def main():
    """Main function.
    """
    with open('part_1_input', 'r') as input_file:
        problem_input = input_file.read()

    part_1_solution = part_1.solution(problem_input)
    part_2_solution = part_2.solution(problem_input)
    print(f"Solution to part one: {part_1_solution}\nSolution to part two: {part_2_solution}")


if __name__ == '__main__':
    main()
