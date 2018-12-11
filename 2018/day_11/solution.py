#!/usr/bin/env python3
"""Author:      Olivier van der Toorn <oliviervdtoorn@gmail.com>
Description:    Solution for AoC day 02.
"""
import timeit
import functools
import re

import part_1
import part_2


def main():
    """Main function.
    """

    problem_input = 5468
    part_1_solution = part_1.solution(problem_input)
    print(f"Solution to part one: {part_1_solution}")
    part_2_solution = part_2.solution(problem_input)
    print(f"Solution to part one: {part_1_solution}\nSolution to part two: {part_2_solution}")


if __name__ == '__main__':
    main()
