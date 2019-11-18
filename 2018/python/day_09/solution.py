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
    part_1_solution = part_1.solution(445, 71223)
    part_2_solution = part_1.solution(445, 7122300)
    print(f"Solution to part one: {part_1_solution}\nSolution to part two: {part_2_solution}")


if __name__ == '__main__':
    main()
