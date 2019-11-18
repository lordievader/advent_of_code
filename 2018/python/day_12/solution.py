#!/usr/bin/env python3
"""Author:      Olivier van der Toorn <oliviervdtoorn@gmail.com>
Description:    Solution for AoC day 02.
"""
import timeit
import functools
import re
import pdb

import part_1


def main():
    """Main function.
    """
    with open('part_1_input', 'r') as input_file:
        problem_input = input_file.read()

    part_1_solution = part_1.solution(problem_input)

    score_previous = part_1.solution(problem_input, 159)
    score = part_1.solution(problem_input, 160)
    diff = score - score_previous
    part_2_solution = (int(5e10) - 160) * diff + score
    print(f"Solution to part one: {part_1_solution}\nSolution to part two: {part_2_solution}")


if __name__ == '__main__':
    main()
